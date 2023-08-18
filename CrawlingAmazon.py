from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import time
from bs4 import BeautifulSoup as bs
from lxml import html
from selenium.webdriver import FirefoxOptions
import re
import pandas as pd



"""
driver.get("https://www.amazon.in")
driver.find_element(By.ID, "nav-global-location-popover-link").click()
driver.find_element(By.ID, "GLUXZipUpdateInput").send_keys('110020')
Another wayt to click 
driver.find_element(By.XPATH,'//span[@id="GLUXZipUpdate"]//input[@class="a-button-input"]').click()
driver.find_element(By.XPATH, "//span[@id='GLUXZipUpdate']//span").click()

itservices.aah@byldgroup.com
110020, 110006, 110006
Bread, sports, beauty


"""


OuputData = []
base_url = "https://www.amazon.in{}"

# Cleaning the price.
def clean_price(price):
    if price and isinstance(price, str):
        price = price.lower().replace('₹', '').replace(',', '').strip() if price else ''
    return price



# Cleaning title 
def clean_title(title):
    if title not in [None, '']:
        title = title.replace('\r', '').replace('\n', '').replace('\t', '').strip()
    return title


# Function is for pagination or next pages
def CrawlingNextPage(driver,NextPageUrl,category):
    driver.get(NextPageUrl)
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    soup = bs(driver.page_source,'html.parser')
    products = soup.findAll("div","a-section a-spacing-base")
    time.sleep(2)
    for product in products:
        item = dict()
        product_url = product.find("a","a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
        item["product_url"] = base_url.format(product_url) if product_url else ""
        title = product.find("span","a-size-base-plus a-color-base a-text-normal")
        item["title"] = clean_title(title.text) if title else ""
        price = product.find("span","a-price")
        item["offer_price"] = clean_price(price.find("span","a-offscreen").text) if price else ""
        item["list_price"]  = item["offer_price"]
        brand = product.find("span","a-color-information a-text-bold")
        item["brand"] = clean_title(brand.text) if brand else ""
        image_url = product.find("div","a-section aok-relative s-image-square-aspect")
        item["image_url"] = image_url.find("img").get("src") if image_url.find("img") else ""
        item['Category'] = category
        print(f"Data for Next Page :- {item}")
        OuputData.append(item)
    
    try:
        next_page = soup.find("span","s-pagination-strip")
        if next_page and next_page.find("a","s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"):
            next_url = next_page.find("a","s-pagination-item s-pagination-next s-pagination-button s-pagination-separator").get("href")
            CrawlingNextPage(driver, base_url.format(next_url),category)
    except Exception as e:
        print(f"Error in Pagiantion {e}")


def start_request():
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    driver = webdriver.Firefox()
    # driver = webdriver.Firefox(options=opts)
    url = "https://www.amazon.in"
    PinCode = ["110020", "110006"]
    Category = ["Bread", "beauty"]
    try:
        driver.get(url)
    except WebDriverException as e:
        print(f"issue in webdriver please check...{e}")
        return False
    except Exception as e:
        print("issue in getting url in browser pls check browers or url")
        return False
    driver.implicitly_wait(5) # wait untill tag visible
    for index, data in enumerate(zip(PinCode,Category)):
        time.sleep(2)
        print(data[0])
        driver.find_element(By.ID, "nav-global-location-popover-link").click()
        time.sleep(2)
        driver.find_element(By.ID, "GLUXZipUpdateInput").clear()
        driver.find_element(By.ID, "GLUXZipUpdateInput").send_keys(data[0])
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[@id='GLUXZipUpdate']//span").click()
        driver.implicitly_wait(10)
        time.sleep(2)
        driver.find_element(By.ID, "twotabsearchtextbox").send_keys(data[1])
        time.sleep(5)
        driver.find_element(By.ID, "nav-search-submit-button").click()
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        soup = bs(driver.page_source,'html.parser')
        products = soup.findAll("div","a-section a-spacing-base")
        print("Length of products :- {}".format(len(products)))
        time.sleep(2)
        for product in products:
            item = dict()
            product_url = product.find("a","a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
            item["product_url"] = base_url.format(product_url.get("href")) if product_url else ""
            title = product.find("span","a-size-base-plus a-color-base a-text-normal")
            item["title"] = clean_title(title.text) if title else ""
            price = product.find("span","a-price")
            item["offer_price"] = clean_price(price.find("span","a-offscreen").text) if price else ""
            item["list_price"]  = item["offer_price"]
            image_url = product.find("div","a-section aok-relative s-image-square-aspect")
            item["image_url"] = image_url.find("img").get("src") if image_url.find("img") else ""
            item["Category"] = data[1]
            print(f"Data for 1 Page :- {item}")
            OuputData.append(item)
        


        # For pagination or next pages. you need to uncommit the these lines and the funtion is created just need to uncommit the lines
        # time.sleep(2)
        # try:
        #     next_page = soup.find("span","s-pagination-strip")
        #     if next_page and next_page.find("a","s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"):
        #         next_url = next_page.find("a","s-pagination-item s-pagination-next s-pagination-button s-pagination-separator").get("href")
        #         CrawlingNextPage(driver, base_url.format(next_url),data[1])
        # except Exception as e:
        #     print(f"Error in Pagiantion {e}")



        # Opne the new tab for opening the website and searching the keys
        driver.execute_script("window.open('');") 
        driver.switch_to.window(driver.window_handles[index+1]) # switch to new tab to get weather info for another city 

        try:
            driver.get(url)
        except WebDriverException as e:
            print(f"issue in webdriver please check...{e}")
            break
        except Exception as e:
            print("issue in getting url in browser pls check browers or url")


# Calling the start function for start the scraping the data
fdata = start_request()

print("Generating The Output files for Excel and CSV")
time.sleep(2)
df = pd.DataFrame(OuputData)
df.to_excel("ExcelFiles_OutputFile.xlsx",index=False)
df.to_csv("CsvFiles_OutputFile.csv",index=False)

print("Done.......")    


