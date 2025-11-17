📈 TrendHive – Real-Time Price Trend Analysis Platform

TrendHive is a real-time price comparison and analytics platform that scrapes product prices from e-commerce sites, stores them in a structured format, and visualizes insights through interactive charts and organized dashboards.

It helps users compare prices, discover trends, and analyze product pricing in a clean and intuitive interface.

<p align="center"> <img src="https://img.shields.io/badge/Backend-Flask-blue" /> <img src="https://img.shields.io/badge/Web%20Scraping-Selenium-orange" /> <img src="https://img.shields.io/badge/Database-MySQL-success" /> <img src="https://img.shields.io/badge/Visualization-Matplotlib-lightgrey" /> <img src="https://img.shields.io/badge/Language-Python-yellow" /> </p>


🔐 User Authentication

Sign Up Page

Login Page

🏠 Home Page

🔍 Product Search & Live Scraping

Search Input Page

Scraping in Progress

📄 Search Results

📊 Dashboard Overview

📈 Analytics & Visualizations
Website Product Share

Price Distribution (Histogram)

Average Price by Website

✨ Features

🔍 Live product scraping using Selenium

🛒 Compare prices across Amazon & Myntra

📊 Interactive dashboard with charts

📈 Matplotlib-powered visual reports

💾 MySQL database integration

📂 CSV download support

🔐 User Authentication System

🎨 Clean, modern & responsive UI

🧰 Tech Stack
Frontend

HTML

CSS

Bootstrap

Backend

Python

Flask

Data Processing

Pandas

CSV

Matplotlib

Scraping

Selenium (Chrome WebDriver)

Database

MySQL
🛠️ Tech Stack
Frontend

HTML

CSS

Bootstrap

Backend

Python (Flask Framework)

Selenium (Live Web Scraping)

MySQL (Database for storing product data)

Pandas (Data cleaning & processing)

Matplotlib (Data visualizations & charts)

Data & Analysis

Python (Pandas, NumPy)

Matplotlib (Graphs for price distribution & averages)

CSV Export Support

📋 Prerequisites

Before running the project, ensure you have the following installed:

Python 3.8 or higher

Google Chrome Browser

ChromeDriver (matching your Chrome version)

MySQL Server

pip (Python package manager)

Git (for cloning, optional)

🚀 Installation & Setup
1. Clone the Repository
git clone https://github.com/Tanvi166/trendhive.git
cd trendhive

2. Backend Setup (Flask)
Install Python Dependencies
pip install -r requirements.txt

Configure Environment Variables

Create a .env file in the project root:

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=trendhive


Also add:

CHROME_DRIVER_PATH=your_chromedriver_path

Start the Backend Server
python app.py


The server will run at:

👉 http://127.0.0.1:5000

3. Set Up MySQL Database

Login to MySQL:

mysql -u root -p


Create database:

CREATE DATABASE trendhive;


Your Flask app will automatically store data after scraping.

4. Selenium Setup
Download ChromeDriver

Get the version matching your Chrome browser from:
https://chromedriver.chromium.org/

Place it somewhere safe and update the path in .env.

🖥️ Running the Platform

Once Flask is running, open your browser and navigate to:

👉 http://127.0.0.1:5000


🗂️ Project Structure
PRICE_TREND_PROJECT/
│── app.py                 # Main Flask application
│── scraper.py             # Selenium scraper for Amazon & Myntra
│── product_with_prices.csv
│── .env                   # Environment variables
│── .gitignore
│── static/                # CSS, JS, images
│── templates/             # HTML files
│── venv/                  # Virtual environment
│── __pycache__/
└── screenshots/           # Add all screenshots here

.

🎯 Usage Guide
First Time Setup

Sign Up: Create a new user account from the signup page.

Login: Use your credentials to access the platform.

Home Page: Search for any product you want to compare.

Live Scraping: TrendHive automatically scrapes prices from Amazon & Myntra.

Results Page: View product list, prices, images, and direct links.

Dashboard: Explore analytics like:

Total products

Average price

Min & max prices

Price distribution

Website share comparison

Charts: Visualize insights using Matplotlib (histogram, bar chart, pie chart).

🔗 API Endpoints (Backend – Flask)
Method	Endpoint	Description
GET	/	Home page
GET/POST	/search	Search products & scrape live data
GET	/dashboard	Show visual dashboard
GET	/download	Download CSV file
POST	/login	User login
POST	/signup	Create new account

(Note: TrendHive is mainly server-rendered using Flask templates. It does not expose React-based JSON APIs.)

🔧 Troubleshooting
Backend Issues
✅ Port Already in Use (5000)

If Flask fails to start:

netstat -ano | findstr :5000
taskkill /PID <PID> /F

✅ Module Not Found

Run:

pip install -r requirements.txt --upgrade

✅ Selenium / ChromeDriver Issues

If ChromeDriver mismatch occurs:

Check your Chrome version

Download correct ChromeDriver

Update path in .env

✅ MySQL Connection Error

Verify DB username/password

Check that MySQL server is running

Ensure database trendhive exists

Scraper Issues
❗ Product Page Layout Changed

Sometimes Amazon/Myntra change HTML structure.
Fix: Update XPaths or CSS selectors in scraper.py.

❗ Too Fast Scraping → Blocking

Add delay:

time.sleep(2)

📊 Data Sources

TrendHive uses real-time scraped data from:

Amazon India

Myntra

Data includes:

Product title

Price

Image

Website source

Product URL

Stored in:

MySQL database

CSV file (product_with_prices.csv)

🤝 Contributing

Contributions are welcome!
Feel free to:

Report issues

Suggest enhancements

Submit pull requests

📝 License

This project is released under the MIT License.

👥 Team

Developed by:

Tanvi

Sanchi

Yashsavi

🏁 Conclusion

TrendHive provides a simple yet powerful way to analyze product pricing trends in real time.
With live scraping, structured storage, and clear visual insights, the platform helps users make informed decisions while shopping online.
📧 Contact

For queries or suggestions, please create an issue on the GitHub repository.

