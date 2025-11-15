
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.chrome.options import Options
# # from webdriver_manager.chrome import ChromeDriverManager
# # import time
# # import pandas as pd
# # import re

# # def clean_price(price_text):
# #     """Convert price string like '₹1,299' or 'Rs. 599' to integer."""
# #     price = re.sub(r'[^\d]', '', price_text)  # remove ₹, Rs., commas, etc.
# #     return int(price) if price.isdigit() else None


# # def scrape_amazon(driver):
# #     driver.get("https://www.amazon.in/")
# #     search_box = driver.find_element(By.ID, "twotabsearchtextbox")
# #     search_box.send_keys("shoes")
# #     search_box.send_keys(Keys.RETURN)
# #     time.sleep(3)

# #     data = []
# #     products = driver.find_elements(By.CSS_SELECTOR, "div[data-component-type='s-search-result']")

# #     for product in products[:20]:
# #         try:
# #             title = product.find_element(By.TAG_NAME, "h2").text
# #             link = product.find_element(By.TAG_NAME, "a").get_attribute("href")
# #             try:
# #                 price_text = product.find_element(By.CSS_SELECTOR, "span.a-price-whole").text
# #             except:
# #                 price_text = "N/A"

# #             price = clean_price(price_text)
# #             data.append({"Website": "Amazon", "Title": title, "Price": price, "Link": link})
# #         except:
# #             continue
# #     return data


# # def scrape_myntra(driver):
# #     driver.get("https://www.myntra.com/")
# #     time.sleep(3)

# #     search_box = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Search for products, brands and more"]')
# #     search_box.send_keys("shoes")
# #     search_box.send_keys(Keys.RETURN)
# #     time.sleep(5)

# #     data = []
# #     products = driver.find_elements(By.CSS_SELECTOR, "li.product-base")

# #     for product in products[:20]:
# #         try:
# #             brand = product.find_element(By.CSS_SELECTOR, "h3.product-brand").text
# #             name = product.find_element(By.CSS_SELECTOR, "h4.product-product").text

# #             # Try discounted price first
# #             try:
# #                 price_text = product.find_element(By.CSS_SELECTOR, "span.product-discountedPrice").text
# #             except:
# #                 price_text = product.find_element(By.CSS_SELECTOR, "span.product-price").text

# #             link = product.find_element(By.TAG_NAME, "a").get_attribute("href")

# #             price = clean_price(price_text)
# #             data.append({"Website": "Myntra", "Title": f"{brand} {name}", "Price": price, "Link": link})
# #         except:
# #             continue
# #     return data


# # if __name__ == "__main__":
# #     options = Options()
# #     options.add_argument("--start-maximized")
# #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# #     print("⏳ Scraping started...")

# #     amazon_data = scrape_amazon(driver)
# #     print(f"✅ Amazon products scraped: {len(amazon_data)}")

# #     myntra_data = scrape_myntra(driver)
# #     print(f"✅ Myntra products scraped: {len(myntra_data)}")

# #     driver.quit()

# #     all_data = amazon_data + myntra_data
# #     df = pd.DataFrame(all_data)
# #     df.to_csv("product_with_prices.csv", index=False, encoding='utf-8-sig')

# #     print("✅ Done scraping all sites.")
# #     print(f"💾 Saved {len(all_data)} products to 'product_with_prices.csv'")















# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.chrome.options import Options
# # from webdriver_manager.chrome import ChromeDriverManager
# # import time
# # import pandas as pd
# # import re


# # def clean_price(price_text):
# #     """Convert price string like '₹1,299' or 'Rs. 599' to integer."""
# #     price = re.sub(r'[^\d]', '', price_text)
# #     return int(price) if price.isdigit() else None


# # def scrape_amazon(driver, query):
# #     driver.get("https://www.amazon.in/")
# #     search_box = driver.find_element(By.ID, "twotabsearchtextbox")
# #     search_box.send_keys(query)
# #     search_box.send_keys(Keys.RETURN)
# #     time.sleep(2)

# #     data = []
# #     products = driver.find_elements(By.CSS_SELECTOR, "div[data-component-type='s-search-result']")

