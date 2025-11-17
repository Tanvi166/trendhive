from flask import Flask, render_template, request, redirect, session, send_file
import mysql.connector
import pandas as pd
from scraper import scrape_products
from datetime import datetime
from io import StringIO
import plotly.express as px

app = Flask(__name__)

app.secret_key = "trendhive_secret"

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Tanvi@321423",
    database="trendhive"
)
cursor = db.cursor()

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", 
                       (name, email, password))
        db.commit()
        return redirect('/login')
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
        user = cursor.fetchone()
        if user:
            session['user_id'] = user[0]
            return redirect('/home')
        else:
            return render_template('login.html', error="Invalid credentials!")

    return render_template('login.html')

@app.route('/home')
def home():
    if 'user_id' not in session:
        return redirect('/login')
    return render_template('home.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    if 'user_id' not in session:
        return redirect('/login')

    product_name = request.form['product']
    scrape_products(product_name)

    df = pd.read_csv('product_with_prices.csv')
    df = df.dropna(subset=['Title', 'Price', 'Website', 'Link', 'Image'])

    for index, row in df.iterrows():
        cursor.execute("""
            INSERT INTO products (product_name, price, website, link,image, user_id, search_time)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            row['Title'],
            row['Price'],
            row['Website'],
            row['Link'],
            row['Image'],
            session['user_id'],
            datetime.now()
        ))

    db.commit()
    results = df.to_dict(orient='records')
    return render_template('home.html', results=results, product_name=product_name)

@app.route('/history')
def history():
    if 'user_id' not in session:
        return redirect('/login')

    cursor.execute("SELECT product_name, search_time FROM products WHERE user_id=%s ORDER BY search_time DESC", 
                   (session['user_id'],))
    history = cursor.fetchall()
    return render_template('history.html', history=history)

@app.route('/about')
def about():
    return render_template('about.html')


# ✅ ✅ UPDATED DASHBOARD WITH EXTRA CHARTS
@app.route('/dashboard', methods=["GET"])
def dashboard():
    if 'user_id' not in session:
        return redirect('/login')

    try:
        df = pd.read_csv("product_with_prices.csv")
    except:
        return render_template("dashboard.html", error="❌ No scraped data available!")

    df.columns = [c.strip() for c in df.columns]
    df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
    df = df.dropna(subset=["Price"])
    df["Title"] = df["Title"].astype(str)
    df["Website"] = df["Website"].astype(str)
    df["Image"] = df.get("Image", "").fillna("https://via.placeholder.com/100")

    # ---------------- FILTERS ----------------
    sites = sorted(df["Website"].unique())
    selected_sites = request.args.getlist("sites") or sites
    df_filtered = df[df["Website"].isin(selected_sites)]

    title_search = request.args.get("title", "")
    if title_search:
        df_filtered = df_filtered[df_filtered["Title"].str.contains(title_search, case=False)]

    try:
        min_val = float(request.args.get("min", df["Price"].min()))
        max_val = float(request.args.get("max", df["Price"].max()))
    except:
        min_val = df["Price"].min()
        max_val = df["Price"].max()

    df_filtered = df_filtered[(df_filtered["Price"] >= min_val) & (df_filtered["Price"] <= max_val)]

    sort = request.args.get("sort", "low")
    if sort == "low":
        df_filtered = df_filtered.sort_values("Price", ascending=True)
    elif sort == "high":
        df_filtered = df_filtered.sort_values("Price", ascending=False)
    elif sort == "az":
        df_filtered = df_filtered.sort_values("Title", ascending=True)
    elif sort == "za":
        df_filtered = df_filtered.sort_values("Title", ascending=False)

    # ---------------- METRICS ----------------
    total_products = len(df_filtered)
    avg_price = int(df_filtered["Price"].mean()) if not df_filtered.empty else 0
    min_price = int(df_filtered["Price"].min()) if not df_filtered.empty else 0
    max_price = int(df_filtered["Price"].max()) if not df_filtered.empty else 0

    # ---------------- CHART 1 ----------------
    avg_df = df_filtered.groupby("Website")["Price"].mean().reset_index()
    fig = px.bar(avg_df, x="Website", y="Price", text="Price", title="Average Price by Website")
    graph_html = fig.to_html(full_html=False)

    # ✅ EXTRA CHART 2: Histogram
    hist_fig = px.histogram(df_filtered, x="Price", nbins=20, title="Price Distribution")
    histogram_html = hist_fig.to_html(full_html=False)

    # ✅ EXTRA CHART 3: Pie Chart
    pie_fig = px.pie(df_filtered, names="Website", title="Website Product Share", hole=0.3)
    pie_html = pie_fig.to_html(full_html=False)

    # ✅ EXTRA CHART 4: Price Trend (if timestamp exists)
    trend_html = None
    if "search_time" in df_filtered.columns:
        try:
            df_filtered["search_time"] = pd.to_datetime(df_filtered["search_time"])
            line_fig = px.line(
                df_filtered.sort_values("search_time"),
                x="search_time",
                y="Price",
                color="Website",
                title="Price Trends Over Time"
            )
            trend_html = line_fig.to_html(full_html=False)
        except:
            trend_html = None

    # ---------------- PRODUCT LISTS ----------------
    cheap = df_filtered.nsmallest(10, "Price").to_dict("records")
    expensive = df_filtered.nlargest(10, "Price").to_dict("records")

    return render_template(
        "dashboard.html",
        sites=sites,
        selected_sites=selected_sites,
        title_search=title_search,
        min_val=min_val,
        max_val=max_val,
        total_products=total_products,
        avg_price=avg_price,
        min_price=min_price,
        max_price=max_price,
        cheap=cheap,
        expensive=expensive,
        graph_html=graph_html,
        histogram_html=histogram_html,
        pie_html=pie_html,
        trend_html=trend_html,
        sort=sort
    )


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)