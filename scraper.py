import platform
import re
import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


# -------------------------------
# CLEAN PRICE
# -------------------------------
def clean_price(price_text):
    price = re.sub(r"[^\d]", "", price_text)
    return int(price) if price.isdigit() else None


# -------------------------------
# SAFE WAIT
# -------------------------------
def safe_wait(driver):
    try:
        driver.find_element(By.TAG_NAME, "body")
        return True
    except:
        return False


# -------------------------------
# AMAZON SCRAPER
# -------------------------------
def scrape_amazon(driver, query):
    if not safe_wait(driver):
        return []

    driver.get("https://www.amazon.in/")
    time.sleep(2)

    try:
        search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    except:
        return []

    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)

    data = []
    products = driver.find_elements(By.CSS_SELECTOR, "div[data-component-type='s-search-result']")

    for product in products[:20]:
        try:
            title = product.find_element(By.TAG_NAME, "h2").text
            link = product.find_element(By.TAG_NAME, "a").get_attribute("href")

            try:
                price_text = product.find_element(By.CSS_SELECTOR, "span.a-price-whole").text
            except:
                price_text = "N/A"

            try:
                image = product.find_element(By.CSS_SELECTOR, "img.s-image").get_attribute("src")
            except:
                image = ""

            price = clean_price(price_text)

            data.append({
                "Website": "Amazon",
                "Title": title,
                "Price": price,
                "Link": link,
                "Image": image
            })

        except:
            continue

    return data


# -------------------------------
# MYNTRA SCRAPER
# -------------------------------
def scrape_myntra(driver, query):
    if not safe_wait(driver):
        return []

    driver.get("https://www.myntra.com/")
    time.sleep(2)

    try:
        search_box = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Search for products, brands and more"]')
    except:
        return []

    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    data = []
    products = driver.find_elements(By.CSS_SELECTOR, "li.product-base")

    for product in products[:20]:
        try:
            brand = product.find_element(By.CSS_SELECTOR, "h3.product-brand").text
            name = product.find_element(By.CSS_SELECTOR, "h4.product-product").text

            try:
                price_text = product.find_element(By.CSS_SELECTOR, "span.product-discountedPrice").text
            except:
                price_text = product.find_element(By.CSS_SELECTOR, "span.product-price").text

            link = product.find_element(By.TAG_NAME, "a").get_attribute("href")

            try:
                image = product.find_element(By.CSS_SELECTOR, "img.img-responsive").get_attribute("src")
            except:
                image = ""

            price = clean_price(price_text)

            data.append({
                "Website": "Myntra",
                "Title": f"{brand} {name}",
                "Price": price,
                "Link": link,
                "Image": image
            })
        except:
            continue

    return data


# -------------------------------
# DRIVER SETUP (Windows + Render)
def get_driver():
    os_name = platform.system()

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")

    # User agent
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        " AppleWebKit/537.36 (KHTML, like Gecko)"
        " Chrome/118.0.5993.70 Safari/537.36"
    )

    # ----------------------
    # WINDOWS LOCAL
    # ----------------------
    if os_name == "Windows":
        from webdriver_manager.chrome import ChromeDriverManager
        print("▶ Running on Windows (LOCAL)")
        return webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

    # ----------------------
    # LINUX (Render)
    # ----------------------
    print("▶ Running on Render (LINUX)")

    options.binary_location = "/usr/bin/chromium"

    return webdriver.Chrome(
        service=Service("/usr/bin/chromedriver"),
        options=options
    )

# -------------------------------
# MAIN SCRAPER
# -------------------------------
def scrape_products(product_name):
    driver = get_driver()
    print("⏳ Scraping started...")

    try:
        amazon_data = scrape_amazon(driver, product_name)
        myntra_data = scrape_myntra(driver, product_name)
    except Exception as e:
        print("❌ ERROR:", e)
        driver.quit()
        return []
    finally:
        try:
            driver.quit()
        except:
            pass

    all_data = amazon_data + myntra_data

    df = pd.DataFrame(all_data)
    df.to_csv("product_with_prices.csv", index=False, encoding="utf-8-sig")

    print("✅ Scraping completed")
    print(f"📦 Total products found: {len(all_data)}")

    return all_data


# -------------------------------
# RUN MANUALLY
# -------------------------------
if __name__ == "__main__":
    product = input("Enter product to search: ")
    scrape_products(product)