# #     for product in products[:20]:
# #         try:
# #             title = product.find_element(By.TAG_NAME, "h2").text
# #             link = product.find_element(By.TAG_NAME, "a").get_attribute("href")
# #             try:
# #                 price_text = product.find_element(By.CSS_SELECTOR, "span.a-price-whole").text
# #             except:
# #                 price_text = "N/A"
# #                 if link and not link.startswith("http"):
# #                   link = "https://www.amazon.in" + link

# #             price = clean_price(price_text)
# #             data.append({"Website": "Amazon", "Title": title, "Price": price, "Link": link})
# #         except:
# #             continue
# #     return data


# # def scrape_myntra(driver, query):
# #     driver.get("https://www.myntra.com/")
# #     time.sleep(2)

# #     search_box = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Search for products, brands and more"]')
# #     search_box.send_keys(query)
# #     search_box.send_keys(Keys.RETURN)
# #     time.sleep(2)

# #     data = []
# #     products = driver.find_elements(By.CSS_SELECTOR, "li.product-base")

# #     for product in products[:20]:
# #         try:
# #             brand = product.find_element(By.CSS_SELECTOR, "h3.product-brand").text
# #             name = product.find_element(By.CSS_SELECTOR, "h4.product-product").text

# #             try:
# #                 price_text = product.find_element(By.CSS_SELECTOR, "span.product-discountedPrice").text
# #             except:
# #                 price_text = product.find_element(By.CSS_SELECTOR, "span.product-price").text

# #             link = product.find_element(By.TAG_NAME, "a").get_attribute("href")
# #             price = clean_price(price_text)
# #             if link and not link.startswith('http'):
# #                link = "https://www.myntra.in" + link
# #             data.append({"Website": "Myntra", "Title": f"{brand} {name}", "Price": price, "Link": link})
# #         except:
# #             continue
# #     return data


# # # ✅ FUNCTION Flask will call
# # def scrape_products(product_name):
# #     options = Options()
# #     options.add_argument("--start-maximized")
# #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# #     print("⏳ Scraping started...")

# #     amazon_data = scrape_amazon(driver, product_name)
# #     print(f"✅ Amazon products scraped: {len(amazon_data)}")

# #     myntra_data = scrape_myntra(driver, product_name)
# #     print(f"✅ Myntra products scraped: {len(myntra_data)}")

# #     driver.quit()

# #     all_data = amazon_data + myntra_data
# #     df = pd.DataFrame(all_data)
# #     df.to_csv("product_with_prices.csv", index=False, encoding='utf-8-sig')

# #     print("✅ Done scraping all sites.")
# #     print(f"💾 Saved {len(all_data)} products to 'product_with_prices.csv'")

# #     return all_data


# # # ✅ Still runnable manually for testing
# # if __name__ == "__main__":
# #     product = input("Enter product to search: ")
# #     scrape_products(product)















# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.chrome.options import Options
# # from webdriver_manager.chrome import ChromeDriverManager
# # import time
# # import pandas as pd
# # import re


# # def clean_price(price_text):
# #     price = re.sub(r'[^\d]', '', price_text)
# #     return int(price) if price.isdigit() else None


# # def safe_wait(driver):
# #     try:
# #         driver.find_element(By.TAG_NAME, "body")
# #         return True
# #     except:
# #         return False


# # def scrape_amazon(driver, query):
# #     if not safe_wait(driver): return []

# #     driver.get("https://www.amazon.in/")
# #     time.sleep(2)

# #     try:
# #         search_box = driver.find_element(By.ID, "twotabsearchtextbox")
# #     except:
# #         return []

# #     search_box.send_keys(query)
# #     search_box.send_keys(Keys.RETURN)
# #     time.sleep(2)

# #     data = []
# #     products = driver.find_elements(By.CSS_SELECTOR, "div[data-component-type='s-search-result']")

# #     for product in products[:20]:
# #         try:
# #             title = product.find_element(By.TAG_NAME, "h2").text
# #             link = product.find_element(By.TAG_NAME, "a").get_attribute("href")

# #             try:
# #                 price_text = product.find_element(By.CSS_SELECTOR, "span.a-price-whole").text
# #             except:
# #                 price_text = "N/A"

