📈 TrendHive – Real-Time Price Trend Analysis Platform

TrendHive is a real-time price comparison and analytics platform that scrapes product prices from e-commerce sites, stores them in a structured format, and visualizes insights through interactive charts and organized dashboards.

It helps users compare prices, discover trends, and analyze product pricing in a clean and intuitive interface.

<p align="center"> <img src="https://img.shields.io/badge/Backend-Flask-blue" /> <img src="https://img.shields.io/badge/Web%20Scraping-Selenium-orange" /> <img src="https://img.shields.io/badge/Database-MySQL-success" /> <img src="https://img.shields.io/badge/Visualization-Matplotlib-lightgrey" /> <img src="https://img.shields.io/badge/Language-Python-yellow" /> </p>
🖼️ Platform Screenshots

Upload your images inside a /screenshots folder
And GitHub will automatically load them.

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

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone <your-github-repo-link>
cd PRICE_TREND_PROJECT

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Configure Environment Variables

Create a .env file:

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=trendhive

4️⃣ Start Flask Server
python app.py

5️⃣ Open in Browser
http://127.0.0.1:5000

🔍 How the Scraper Works

User enters product name

Selenium opens Amazon & Myntra

Extracts:

Title

Price

Image

Source Website

Product Link

Saves results to MySQL

Converts data to CSV

Matplotlib charts generated

Dashboard displays analytics

🚀 Future Enhancements

Flipkart & Ajio integration

PowerBI dashboard support

Price drop alert system

Background scheduler for daily scraping

Mobile-friendly PWA

User wishlist system

👥 Team Members

Developed by:

Tanvi

Sanchi

Yashsavi

🏁 Conclusion

TrendHive provides a simple yet powerful way to analyze product pricing trends in real time.
With live scraping, structured storage, and clear visual insights, the platform helps users make informed decisions while shopping online.