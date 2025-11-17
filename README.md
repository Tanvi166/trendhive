# 🐝 TrendHive – Smart Price Comparison & Trend Analysis Platform

TrendHive is a real-time product price comparison and analysis platform that helps users discover trending items, compare prices across e-commerce websites, and analyze price insights visually using interactive graphs.  
It is built using **Flask, Selenium, Pandas, MySQL, and Matplotlib** to provide clean insights and smooth user experience.

---

## 🖼️ Platform Screenshots
---

### 🔐 Login Page  
![Login](static/images/login.png)

### 📝 Sign Up Page  
![Signup](static/images/signup.png)

### 🏠 Home Page  
![Home](static/images/home.png)

### 🔍 Product Search  
![Search](static/images/search.png)

### 📄 Search Results  
![Search Results](static/images/search_results.png)

### 📊 Dashboard Overview  
![Dashboard](static/images/dashboard.png)

### 📈 Average Price by Website  
![Graph 1](static/images/graph1_avg_price.png)

### 📉 Price Distribution (Histogram)  
![Graph 2](static/images/graph2_distribution.png)

### 🍩 Website Product Share  
![Graph 3](static/images/graph3_share.png)

### 🛍️ Cheapest & Most Expensive Products  
![Top Products](static/images/cheapest_expensive.png)

---

## ✨ Features
---

- 🔍 Real-time product scraping using Selenium  
- 🛒 Price comparison from Amazon & Myntra  
- 📦 Organized results table with product images & links  
- 📊 Interactive visual dashboard (bar, pie, histogram)  
- 💾 Data stored & processed using Pandas + CSV  
- 🔐 User authentication (Login/Signup)  
- ⚡ Fast Flask API backend  

---

## 🛠️ Tech Stack
---

### **Frontend**
- HTML5  
- CSS3  
- Bootstrap  
- JavaScript  

### **Backend**
- Python Flask  
- Selenium Web Scraping  
- Pandas for Data Processing  
- Matplotlib for Visual Graphs  
- MySQL Database  
- CORS Enabled API  

### **Data Processing**
- Pandas  
- NumPy  
- Matplotlib  

---

## 📂 Project Structure
---

TrendHive/
│
├── static/ # Static frontend files
│ ├── images/ # Screenshots used in README
│ └── styles.css # CSS styling
│
├── templates/ # Frontend HTML templates
│ ├── home.html
│ ├── login.html
│ ├── signup.html
│ ├── dashboard.html
│ └── results.html
│
├── scraper.py # Selenium scraper script
├── app.py # Flask backend server
├── product_with_prices.csv # Generated data file
├── requirements.txt # Dependencies
├── .env # Environment variables
└── README.md # Project documentation

yaml
Copy code

---

## 🚀 Installation & Setup
---

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/Tanvi166/trendhive.git
cd trendhive
2️⃣ Install Python Dependencies
bash
Copy code
pip install -r requirements.txt
3️⃣ Configure Environment Variables
Create a .env file:

ini
Copy code
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=trendhive
4️⃣ Start the Flask Server
bash
Copy code
python app.py
Backend will run on:
👉 http://localhost:5000

🎯 Usage Guide
🔐 Login or sign up

🔍 Enter a product name to search

🤖 System scrapes live data

📄 View product results table

📊 Open dashboard to analyze graphs:

Average price comparison

Price distribution histogram

Website product share

Cheapest & most expensive items

📥 Export CSV if needed

🔧 Troubleshooting
❗ Module Not Found
bash
Copy code
pip install -r requirements.txt --upgrade
❗ MySQL Connection Error
Check .env credentials.

❗ Port Already in Use
bash
Copy code
netstat -ano | findstr :5000
taskkill /PID <PID> /F
🗂️ Data Sources
Live scraped product data

Amazon

Myntra

CSV storage for analysis

👥 Team
Tanvi

Sanchi

Yashsavi

📜 License
MIT License

📧 Contact
For queries, open an issue on GitHub.
TrendHive – Shop Smart. Compare Better. Save More. 🐝

yaml
Copy code

---

# ✅ Done!  
Just paste the entire Markdown block into your **README.md** and GitHub will render it perfectly — including the **exact project structure lines** like your friend’s.

If you want badges, colors, or a banner at the top, I can add that too