# #             if link and not link.startswith("http"):
# #                 link = "https://www.amazon.in" + link

# #             price = clean_price(price_text)
# #             data.append({"Website": "Amazon", "Title": title, "Price": price, "Link": link})
# #         except:
# #             continue

# #     return data


# # def scrape_myntra(driver, query):
# #     if not safe_wait(driver): return []

# #     driver.get("https://www.myntra.com/")
# #     time.sleep(2)

# #     try:
# #         search_box = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Search for products, brands and more"]')
# #     except:
# #         return []

# #     search_box.send_keys(query)
# #     search_box.send_keys(Keys.RETURN)
# #     time.sleep(1)

# #     data = []
# #     products = driver.find_elements(By.CSS_SELECTOR, "li.product-base")

# #     for product in products[:20]:
# #         try:
# #             brand = product.find_element(By.CSS_SELECTOR, "h3.product-brand").text
# #             name = product.find_element(By.CSS_SELECTOR, "h4.product-product").text

# #             try:
# #                 price_text = product.find_element(By.CSS_SELECTOR, "span.product-discountedPrice").text
# #             except:
# #                 price_text = product.find_element(By.CSS_SELECTOR, "span.product-price").text

# #             link = product.find_element(By.TAG_NAME, "a").get_attribute("href")
# #             if link and not link.startswith("http"):
# #                 link = "https://www.myntra.com" + link

# #             price = clean_price(price_text)
# #             data.append({"Website": "Myntra", "Title": f"{brand} {name}", "Price": price, "Link": link})
# #         except:
# #             continue

# #     return data


# # def scrape_products(product_name):
# #     options = Options()
    
# #     options.add_argument("--start-maximized")
# #     options.add_experimental_option("detach", True)  # ✅ prevents browser from auto-closing
# #     options.add_argument("--disable-blink-features=AutomationControlled")  # ✅ avoid blocking
# #     options.add_argument("--disable-infobars")

# #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# #     driver.implicitly_wait(10)  # ✅ give the browser time for DOM

# #     print("⏳ Scraping started...")

# #     try:
# #         amazon_data = scrape_amazon(driver, product_name)
# #         print(f"✅ Amazon scraped: {len(amazon_data)}")

# #         myntra_data = scrape_myntra(driver, product_name)
# #         print(f"✅ Myntra scraped: {len(myntra_data)}")

# #     except Exception as e:
# #         print("❌ Error during scraping:", e)
# #         driver.quit()
# #         return []

# #     finally:
# #         try:
# #             driver.quit()
# #         except:
# #             pass

# #     all_data = amazon_data + myntra_data
# #     df = pd.DataFrame(all_data)
# #     df.to_csv("product_with_prices.csv", index=False, encoding="utf-8-sig")

# #     print("✅ Done scraping all sites")
# #     print(f"💾 Saved {len(all_data)} products")

# #     return all_data


# # if __name__ == "__main__":
# #     product = input("Enter product to search: ")
# #     scrape_products(product)












# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# import pandas as pd
# import re


# def clean_price(price_text):
#     price = re.sub(r'[^\d]', '', price_text)
#     return int(price) if price.isdigit() else None


# def safe_wait(driver):
#     try:
#         driver.find_element(By.TAG_NAME, "body")
#         return True
#     except:
#         return False


# # ✅ AMAZON SCRAPER WITH IMAGE SUPPORT
# def scrape_amazon(driver, query):
#     if not safe_wait(driver):
#         return []

#     driver.get("https://www.amazon.in/")
#     time.sleep(2)

#     try:
#         search_box = driver.find_element(By.ID, "twotabsearchtextbox")
#     except:
#         return []

#     search_box.send_keys(query)
#     search_box.send_keys(Keys.RETURN)
#     time.sleep(2)

#     data = []
#     products = driver.find_elements(By.CSS_SELECTOR, "div[data-component-type='s-search-result']")

#     for product in products[:20]:
#         try:
#             title = product.find_element(By.TAG_NAME, "h2").text
#             link = product.find_element(By.TAG_NAME, "a").get_attribute("href")

