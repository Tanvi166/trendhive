# from flask import Flask, render_template, request
# import pandas as pd
# import plotly.express as px
# from scraper import scrape_products


# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/login')
# def login():
#     return render_template('login.html')

# @app.route('/scrape', methods=['POST'])
# def scrape():
#     product_name = request.form['product']
#     results = scrape_products(product_name)
#     return render_template('home.html', product_name=product_name, results=results)

# @app.route('/dashboard')
# def dashboard():
   
#     # Load your price data
#     df = pd.read_csv('product_with_prices.csv')

#     # Clean and process
#     df = df.dropna(subset=['Price'])
#     df['Price'] = df['Price'].astype(float)

#     # Create an interactive chart
#     fig = px.bar(df, x='Product Name', y='Price', color='Website',
#                  title='💸 Product Price Comparison Across Platforms',
#                  template='plotly_dark')

#     graph_html = fig.to_html(full_html=False)

# #     return render_template('dashboard.html', graph_html=graph_html)

# # if __name__ == '__main__':
# #     app.run(debug=True)




# from flask import Flask, render_template, request
# from scraper import scrape_products  # You can remove this if not used
# import pandas as pd

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/login')
# def login():
#     return render_template('login.html')

# @app.route('/scrape', methods=['POST'])
# def scrape():
#     product_name = request.form['product']
#     results = scrape_products(product_name)
#     return render_template('home.html', product_name=product_name, results=results)

# @app.route('/dashboard')
# def dashboard():
#     # Simply embed the running Streamlit dashboard
#     return render_template('dashboard.html')

# if __name__ == '__main__':
#     app.run(debug=True)













































# from flask import Flask, render_template, request
# from scraper import scrape_products  # You can remove this if not used
# import pandas as pd

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')


# @app.route('/scrape', methods=['POST'])
# def scrape():
#     product_name = request.form['product']
#     scrape_products(product_name)

#     # Read CSV after scraping
#     df = pd.read_csv('product_with_prices.csv')
#     df = df.dropna(subset=['Title', 'Price', 'Website'])
    
#     # Convert dataframe to list of dicts
#     results = df.to_dict(orient='records')

#     return render_template('home.html', product_name=product_name, results=results)

# @app.route('/dashboard')
# def dashboard():
#     # Simply embed the running Streamlit dashboard
#     return render_template('dashboard.html')

# if __name__ == '__main__':
#     app.run(debug=True)






























# from flask import Flask, render_template, request, redirect, session
# import mysql.connector
# import pandas as pd
# from scraper import scrape_products
# from datetime import datetime

# app = Flask(__name__)
# app.secret_key = "trendhive_secret"

# # Database connection
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Tanvi@321423",
#     database="trendhive"
# )
# cursor = db.cursor()

# @app.route('/')
# def login_page():
#     return render_template('login.html')

# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         password = request.form['password']
        
#         cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", 
#                        (name, email, password))
#         db.commit()
#         return redirect('/login')
#     return render_template('signup.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']

#         cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
#         user = cursor.fetchone()
#         if user:
#             session['user_id'] = user[0]
#             return redirect('/home')
#         else:
#             return render_template('login.html', error="Invalid credentials!")

#     return render_template('login.html')

# @app.route('/home')
# def home():
#     if 'user_id' not in session:
#         return redirect('/login')
#     return render_template('home.html')

# @app.route('/scrape', methods=['GET', 'POST'])
# def scrape():
#     if request.method == 'GET':
#         return redirect('/home')   # prevent error

#     # POST handling
#     if 'user_id' not in session:
#         return redirect('/login')

#     product_name = request.form['product']
#     scrape_products(product_name)

#     df = pd.read_csv('product_with_prices.csv')
#     df = df.dropna(subset=['Title', 'Price', 'Website', 'Link', 'Image'])

#     # Insert scraped data
#     for index, row in df.iterrows():
#         cursor.execute("""
#             INSERT INTO products (product_name, price, website, link,image, user_id, search_time)
#             VALUES (%s, %s, %s, %s, %s, %s, %s)
#         """, (
#             row['Title'],
#             row['Price'],
#             row['Website'],
#             row['Link'],
#             row['Image'],
#             session['user_id'],
#             datetime.now()
#         ))

#     db.commit()

#     results = df.to_dict(orient='records')
#     return render_template('home.html', results=results, product_name=product_name)


# @app.route('/history')
# def history():
#     if 'user_id' not in session:
#         return redirect('/login')

#     cursor.execute("SELECT product_name, search_time FROM products WHERE user_id=%s ORDER BY search_time DESC", 
#                    (session['user_id'],))
#     history = cursor.fetchall()
#     return render_template('history.html', history=history)

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html')
# @app.route('/logout')
# def logout():
#     session.clear()
#     return redirect('/login')

# if __name__ == '__main__':
#     app.run(debug=True)
















