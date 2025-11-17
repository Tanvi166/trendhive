from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import re


# 🔹 Clean prices
def clean_price(price_text):
    price = re.sub(r'[^\d]', '', price_text)
    return int(price) if price.isdigit() else None


# 🔹 Basic wait validation
def safe_wait(driver):
    try:
        driver.find_element(By.TAG_NAME, "body")
        return True
    except:
        return False


# ----------------------------------------
# ✅ AMAZON SCRAPER (works in headless)
# ----------------------------------------
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
    time.sleep(2)

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

            # image
            try:
                image = product.find_element(By.CSS_SELECTOR, "img.s-image").get_attribute("src")
            except:
                image = ""

            if link and not link.startswith("http"):
                link = "https://www.amazon.in" + link

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


# ----------------------------------------
# ✅ MYNTRA SCRAPER (FULL HEADLESS FIX)
# ----------------------------------------
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

    # 🔹 SCROLL so Myntra loads all products
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    data = []
    products = driver.find_elements(By.CSS_SELECTOR, "li.product-base")

    for product in products[:20]:
        try:
            brand = product.find_element(By.CSS_SELECTOR, "h3.product-brand").text
            name = product.find_element(By.CSS_SELECTOR, "h4.product-product").text

            # price
            try:
                price_text = product.find_element(By.CSS_SELECTOR, "span.product-discountedPrice").text
            except:
                price_text = product.find_element(By.CSS_SELECTOR, "span.product-price").text

            # link
            link = product.find_element(By.TAG_NAME, "a").get_attribute("href")
            if link and not link.startswith("http"):
                link = "https://www.myntra.com" + link

            # image
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


# ----------------------------------------
# ⭐ MAIN SCRAPER (HEADLESS ENABLED)
# ----------------------------------------
def scrape_products(product_name):

    # FULL HEADLESS CONFIG FOR DEPLOYMENT
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--window-size=1920,1080")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.70 Safari/537.36"
    )

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    print("⏳ Scraping started...")

    try:
        amazon_data = scrape_amazon(driver, product_name)
        print(f"✅ Amazon scraped: {len(amazon_data)}")

        myntra_data = scrape_myntra(driver, product_name)
        print(f"✅ Myntra scraped: {len(myntra_data)}")

    except Exception as e:
        print("❌ Error during scraping:", e)
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

    print("✅ Done scraping all sites")
    print(f"💾 Saved {len(all_data)} products")

    return all_data


# Run manually
if __name__ == "__main__":
    product = input("Enter product to search: ")
    scrape_products(product)




#redo if end above is working