#             try:
#                 price_text = product.find_element(By.CSS_SELECTOR, "span.a-price-whole").text
#             except:
#                 price_text = "N/A"

#             # ✅ Extract product image
#             try:
#                 image = product.find_element(By.CSS_SELECTOR, "img.s-image").get_attribute("src")
#             except:
#                 image = ""

#             if link and not link.startswith("http"):
#                 link = "https://www.amazon.in" + link

#             price = clean_price(price_text)
#             data.append({
#                 "Website": "Amazon",
#                 "Title": title,
#                 "Price": price,
#                 "Link": link,
#                 "Image": image
#             })
#         except:
#             continue

#     return data


# # ✅ MYNTRA SCRAPER WITH IMAGE SUPPORT
# def scrape_myntra(driver, query):
#     if not safe_wait(driver):
#         return []

#     driver.get("https://www.myntra.com/")
#     time.sleep(2)

#     try:
#         search_box = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Search for products, brands and more"]')
#     except:
#         return []

#     search_box.send_keys(query)
#     search_box.send_keys(Keys.RETURN)
#     # time.sleep(2)

#     data = []
#     products = driver.find_elements(By.CSS_SELECTOR, "li.product-base")

#     for product in products[:20]:
#         try:
#             brand = product.find_element(By.CSS_SELECTOR, "h3.product-brand").text
#             name = product.find_element(By.CSS_SELECTOR, "h4.product-product").text

#             try:
#                 price_text = product.find_element(By.CSS_SELECTOR, "span.product-discountedPrice").text
#             except:
#                 price_text = product.find_element(By.CSS_SELECTOR, "span.product-price").text

#             link = product.find_element(By.TAG_NAME, "a").get_attribute("href")
#             if link and not link.startswith("http"):
#                 link = "https://www.myntra.com" + link

#             # ✅ Extract product image
#             try:
#                 image = product.find_element(By.CSS_SELECTOR, "img.img-responsive").get_attribute("src")
#             except:
#                 image = ""

#             price = clean_price(price_text)

#             data.append({
#                 "Website": "Myntra",
#                 "Title": f"{brand} {name}",
#                 "Price": price,
#                 "Link": link,
#                 "Image": image
#             })
#         except:
#             continue

#     return data


# # ✅ Main used by Flask
# def scrape_products(product_name):
#     options = Options()
#     options.add_argument("--start-maximized")
#     options.add_argument("--disable-blink-features=AutomationControlled")
#     options.add_argument("--disable-infobars")
#     options.add_experimental_option("detach", True)

#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#     # driver.implicitly_wait(10)

#     print("⏳ Scraping started...")

#     try:
#         amazon_data = scrape_amazon(driver, product_name)
#         print(f"✅ Amazon scraped: {len(amazon_data)}")

#         myntra_data = scrape_myntra(driver, product_name)
#         print(f"✅ Myntra scraped: {len(myntra_data)}")

#     except Exception as e:
#         print("❌ Error during scraping:", e)
#         driver.quit()
#         return []

#     finally:
#         try:
#             driver.quit()
#         except:
#             pass

#     all_data = amazon_data + myntra_data

#     df = pd.DataFrame(all_data)
#     df.to_csv("product_with_prices.csv", index=False, encoding="utf-8-sig")

#     print("✅ Done scraping all sites")
#     print(f"💾 Saved {len(all_data)} products")

#     return all_data


# # ✅ Run manually if needed
# if __name__ == "__main__":
#     product = input("Enter product to search: ")
#     scrape_products(product)






























# import platform
# import re
# import time
# import pandas as pd

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service


# def clean_price(price_text):
#     price = re.sub(r"[^\d]", "", price_text)
#     return int(price) if price.isdigit() else None


# def safe_wait(driver):
#     try:
#         driver.find_element(By.TAG_NAME, "body")
#         return True
#     except:
#         return False


# # ================= AMAZON =================
# def scrape_amazon(driver, query):
#     if not safe_wait(driver):
#         return []

#     driver.get("https://www.amazon.in/")
#     time.sleep(1.5)

#     try:
#         search_box = driver.find_element(By.ID, "twotabsearchtextbox")
#     except:
#         return []