# from flask import Flask, render_template, request, redirect, session, send_file
# import mysql.connector
# import pandas as pd
# from scraper import scrape_products
# from datetime import datetime
# from io import StringIO
# import plotly.express as px

# app = Flask(__name__)
# app.secret_key = "trendhive_secret"

# # Database connection
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Tanvi@321423",
#     database="trendhive"
# )
# cursor = db.cursor()

# # -------------------------------
# # LOGIN PAGE
# # -------------------------------
# @app.route('/')
# def login_page():
#     return render_template('login.html')

# # -------------------------------
# # SIGNUP
# # -------------------------------
# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         password = request.form['password']
        
#         cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", 
#                        (name, email, password))
#         db.commit()
#         return redirect('/login')
#     return render_template('signup.html')

# # -------------------------------
# # LOGIN
# # -------------------------------
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']

#         cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
#         user = cursor.fetchone()
#         if user:
#             session['user_id'] = user[0]
#             return redirect('/home')
#         else:
#             return render_template('login.html', error="Invalid credentials!")

#     return render_template('login.html')

# # -------------------------------
# # HOME
# # -------------------------------
# @app.route('/home')
# def home():
#     if 'user_id' not in session:
#         return redirect('/login')
#     return render_template('home.html')

# # -------------------------------
# # SCRAPE PRODUCT
# # -------------------------------
# @app.route('/scrape', methods=['POST'])
# def scrape():
#     if 'user_id' not in session:
#         return redirect('/login')

#     product_name = request.form['product']
#     scrape_products(product_name)

#     df = pd.read_csv('product_with_prices.csv')
#     df = df.dropna(subset=['Title', 'Price', 'Website', 'Link', 'Image'])

#     for index, row in df.iterrows():
#         cursor.execute("""
#             INSERT INTO products (product_name, price, website, link,image, user_id, search_time)
#             VALUES (%s, %s, %s, %s, %s, %s, %s)
#         """, (
#             row['Title'],
#             row['Price'],
#             row['Website'],
#             row['Link'],
#             row['Image'],
#             session['user_id'],
#             datetime.now()
#         ))

#     db.commit()

#     results = df.to_dict(orient='records')
#     return render_template('home.html', results=results, product_name=product_name)

# # -------------------------------
# # HISTORY
# # -------------------------------
# @app.route('/history')
# def history():
#     if 'user_id' not in session:
#         return redirect('/login')

#     cursor.execute("SELECT product_name, search_time FROM products WHERE user_id=%s ORDER BY search_time DESC", 
#                    (session['user_id'],))
#     history = cursor.fetchall()
#     return render_template('history.html', history=history)

# # -------------------------------
# # ABOUT
# # -------------------------------
# @app.route('/about')
# def about():
#     return render_template('about.html')

# # -------------------------------
# # DASHBOARD  ✅ FULL ANALYTICS
# # -------------------------------
# @app.route('/dashboard', methods=["GET"])
# def dashboard():
#     if 'user_id' not in session:
#         return redirect('/login')

#     try:
#         df = pd.read_csv("product_with_prices.csv")
#     except:
#         return render_template("dashboard.html", error="❌ No scraped data available!")

#     # Clean
#     df.columns = [c.strip() for c in df.columns]
#     df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
#     df = df.dropna(subset=["Price"])
#     df["Title"] = df["Title"].astype(str)
#     df["Website"] = df["Website"].astype(str)
#     df["Image"] = df.get("Image", "").fillna("https://via.placeholder.com/100")

#     # Filters
#     sites = sorted(df["Website"].unique())
#     selected_sites = request.args.getlist("sites") or sites

#     df_filtered = df[df["Website"].isin(selected_sites)]

#     title_search = request.args.get("title", "")
#     if title_search:
#         df_filtered = df_filtered[df_filtered["Title"].str.contains(title_search, case=False)]

#     try:
#         min_val = float(request.args.get("min", df["Price"].min()))
#         max_val = float(request.args.get("max", df["Price"].max()))
#     except:
#         min_val = df["Price"].min()
#         max_val = df["Price"].max()

#     df_filtered = df_filtered[(df_filtered["Price"] >= min_val) & (df_filtered["Price"] <= max_val)]

#     sort = request.args.get("sort", "low")

#     if sort == "low":
#         df_filtered = df_filtered.sort_values("Price", ascending=True)
#     elif sort == "high":
#         df_filtered = df_filtered.sort_values("Price", ascending=False)
#     elif sort == "az":
#         df_filtered = df_filtered.sort_values("Title", ascending=True)
#     elif sort == "za":
#         df_filtered = df_filtered.sort_values("Title", ascending=False)

#     # Metrics
#     total_products = len(df_filtered)
#     avg_price = int(df_filtered["Price"].mean()) if not df_filtered.empty else 0
#     min_price = int(df_filtered["Price"].min()) if not df_filtered.empty else 0
#     max_price = int(df_filtered["Price"].max()) if not df_filtered.empty else 0