#     search_box.send_keys(query)
#     search_box.send_keys(Keys.RETURN)
#     time.sleep(2)

#     data = []
#     products = driver.find_elements(By.CSS_SELECTOR, 
#         "div[data-component-type='s-search-result']"
#     )

#     for product in products[:8]:   # ⬅ LIMIT 8 ITEMS
#         try:
#             title = product.find_element(By.TAG_NAME, "h2").text
#             link = product.find_element(By.TAG_NAME, "a").get_attribute("href")
#             try:
#                 price_text = product.find_element(By.CSS_SELECTOR, "span.a-price-whole").text
#             except:
#                 price_text = ""
#             try:
#                 image = product.find_element(By.CSS_SELECTOR, "img.s-image").get_attribute("src")
#             except:
#                 image = ""

#             data.append({
#                 "Website": "Amazon",
#                 "Title": title,
#                 "Price": clean_price(price_text),
#                 "Link": link,
#                 "Image": image
#             })
#         except:
#             continue

#     return data


# # ================= MYNTRA =================
# def scrape_myntra(driver, query):
#     if not safe_wait(driver):
#         return []

#     driver.get("https://www.myntra.com/")
#     time.sleep(1.5)

#     try:
#         search_box = driver.find_element(By.CSS_SELECTOR,
#             'input[placeholder="Search for products, brands and more"]'
#         )
#     except:
#         return []

#     search_box.send_keys(query)
#     search_box.send_keys(Keys.RETURN)
#     time.sleep(3)

#     products = driver.find_elements(By.CSS_SELECTOR, "li.product-base")
#     data = []

#     for product in products[:8]:   # ⬅ LIMIT 8 ITEMS
#         try:
#             brand = product.find_element(By.CSS_SELECTOR, "h3.product-brand").text
#             name = product.find_element(By.CSS_SELECTOR, "h4.product-product").text

#             try:
#                 price_text = product.find_element(By.CSS_SELECTOR, "span.product-discountedPrice").text
#             except:
#                 try:
#                     price_text = product.find_element(By.CSS_SELECTOR, "span.product-price").text
#                 except:
#                     price_text = ""

#             link = product.find_element(By.TAG_NAME, "a").get_attribute("href")
#             try:
#                 image = product.find_element(By.CSS_SELECTOR, "img").get_attribute("src")
#             except:
#                 image = ""

#             data.append({
#                 "Website": "Myntra",
#                 "Title": f"{brand} {name}",
#                 "Price": clean_price(price_text),
#                 "Link": link,
#                 "Image": image
#             })

#         except:
#             continue

#     return data


# # ================= DRIVER =================
# def get_driver():
#     os_name = platform.system()

#     options = Options()
#     options.add_argument("--headless=new")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
#     options.add_argument("--disable-gpu")
#     options.add_argument("--disable-infobars")
#     options.add_argument("--disable-extensions")
#     options.add_argument("--window-size=1280,720")
#     options.add_argument("--disable-blink-features=AutomationControlled")

#     options.add_argument(
#         "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
#         "(KHTML, like Gecko) Chrome/118 Safari/537.36"
#     )

#     if os_name == "Windows":
#         from webdriver_manager.chrome import ChromeDriverManager
#         return webdriver.Chrome(
#             service=Service(ChromeDriverManager().install()),
#             options=options
#         )

#     options.binary_location = "/usr/bin/chromium"
#     return webdriver.Chrome(
#         service=Service("/usr/bin/chromedriver"),
#         options=options
#     )


# # ================= MAIN =================
# def scrape_products(product_name):
#     driver = get_driver()
#     print("Scraping...")

#     try:
#         amazon_data = scrape_amazon(driver, product_name)
#         myntra_data = scrape_myntra(driver, product_name)
#     except Exception as e:
#         print("ERROR:", e)
#         driver.quit()
#         return []
#     finally:
#         driver.quit()

#     all_data = amazon_data + myntra_data
#     pd.DataFrame(all_data).to_csv("product_with_prices.csv", index=False)

#     print("Done:", len(all_data))
#     return all_data














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
    time.sleep(3)

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
    time.sleep(3)

    try:
        search_box = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Search for products, brands and more"]')
    except:
        return []

    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)

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