#     # Chart
#     avg_df = df_filtered.groupby("Website")["Price"].mean().reset_index()
#     fig = px.bar(avg_df, x="Website", y="Price", text="Price", title="Average Price by Website")
#     graph_html = fig.to_html(full_html=False)

#     cheap = df_filtered.nsmallest(10, "Price").to_dict("records")
#     expensive = df_filtered.nlargest(10, "Price").to_dict("records")

#     return render_template(
#         "dashboard.html",
#         sites=sites,
#         selected_sites=selected_sites,
#         title_search=title_search,
#         min_val=min_val,
#         max_val=max_val,
#         total_products=total_products,
#         avg_price=avg_price,
#         min_price=min_price,
#         max_price=max_price,
#         cheap=cheap,
#         expensive=expensive,
#         graph_html=graph_html,
#         sort=sort
#     )

# # -------------------------------
# # LOGOUT
# # -------------------------------
# @app.route('/logout')
# def logout():
#     session.clear()
#     return redirect('/login')


# if __name__ == '__main__':
#     app.run(debug=True)

























from flask import Flask, render_template, request, redirect, session, send_file
import mysql.connector
import pandas as pd
from scraper import scrape_products
from datetime import datetime
from io import StringIO
import plotly.express as px
import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
app.secret_key = "trendhive_secret"

# Database connection
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Tanvi@321423",
#     database="trendhive"
# )
print("DB_HOST =", os.getenv("DB_HOST"))
print("DB_USER =", os.getenv("DB_USER"))
print("DB_PASSWORD =", os.getenv("DB_PASSWORD"))
print("DB_NAME =", os.getenv("DB_NAME"))
print("DB_PORT =", os.getenv("DB_PORT"))


db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    port=int(os.getenv("DB_PORT")),
    use_pure=True
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

import plotly.graph_objects as go

# 1️⃣ AVERAGE PRICE BY WEBSITE (Premium Bar Chart)
def get_avg_price_chart(df):
    avg_data = df.groupby("Website")["Price"].mean().reset_index()

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=avg_data["Website"],
        y=avg_data["Price"],
        marker=dict(
            color=['#FF6A00', '#713FFF', '#2BBF0A', '#00A8E8'],
            line=dict(color="#444", width=1.2),
        ),
        text=avg_data["Price"].round(0),
        textposition="outside",
    ))

    fig.update_layout(
        height=380,
        template="simple_white",
        margin=dict(l=20, r=20, t=20, b=20),
        yaxis=dict(showgrid=True, gridcolor="#eee"),
        xaxis=dict(showline=True, linewidth=1, linecolor='#ccc'),
    )

    return fig.to_html(full_html=False)



# 2️⃣ PRICE DISTRIBUTION (Gradient Histogram)
def get_histogram(df):
    fig = go.Figure()

    fig.add_trace(go.Histogram(
        x=df["Price"],
        nbinsx=20,
        marker=dict(
            color="#713FFF",
            opacity=0.85
        )
    ))

    fig.update_layout(
        height=350,
        template="simple_white",
        margin=dict(l=20, r=20, t=20, b=20),
        yaxis=dict(showgrid=True, gridcolor="#eee"),
        xaxis=dict(showline=True, linewidth=1, linecolor='#ccc'),
    )

    return fig.to_html(full_html=False)



# 3️⃣ PIE CHART (Beautiful Donut Chart)
def get_pie_chart(df):
    website_counts = df["Website"].value_counts()

    fig = go.Figure(data=[go.Pie(
        labels=website_counts.index,
        values=website_counts.values,
        hole=0.55,
        marker=dict(
            colors=['#FF6A00', '#713FFF', '#2BBF0A', '#00A8E8'],
            line=dict(color='white', width=2)
        ),
        textinfo="label+percent",
        textfont=dict(size=14)
    )])

    fig.update_layout(
        height=330,
        margin=dict(l=20, r=20, t=20, b=20),
        showlegend=False
    )

    return fig.to_html(full_html=False)



# 4️⃣ PRICE TREND OVER TIME (Smooth Line Chart)
def get_trend(df):
    if {"open","high","low","close"}.issubset(df.columns):
        fig = go.Figure(data=[go.Candlestick(
            x=df["search_time"],
            open=df["open"],
            high=df["high"],
            low=df["low"],
            close=df["close"]
        )])

        fig.update_layout(
            height=380,
            template="simple_white",
            margin=dict(l=20, r=20, t=20, b=20)
        )

        return fig.to_html(full_html=False)

    return None


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

# ---------------- PREMIUM MODERN CHARTS ----------------
    graph_html = get_avg_price_chart(df_filtered)
    histogram_html = get_histogram(df_filtered)
    pie_html = get_pie_chart(df_filtered)
    trend_html = get_trend(df_filtered)

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










