import requests
import logging
from loguru import logger
import re
from time import sleep
from random import randint
import threading
from concurrent.futures import ThreadPoolExecutor
# import httpx
from selenium import webdriver
import time
# from selenium.webdriver.chrome.options import Options
import seleniumwire.undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import socket
from bs4 import BeautifulSoup as BS
import json
import mysql.connector
import datetime
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import datetime
# from connection1 import DB_conn
# EventId = 3285
price_class_id = 4261
bold_red = "\x1b[31;1m"
yellow = "\x1b[33;20m"
red = "\x1b[31;20m"
reset = "\x1b[0m"
format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
logging.CRITICAL: bold_red + format + reset
logging.WARNING: yellow + format + reset
logging.DEBUG: red + format + reset
from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import random
import mysql.connector

# connection_to_db = mysql.connector.connect( host = 'localhost',
#                                                 port = '3306',
#                                                 database = 'lightercreditco_db',
#                                                 user = 'root',
#                                                 password = 'admin',
#                                                 )

# cursor_conn = connection_to_db.cursor()
# connection_to_db = mysql.connector.connect( host = '69.16.249.74',
#                                                 port = '3306',
#                                                 database = 'lightercreditco_db',
#                                                 user = 'lightercreditco_workbench',
#                                                 password = 'XLJ4Q)NVR{GP',
#                                                 ssl_disabled = True
#                                                 )
                                                

# cursor_conn = connection_to_db.cursor()

session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)
session.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Origin': 'https://developer.ticketmaster.com',
    'Connection': 'keep-alive',
    'Referer': 'https://developer.ticketmaster.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
}

headers = {
            'authority': 'availability.ticketmaster.se',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            # 'cookie': 'eps_sid=1520f434290f7a5e5c0e9decb8ccc7d524af2664; reese84=3:SuVATT8NTiz5dDf66HNHzA==:gKdTyQ5UsgqOeKNFHTU4z5vtaJoC7EPulMJW7Hx0S6PoPz6qUAI3qwUnv4/RTQ001EbO/QohTe9RTFz4Zgfgc03kn0Pm7sfo9uIl3/HuYRN7d7YkJPxJLMSmkz552nsCEHm74wVQKpH5XHtsdtJg9dsFgU/5bz1Vo0a78CTp/2kZHj0tqjr6vgTwQ00/2PmGYtK3GF+piOzF3kVjp9ybwehsUEjRf36xTyidnko4ZA3QAdO3Z4elCW03z4Elum1TCjEFaBD9YfooAN9gisEcx6bEEgqqqEBmHMKVL8u41AL7oGcH4uvLzN8h53XZ3be7BLuhRzmDfBtSdMWKG09THWPBznyzG+CHgSwjutb0nuDSRpWNjcvJZNRqUCdmffjcxz5/UtYa6anXcwH4wOKEy7PfhM70Kx5/tAEZxSD1ad8X1ehPAlVAaBp11klYAAzm37Bs+vyBljPampLwCAotJA==:CUDC6XLXCQiH5uugI3Z2d4p7ttEG+MZ5kjJub+NGqVo=; language=sv-se; NDMA=612; TMUO=west_rplSrC/KrnlCFZNjY5TyjjPVrQy+BsLBSwYRTinYRcY=; LANGUAGE=sv-se; SID=rzdZ8GwX5zQk497PYUpO62EjrCUkoTOc8f5-ZHRL4msxJn0kFytM7PSQEFQ1lashV_PoNXFrMh-iw1vHXamE; BID=FKkL3xW7LC24k5yTlFsZ6i3LPySA3Vyhp2YL4cVzHFqu5joLwEqpj7VKOdkgzqAKgekk3fozygwc5Hc; OptanonAlertBoxClosed=2023-12-04T13:52:26.017Z; eupubconsent-v2=CP2P9uQP2P9uQAcABBENAdEsAP_gAAAAACiQg1NX_H__bX9r8Xr3aft0eY1P99j77uQxBhfJk-4FyLvW_JwX32EyNA26tqYKmRIEu3ZBIQFlHJHURVigaogVryHsYkGchTNKJ6BkgFMRI2dYCF5vmYtj-QKY58ouM3f5mDeAAAIAEAAAAAAAAAQAAAAAAAAAAAAAAAAADRKb-5IO9-78v4v09l_rk2_eTVn_pcvr7B-uft87_XU-9_fAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAB4IAWAAkAP4AwQCKAFpANEAdUBGICqwFXgK7CAMgAAgAGAATAA4ADwAMgAsACOAFAAK4AWwA_gCLAEuAL6AagBqwDnAOsAeQA-QCBgEHAIoARwAmgBP4ChgKKAXYAvgBnADRAG8AOqAegA-QCG4EXgRiAj0BIoCSwErAJlgTYBNoClwFXgK7AWFAsQCxQF1ALuAXkAwIJAwAAQAAuACgAKgAcAA8ACAAGEAMgA1AB4AEQAJgAVQA3gB6AEJAIYAiQBHACWAE0AKUAYYAywBsgDvgHsAfEA-wD9AIBARcBGACNAEpAKCAVAAq4BcwDFAG0ANwAcQBIgCdgFDgKPAUiApsBbAC5AF3gLzDASwAAgAGAASAA4ACgAIoATgBYADCAHgAewBCAEQAI4ATAAqABXgC2ALgAb4A5gDwAH8AQwAiQBFgCXAFIAK0AakA2QDgAHGAOcAeQA_ACAAEUAIwASYAnQBRQClwFeAV8AuwBfAC_AGcANkAbYA3gBxwDmwHUAdUA7IB6gD5AH7AQkAhsBFUCLwIxAR1AkQCRQElwJaAl4BNgCdgFCAKJgUiBSQCmwFVgKvgWIBYoC0QFyALoAXcAwIBjIgCYAAEAAwACQAHAAUABFACcALAAYQA8AD2AIQAiABHACYAFcALYAb4A5gDuAH8AQwAiQBFgCXAFIAK0AakA2QDgAHGAOcAeQA-QB-AEAAIoARgAkwBOgCigFLgK8Ar4BdgC-AF-AM4AaIA1ABtgDeAHHAOaAdUA7IB6gD5AH7AQkAhuBF4EYgI7gSIBIoCS4EtAS8AmwBOwChAFEgKSAU2AqsBV4Cu4FiAWKAtEBcgC6AF3AMCAYyKAPgAJABFACoALAAhABMAC4AHgARwApABqADgAI4AUWArwCvgF2AL4AX4AzgBvADmgHVAP2Aj0BIoCXgE2AKvgWIBYoC0QFsALuGAHAAEgAigBUAFgAQgAmACOAFIANQAcABHACiwFeAV8AuwBfAC_AGcAN4Ac0A6oB-wEegJeATYAq8BYgC0QFsALuHASYADAATAA4ADwALgAZABYADmAHwAfgBHACaAFAAK4AWwAugBfADQAH8AQgAiwBHACXAFIALIAXwAwgBqQDnAOsAdwA8gB8wEAAQOAg4CEAERAIoARwAnEBPgE_AKKAUsAqABWQC7QF6AXwAzgBogDeAHHAOkAdUA9AB8gENgIiARUAj0BIoCSwErQJiAmWBNgE2gKQAUmApcBVQCrAFXgK7AWIAsoBbMC6ALqAXcAvoBgQ6BqAAuACgAKgAcABAAC6AGAAagA8ACIAEwAKoAXAAxABmADeAHqAQwBEgCWAE0AKMAUoAwwBlADRAGyAO8Ae0A-wD9AH_ARYBGACUgFBAKuAWIAuYBeQDFAG0ANwAcQA6gCLwEiAJUATsAocBR8CmgKbAWKAtgBcgC7QF3gLzIAI4AEAASABkAFgATQAvgBoAD-AKQAWQAvgBqADnAIoARwAnABPoChgKKAUsArIBYgC0gF2AL4AbwA5oB1QD0AI9gTYBNoCkwFiALZAXcAvIBgRCAyAAsACgALgAYgBMACqAFwAMQAbwA9ACOAHeAP8AlIBQQCrgFzAMUAbQA6gCVAFNALFAWiAuQkAwAAMAAkABwAFwAMgAsAByAEcAJoAVAAvgBkADaAG8APAAhABSACygGoAaoA6wB3AEAAIoARwAn0BTQFQAKyAWkAuwBogDeAHVAPkAioBGICOgEegJFASsAlqBNgE2gKTAVSAqsBXYCxAFlALuJQGgAEAALAAoAByAGAAYgA8ACIAEwAKoAXAAxQCGAIkARwAowBsgDvAH4AVcAxQB1AEXgJEAUeAsUBbAC8ygDkABIAFwAMgAsAByAEcAJoAVAAvgBkADaAG8APAAhABFgCOAEyAKQAWQAvgBhQDUANUAc4A7oB8gH2AQAAigBHACRAE-AKGAUuArICtgFigLqAuwBogDXgG8AOqAdsA9AB_wEdAI9ASKAksBMUCbAJtAUgAp8BXYCxAF0ALuAXkAvoBgRSBQAAuACgAKgAcABBADAANQAeABEACYAFIAKoAYgAzQCGAIkAUYApQBlADRAGyAO-AfgB-gEWAIwASkAoIBVwC5gF5AMUAbQA3ACLwEiAJ2AUPApoCmwFigLYAXIAu0BeY.f_wAAAAAAAAA; _gcl_au=1.1.1914691768.1701697946; permutive-id=6b222629-1a1d-48d5-a25d-c3d98d3642e4; _ga=GA1.2.416277617.1701697946; _gid=GA1.2.1113942339.1701697946; _scid=5a94f2e1-a5be-4597-96ae-fe3f016c8a0a; mt.v=2.72000056.1701697946371; mt.pc=2.1; mt.g.45f235f0=2.72000056.1701697946371; __gads=ID=f2e6f4ab2dea5031:T=1701697946:RT=1701697946:S=ALNI_Maw3juC0ROv4_oNscxLval2sfZubA; __gpi=UID=00000ca4cb33e669:T=1701697946:RT=1701697946:S=ALNI_MZnD-oV0qWFiNd4ArWATxaUksXryA; _scid_r=5a94f2e1-a5be-4597-96ae-fe3f016c8a0a; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Dec+04+2023+19%3A22%3A31+GMT%2B0530+(India+Standard+Time)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=397958d6-59b1-4d5d-b05d-c392deda4db9&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CV2STACK42%3A1&geolocation=IN%3BDL&AwaitingReconsent=false; _sc_cspv=https%3A%2F%2Ftr.snapchat.com%2Fp',
            'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        }


from undetected_chromedriver import Chrome, ChromeOptions
class Options(ChromeOptions):
    def _init_(self, *args, **kwargs) -> None:
        super()._init_(*args, **kwargs)
        self.headless: bool = False

country_code = 'se'
capital_country_code = 'SE'



def main_api_list_urls():
    count = 34
    retry = Retry(connect=3, backoff_factor=0.5)
    while count<=35:
        response = session.get(
            f'https://app.ticketmaster.com/discovery/v2/events?apikey=SMvvvra68oURBjOqSaikLG147bUDvaoO&locale=*&page={count}&countryCode=SE')
        print('Response----->>',response,'url------->',response.url)
        print('main_link---------------------------->>>>>>>>',count)
        if response.status_code == 400:
            print(response.text)
            break
        count += 1
        js = response.json()
        list1 = []
        driver = get_chromedriver()
        driver.get("https://www.ticketmaster.se")
        check_queue_it(driver)
        time.sleep(5)
        try:
            accept_cookie = WebDriverWait(driver,30).until(
                                    ec.presence_of_element_located((By.XPATH,'//button[@id="onetrust-accept-btn-handler"]')))
            accept_cookie.click()
        except:
            pass
        check_queue_it(driver)
        time.sleep(3)
        
        
        count1 = 1
        for i in js['_embedded']['events']:
            event_urls = i.get('url')
            print('event_url------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>',count1)
            count1+=1
            event_id = str(event_urls.split("/")[-1])
            driver.get(event_urls)
            check_queue_it(driver)
        
            time.sleep(5)
            cookiess = driver.get_cookies()
            row = {}
            for cookie in cookiess:
                coo = cookie.get('name')
                val = cookie.get('value')
                raw = {coo:val}
                row.update(raw)
            print('-------------------------------------------',row)
        
            cookies = row
            category_name(cookies,event_urls,event_id)
            time.sleep(20)
            driver.refresh()

def check_queue_it(driver):
    check_queue = False
    while check_queue == False:
        window_title = driver.title
        if window_title == "Pardon Our Interruption" or window_title == "Queue-it" or window_title == "Your Session Has Been Suspended" or "ticketmaster.se/event" in window_title:
            print(window_title)
            time.sleep(15)
        else:
            check_queue = True

def get_chromedriver():
    proxy_user = "zcanqxgl"
    proxy_password ="i5zo8eun18d5"
    endpoint = "104.250.204.153:6244"
    seleniumwire_options = {
            "proxy": {
                "http": f"http://{proxy_user}:{proxy_password}@{endpoint}",
                "https": f"http://{proxy_user}:{proxy_password}@{endpoint}",
            }
        }
    try:
        driver = uc.Chrome(options=Options())#, seleniumwire_options=seleniumwire_options)
    except:
        driver = uc.Chrome(options=Options())#, seleniumwire_options=seleniumwire_options)
    driver.set_window_size(500,800)
    return driver


    

def category_name(cookies,event_urls,event_id):
    scrap_done = False
    while scrap_done == False:
        try:
            response = requests.get(f'https://availability.ticketmaster.{country_code}/api/v2/TM_{capital_country_code}/manifest/{event_id}',
                            cookies=cookies, 
                            headers=headers
                            )
        

            print('response-check--->>', response)
            if response.status_code == 200:
                logger.info(f'Response-check---> {response}')
                section_details = {}
                for i in response.json().keys():
                    sections = response.json()[str(i)]
                    for j in sections:
                        name = j.get('name')
                        code = j.get('code')
                        section_details.update({code:name})
                print(section_details)
                scrap_done = detail_page(cookies,event_urls,event_id,section_details)
                # scrap_done = True
                if scrap_done == None:
                    break
            else:
                print('Response---',response)
                scrap_done = True

            time.sleep(0.5)
        except:
            pass



def detail_page(cookies,event_urls,event_id,section_details):
    # params = {
    # '_ga': '2.175788005.634592536.1700571350-984551424.1700571350',
    # }
    response =session.get(
        event_urls,
        cookies=cookies,
        headers=headers,
        # params=params
    )
    logger.info(f'Response--check----{response}-----{response.url}')
    # print(response.text)
    soup = BS(response.text,'html.parser')

    # event_url = response.url

    if response.status_code == 200:
        try:
            event_name = soup.find('div','sc-1cef9ru-0 jXNmSo').find('h1').text
        except:
            event_name = soup.find('div','eventcard').find('h1').text

        try:
            event_vanue = soup.find('div','sc-1cef9ru-5 WZQIZ').find('p','sc-1cef9ru-3 juupaa').text
        except:
            event_vanue = soup.find('div','eventcard').find('div','eventcard__body__venue').text
        
        try:
            event_date = soup.find('div','sc-1cef9ru-0 jXNmSo').find('span').text
        except:
            event_date = soup.find('div','eventcard').find('div','datebox').text.strip().replace("\n","/")

        try:
            price = re.findall('"ticketPriceComponents"(.*?)]',response.text)[0].replace(":[","").replace('"','')
        except:
            try:
                price = re.search('"priceRange":(.*?)"chargeRange":',response.text).group(1)
            except:
                price = re.search('priceCategories":(.*?)"areaNames',response.text).group(1)
            pass
        try:
            tax_fee = float(price.split(",")[1].split[0].strip().replace('"',''))
        except:
            try:
                tax_fee = float(price.split(",")[1].split(" ")[0])
            except:
                try:
                    tax_fee = float(re.findall('priceRange":"(.*?)",',price)[0].split("-")[0])
                except:
                    tax_fee = 0
        try:
            lower_price = float(price.split(",")[0].split("-")[0].strip())+tax_fee
        except:
            try:
                lower_price = float(price.split(",")[0].split(" ")[0])+tax_fee
            except:
                try:
                    lower_price = float(price.split()[0].strip().replace('"','').split("-")[0])
                except:
                    try:
                        lower_price = float(re.findall('priceRange":"(.*?)",',price)[0].split("-")[1].split(" ")[0])+tax_fee
                    except:
                        lower_price = float(price.split("-")[0])
        try:
            higher_price = float(price.split(",")[0].split("-")[1].strip().split(" ")[0])+float(price.split(",")[1].split("-")[1].strip().split(" ")[0])
        except:
            try:
                higher_price = float(re.findall('priceRange":"(.*?)",',price)[-1].split("-")[1].split(" ")[0])+float(re.findall('priceRange":"(.*?)",',price)[-1].split("-")[0])
            except:
                try:
                    higher_price =  float(price.split()[0])
                except:
                    try:
                        higher_price = float(price.split()[0].replace('"',''))
                    except:
                        try:
                            higher_price = float(price.split("-")[1].strip().split(" ")[0])
                        except:
                            higher_price = float(price.split(",")[0].split()[0])+float(price.split(",")[1].split()[0])
        try:
            currency = price.split(",")[0].split("-")[1].strip().split(".00")[1].strip()
        except:
            try:
                currency = price.split(",")[0].split("-")[-1].split()[1]
            except:
                try:
                    currency = price.split()[-1].strip().replace('"','').replace(',','')
                except:
                    try:
                        currency = price.split(" ")[1]
                    except: 
                        currency = re.findall('priceRange":"(.*?)",',price)[0].split("-")[1].split(" ")[1]

        seet_search(cookies,event_urls,event_id,section_details,event_name,event_vanue,event_date,price,lower_price,higher_price,currency)
        return True
    else:
        return

def seet_search(cookies,event_urls,event_id,section_details,event_name,event_vanue,event_date,price,lower_price,higher_price,currency):
    #     params = {
    #     'subChannelId': '1',  
    # }
        response = session.get(
            f'https://availability.ticketmaster.{country_code}/api/v2/TM_{capital_country_code}/availability/{event_id}',
            # params=params,
            cookies=cookies,
            headers=headers,
        )
        logger.info(f'Response--check----{response}')
        js = response.json()
        l = []
        section_keys = []
        site_name = 'ticketmaster.se'
        print("dicts--->",section_details)
        # try:
        for num in js['groups']:
            try:
                for j in num['places']:
                    if j.startswith ("-"):
                        keys = j.split("-")[-1]
                    else:
                        try:
                            keys = j.split("-")[0]
                        except:
                            try:
                                keys = j.split("-")[1]
                            except:
                                keys = j
                    print("keys-name____",keys)
                    try:
                        key = j.split("-")[1] 
                    except:
                        key = ''
                    seat_lenght = []
                    for k in num['places'][str(j)]:
                        for n in num['places'][str(j)][str(k)]:
                            seat_lenght.append(n)
                    availabe_sheet = len(seat_lenght)
                    try:
                        data = section_details.get(keys)+" "+section_details.get(key)
                    except:
                        data = ''
                    # print('Name:-- ',data,' Sheets:-- ',availabe_sheet)
            
                    print('Event_name',event_name)
                    print('Event_date--->',event_date)
                    print('Event_Venue--->',event_vanue)
                    print('category_name---',data,'price:- ',lower_price,'-',higher_price,currency)
                    print('Availabe_sheets--->',availabe_sheet)
                    print('Website_name--->',site_name)
                    print('Event_url---->>',event_urls)

            
                    # now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    # sql_query = "INSERT INTO  lightercreditco_db.scrap_data_ticketmaster (site_name, event_name, league_name, event_date, event_venue,event_schedule,category_name,category_minimum_price,category_maximum_price,currency,available_quantity,event_url,desciption, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,now(),now())"
                    # values = (site_name,event_name, '',event_date,event_vanue, '', data,lower_price, higher_price, currency,availabe_sheet, event_urls, "" )
                    # cursor_conn.execute(sql_query,values)
                    # connection_to_db.commit()
            except Exception as e:
                print('eeeerrrorrr--->',e)

def main():
    main_api_list_urls()
main()

# update_query = "UPDATE lightercreditco_db.scraper_status SET status=1 where scraper_name = 'ticketmaster.se'"
# cursor_conn.execute(update_query)
# connection_to_db.commit()
# cursor_conn.close()




















# import requests
# import logging
# from loguru import logger
# import re
# from time import sleep
# from random import randint
# import threading
# from concurrent.futures import ThreadPoolExecutor
# # import httpx
# from selenium import webdriver
# import time
# # from selenium.webdriver.chrome.options import Options
# import seleniumwire.undetected_chromedriver as uc
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.ui import WebDriverWait
# import socket
# from bs4 import BeautifulSoup as BS
# import json
# import mysql.connector
# import datetime
# # from connection1 import DB_conn
# # EventId = 3285
# price_class_id = 4261
# bold_red = "\x1b[31;1m"
# yellow = "\x1b[33;20m"
# red = "\x1b[31;20m"
# reset = "\x1b[0m"
# format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
# logging.CRITICAL: bold_red + format + reset
# logging.WARNING: yellow + format + reset
# logging.DEBUG: red + format + reset

# # connection_to_db = mysql.connector.connect( host = 'localhost',
# #                                                 port = '3306',
# #                                                 database = 'lightercreditco_db',
# #                                                 user = 'root',
# #                                                 password = 'admin',
# #                                                 )

# # cursor_conn = connection_to_db.cursor()
# connection_to_db = mysql.connector.connect( host = '69.16.249.74',
#                                                 port = '3306',
#                                                 database = 'lightercreditco_db',
#                                                 user = 'lightercreditco_workbench',
#                                                 password = 'XLJ4Q)NVR{GP',
#                                                 ssl_disabled = True
#                                                 )
                                                

# cursor_conn = connection_to_db.cursor()

# cookies = {
#     'eps_sid': 'ef9fdfbf2f9e954e24ef31157d3054449569272d',
#     '_pxvid': '92611744-9d7e-11ee-9620-4c39d692e7c0',
#     'reese84': '3:k8qUKVTqlkklfqQ8bbeAlQ==:A+SSXsj72in5HarcXbnTRnPtIcbFJFJc1T/fHfRhQIYxHe0m6hcvVBbTrRpkzFUE0BmhxarW3+q/vIfuc//ZG3EnU+F5KCIiBEMKBPSScX96msUlT6sHZSkrp61urRMjZ7ss6DAzslNOJH0KpK97uc0lAxCXMKqi5zCxKVHJwqdB76DEoNpUpHNmhpF444MdiDO8LTbLZND/xIhg2TUXS6ziP0qCYU3cJgidDLcH6EQRXACvehUPnYLPIt1VTbQIeam25799FOS3amhhzUCv5ww84ezegl9QmE8P9DWvLhuLTqE/XeL4y9tFT7GFiC6mBCQkvrMVOONPrZrpgwjICmS0LRhDJo23DX2VnhyGymrrdyYS5Dt8qEao4EGgTygfZit4/MCiv3exHYXJOqmUP/GEBeJcOEf/nhUt1aagqYLlG97xYrKjffqb7QsWfazn3eBU5GPmgKbmKRWWafNycII/CwLAyVYOu61jrHizPwW/fusdOUjvIq4Nb5OgZIO/2gXtLGPWWc3MVW14kj4D3g==:19/IvDhkuyWRQIsIGfUUDsqvhuEcRPmTNqL2KtYlHnw=',
#     'language': 'sv-se',
#     'OptanonConsent': 'isGpcEnabled=0&datestamp=Wed+Jan+10+2024+11%3A18%3A52+GMT%2B0530+(India+Standard+Time)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=60b104da-7df3-4c74-b9c4-2b552841680a&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CV2STACK42%3A1&geolocation=MD%3BCU&AwaitingReconsent=false',
#     'BID': 'eda8b962defe4167a89f5d7d',
#     'OptanonAlertBoxClosed': '2023-12-18T08:23:04.622Z',
#     'eupubconsent-v2': 'CP2-G2QP2-G2QAcABBENAfEsAP_gAAAAACiQg1NX_H__bX9r8Xr3aft0eY1P99j77sQxBhfJk-4FyLvW_JwX32EyNA26tqYKmRIEu3ZBIQFlHJHURVigaogVryHsYkGcgTNKJ6BkgFMRM2dYCF5vmYtj-QKY58osM3f5mDeAAAIAEAAAAAAAAAQAAAAAAAAAAAAAAAAADRKb-5IOd_78v4v09F_rk2_eTVn_pcvr7B-uft87_XU-9_feAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAB4IAYAAkAP4AwQCKAFpANEAdUBGICZgFVgKvAV2EAZAABAAMAAmABwAHgAZABYAEcAKAAVwAtgB_AEWAJcAX0A1ADVgHOAdYA8gB8gEDAIOARQAjgBNACfwFDAUUAuwBfADOAGiAN4AdUA9AB8gENwIvAjEBHoCRQElgJWgTKBM0CbAJtAUuAq8BXYCwoFiAWKAuoBdwC8gGBBIF4ACAAFwAUABUADgAHgAQAAwgBkAGoAPAAiABMACqAG8APQAhIBDAESAI4ASwAmgBhgDLAGyAO-AewB8QD7AP0AgEBFwEYAI0ASkAoIBUACrgFzAMUAbQA3ABxAEiAJ2AUOAo8BSICmwFsALkAXeAvMMBMAACAAYABIADgAKAAigBOAFgAMIAeAB7AEIARAAjgBMACoAFeALYAuABvgDmAPAAfwBDACJAEWAJcAUgArQBqQDZAOAAcYA5wB5AD8AIAARQAjABJgCdAFFAKXAV4BXwC7AF8AL8AZwA2QBtgDeAHHAObAdQB1QDsgHqAPkAfsBCQCGwEVQIvAjEBHUCRAJFASXAloCXgEzAJsATsAoQBRMCkQKSAU2AqsBV8CxALFAWiAuQBdAC7gGBAMZEATQAAgAGAASAA4ACgAIoATgBYADCAHgAewBCAEQAI4ATAArgBbADfAHMAdwA_gCGAESAIsAS4ApABWgDUgGyAcAA4wBzgDyAHyAPwAgABFACMAEmAJ0AUUApcBXgFfALsAXwAvwBnADRAGoANsAbwA44BzQDqgHZAPUAfIA_YCEgENwIvAjEBHcCRAJFASXAloCXgEzAJsATsAoQBRICkgFNgKrAVeAruBYgFigLRAXIAugBdwDAgGMigEAACQARQAqACwAIQATAAuAB4AEcAKQAagA4ACOAFFgK8Ar4BdgC-AF-AM4AbwA5oB1QD9gI9ASKAl4BMwCbAFXwLEAsUBaIC2AF3DADoACQARQAqACwAIQATABHACkAGoAOAAjgBRYCvAK-AXYAvgBfgDOAG8AOaAdUA_YCPQEvAJmATYAq8BYgC0QFsALuHASYADAATAA4ADwALgAZABYADmAHwAfgBHACaAFAAK4AWwAugBfADQAH8AQgAiwBHACXAFIALIAXwAwgBqQDnAOsAdwA8gB8wEAAQOAg4CEAERAIoARwAnEBPgE_AKKAUsAqABWQC7QF6AXwAzgBogDeAHHAOkAdUA9AB8gENgIiARUAj0BIoCSwErQJiAmaBNgE2gKQAUmApcBVQCrAFXgK7AWIAsoBbMC6ALqAXcAvoBgQ6BoAAuACgAKgAcABAAC6AGAAagA8ACIAEwAKoAXAAxABmADeAHqAQwBEgCWAE0AKMAYYAygBogDZAHeAPaAfYB-gD_gIsAjABKQCggFXALEAXMAvIBigDaAG4AOIAdQBF4CRAEqAJ2AUOAo-BTQFNgLFAWwAuQBdoC7wF5kAEcACAAJAAyACwAJoAXwA0AB_AFIALIAXwA1ABzgEUAI4ATgAn0BQwFFAKWAVkAsQBaQC7AF8AN4Ac0A6oB6AEegJmgTYBNoCkwFiALuAXkAwIhAZAAWABQAFwAMQAmABVAC4AGIAN4AegBHADvAH-ASkAoIBVwC5gGKANoAdQBKgCmgFigLRAXISAYgAGAASAA4AC4AGQAWAA5ACOAE0AKgAXwAyABtADeAHgAQgApABZQDUANUAdYA7gCAAEUAI4AT6ApoCoAFZALSAXYA0QBvADqgHyARUAjEBHQCPQEigJWAS0AmaBNgE2gKTAVSAqsBXYCxAFlALuJQGgAEAALAAoAByAGAAYgA8ACIAEwAKoAXAAxQCGAIkARwAowBsgDvAH4AVcAxQB1AEXgJEAUeAsUBbAC8ygDoABIAFwAMgAsAByAEcAJoAVAAvgBkADaAG8APAAhABFgCOAEyAKQAWQAvgBhQDUANUAc4A7oB8gH2AQAAigBHACRAE-AKGAUuArICtgFigLqAuwBogDXgG8AOqAdsA9AB_wEdAI9ASKAksBMQCZoE2ATaApABT4CuwFiALoAXcAvIBfQDAikCcABcAFAAVAA4ACCAGAAagA8ACIAEwAKQAVQAxABmgEMARIAowBlADRAGyAO-AfgB-gEWAIwASkAoIBVwC5gF5AMUAbQA3ACLwEiAJ2AUPApoCmwFigLYAXIAu0BeYAA.f_wAAAAAAAAA',
#     '_gcl_au': '1.1.1078440443.1702887785',
#     'permutive-id': 'a6b34f8c-5da4-48e1-aed0-a083a8d13816',
#     '_ga_LF0VMHMZB9': 'GS1.1.1704865732.3.0.1704865732.60.0.0',
#     '_ga': 'GA1.2.54074150.1702887785',
#     '_pnvl_fqf2nqQu': 'false',
#     'pushly.user_puuid_fqf2nqQu': 'mb8toTvGoNzqwxHRpRzNLhKPYBtN0AZR',
#     '_pnss_fqf2nqQu': 'none',
#     'mt.v': '2.1630451120.1702887787230',
#     'LANGUAGE': 'sv-se',
#     '__gads': 'ID=4531e4ddcc853423:T=1703069543:RT=1703069543:S=ALNI_MY8XrH1bALx49jY4xXncGj7khz1KQ',
#     '__gpi': 'UID=00000d23f23c62a9:T=1703069543:RT=1703069543:S=ALNI_MaaMzFXAoDEdbLSa2Q18l8s6WwxtA',
#     '_ga_YZ2D5CYJJ4': 'GS1.1.1704785249.4.1.1704785453.0.0.0',
#     '_ga_0YTBRC3P3B': 'GS1.1.1704785249.4.1.1704785453.60.0.0',
#     '_gid': 'GA1.2.1086892689.1704691059',
#     'pxcts': 'd3fd4c23-af7b-11ee-a1b0-aa41b2734a5d',
#     'NDMA': '612',
#     'ORIGIN_647841': '#{1}#',
#     'SID': 'f96f9262efae4186a5eba66f',
#     'session': '1',
#     'referrer': '',
#     'mt.pc': '2.2',
#     'ORIGIN_647107': '#{1}#',
#     '_gat_gtag_UA_9007471_1': '1',
#     '_gat_gtag_UA_141060251_4': '1',
# }

# par = '2.175788005.634592536.1700571350-984551424.1700571350'
# params = {
#         '_ga': f'{par}',
#     }


# class TicketMaster():
#     def __init__(self) -> None:
#         self.country_code = 'se'
#         self.capital_country_code = 'SE'
#         self.event_id = "647107"
#         self.headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
#             'Accept': '*/*',
#             'Accept-Language': 'en-US,en;q=0.5',
#             # 'Accept-Encoding': 'gzip, deflate, br',
#             'Referer': 'https://www.ticketmaster.be/',
#             'Origin': 'https://www.ticketmaster.be',
#             'Connection': 'keep-alive',
#             # 'Cookie': 'eps_sid=68345b555d7f2557bbb48ef37518e7a6c6a77fda; reese84=3:wRcgwsGD5kVqDVxcNIVkZw==:M+Qltd7hB2Og4/2yGdiv/pUpS+ErBVKIc6Cq0fdvu4xhhiSRQkPZyi5mzCaJjTXbrcz6zPqN4i4fv4y10Y9IFJm7U2kGahlVWM78Q0/VEq3NqN2hs0HOFHZU4NQfKcMxL6l18LEKo+qtYB4/jgn1XPqMiHNsx1RPOr5kUXndzrKcsKIOIFYOeSsTpKhtWZf64s8u+6Nh9ZQbUuRvh7+lbLZrSbEyQXxSMh9l28bejE8koZx/Ku+YidYfILZo8Nfo2avTFk7/+qnsoe4qgJv+nXWbwGs8oiPw0MgJORC/EAnfT7zKzBqy5owBLfxN9rTL9A4M+Jx2eWKWS9YBLxSIvHMIuJa9HCXw8gc8CGKO6DA/5TFiga5zcuSltM1bWtrrIEyKg2csNqhk2UEyPkX/Q/GOKOvntS8EErStWPwiXjxSjkNwqiw7K5YtzBk2zPxO2rn0Q7bMbVt/Z7Fh8Mm91A==:FfuVI5D0YuN9OyqViePHFGQBIA6kUrpWwkvG4d+7MEI=; language=en-us; NDMA=904; ORIGIN_49799=#{1}#',
#             'Sec-Fetch-Dest': 'empty',
#             'Sec-Fetch-Mode': 'cors',
#             'Sec-Fetch-Site': 'same-site',
#             'Pragma': 'no-cache',
#             'Cache-Control': 'no-cache',
#         }
#         self.name_code = self.category_name()


#     def category_name(self):
#         params = {
#             'subChannelId': '1',
#         }
#         self.response = requests.get(f'https://availability.ticketmaster.{self.country_code}/api/v2/TM_{self.capital_country_code}/manifest/{self.event_id}',
#                         cookies=cookies, 
#                         headers=self.headers,
#                         params=params
#                         )
#         # print('response-check--->>', self.response)
#         logger.info(f'Response-check---> {self.response}')
#         self.section_details = {}
#         for i in self.response.json().keys():
#             sections = self.response.json()[str(i)]
#             for j in sections:
#                 name = j.get('name')
#                 code = j.get('code')
#                 self.section_details.update({code:name})
#         print(self.section_details)
#         return self.section_details

#     def seet_search(self):
#             params = {
#             'subChannelId': '1',
#         }
#             response = requests.get(
#                 f'https://availability.ticketmaster.{self.country_code}/api/v2/TM_{self.capital_country_code}/availability/{self.event_id}',
#                 params=params,
#                 cookies=cookies,
#                 headers=self.headers,
#             )
#             logger.info(f'Response--check----{self.response}')
#             js = response.json()
#             self.l = []
#             self.section_keys = []
#             # try:
#             for num in js['groups']:
#                 try:
#                     for j in num['places']:
#                         try:
#                             self.keys = j.split("-")[0]
#                         except:
#                             self.keys = ''
#                         try:
#                             self.key = j.split("-")[1] 
#                         except:
#                             self.key = ''
#                         self.seat_lenght = []
#                         for k in num['places'][str(j)]:
#                             for n in num['places'][str(j)][str(k)]:
#                                 self.seat_lenght.append(n)
#                         self.availabe_sheet = len(self.seat_lenght)
#                         try:
#                             self.data = self.name_code.get(self.keys)+" "+self.name_code.get(self.key)
#                         except:
#                             self.data = ''
#                         # print('Name:-- ',self.data,' Sheets:-- ',self.availabe_sheet)
                
#                         print('Event_name',self.event_name)
#                         print('Event_date--->',self.event_date)
#                         print('Event_Venue--->',self.event_vanue)
#                         print('category_name---',self.data,'price:- ',self.lower_price,'-',self.higher_price,self.currency)
#                         print('Availabe_sheets--->',self.availabe_sheet)
#                         print('Website_name--->',self.site_name)
#                         print('Event_url---->>',self.event_url)

#                         self.now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#                         self.sql_query = "INSERT INTO  lightercreditco_db.scrap_data_ticketmaster (site_name, event_name, league_name, event_date, event_venue,event_schedule,category_name,category_minimum_price,category_maximum_price,currency,available_quantity,event_url,desciption, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,now(),now())"
#                         self.values = (self.site_name, self.event_name, '', self.event_date, self.event_vanue, '', self.data, self.lower_price, self.higher_price, self.currency, self.availabe_sheet, self.event_url, "" )
#                         cursor_conn.execute(self.sql_query,self.values)
#                         connection_to_db.commit()
#                 except Exception as e:
#                     print('eeeerrrorrr--->',e)
#                     # try:
#                     #     self.place = num['places']
#                     # except:
#                     #     self.place = ''
#                     # for j in self.place:
#                     #     a = num['places'][str(j)]
#                     #     self.sec1 = j.split("-")[0]
#                     #     print('sec1--->',self.sec1)
#                     #     self.sec2 = j.split("-")[1]
#                     #     print('sec2------>',self.sec2)                
#                     #     self.seat_lenght = []
#                     #     for k in a:
#                     #         for n in a[str(k)]:
#                     #             self.seat_lenght.append(n)
#                     #     self.availabe_sheet = len(self.seat_lenght)
#                     #     self.data = self.name_code.get(self.sec1)+" "+self.name_code.get(self.sec2)


#                     #     print('Event_name1',self.event_name)
#                     #     print('Event_date1--->',self.event_date)
#                     #     print('Event_Venue-1-->',self.event_vanue)
#                     #     print('category_name--1-',self.data,'price:- ',self.lower_price,'-',self.higher_price,self.currency)
#                     #     print('Availabe_sheets-1-->',self.availabe_sheet)
#                     #     print('Website_name-1-->',self.site_name)
#                     #     print('Event_url--1-->>',self.event_url)
#                     # self.sql_query = "INSERT INTO  lightercreditco_db.scrap_data_ticketmaster (site_name, event_name, league_name, event_date, event_venue,event_schedule,category_name,category_minimum_price,category_maximum_price,currency,available_quantity,event_url,desciption, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,now(),now())"
#                     # self.values = (self.site_name, self.event_name, '', self.event_date, self.event_vanue, '', self.data, self.lower_price, self.higher_price, self.currency, self.availabe_sheet, self.event_url, "" )
#                     # cursor_conn.execute(self.sql_query,self.values)
#                     # connection_to_db.commit()
#                     # print('error--->',e)
                



#     def detail_page(self):
#         # params = {
#         # '_ga': '2.175788005.634592536.1700571350-984551424.1700571350',
#         # }
#         response = requests.get(
#             f'https://www.ticketmaster.{self.country_code}/event/music-of-the-christmas-night-2023-biljetter/{self.event_id}',
#             cookies=cookies,
#             headers=self.headers,
#             # params=params
#         )
#         logger.info(f'Response--check----{self.response}')
#         # print(response.text)
#         soup = BS(response.text,'html.parser')

#         self.site_name = 'ticketmaster.se'

#         self.event_url = response.url


#         try:
#             self.event_name = soup.find('div','sc-1cef9ru-0 jXNmSo').find('h1').text
#         except:
#             self.event_name = soup.find('div','eventcard').find('h1').text

#         try:
#             self.event_vanue = soup.find('div','sc-1cef9ru-5 WZQIZ').find('p','sc-1cef9ru-3 juupaa').text
#         except:
#             self.event_vanue = soup.find('div','eventcard').find('div','eventcard__body__venue').text
       
#         try:
#             self.event_date = soup.find('div','sc-1cef9ru-0 jXNmSo').find('span').text
#         except:
#             self.event_date = soup.find('div','eventcard').find('div','datebox').text.strip().replace("\n","/")

#         try:
#             self.price = re.findall('"ticketPriceComponents"(.*?)]',response.text)[0].replace(":[","").replace('"','')
#         except:
#             try:
#                 self.price = re.search('"priceRange":(.*?)"chargeRange":',response.text).group(1)
#             except:
#                 self.price = re.search('priceCategories":(.*?)"areaNames',response.text).group(1)
        
#         try:
#             self.tax_fee = float(self.price.split(",")[1].split[0].strip().replace('"',''))
#         except:
#             try:
#                 self.tax_fee = float(self.price.split(",")[1].split(" ")[0])
#             except:
#                 try:
#                     self.tax_fee = float(re.findall('priceRange":"(.*?)",',self.price)[0].split("-")[0])
#                 except:
#                     self.tax_fee = 0
#         try:
#             self.lower_price = float(self.price.split(",")[0].split("-")[0].strip())+self.tax_fee
#         except:
#             try:
#                 self.lower_price = float(self.price.split(",")[0].split(" ")[0])+self.tax_fee
#             except:
#                 try:
#                     self.lower_price = float(self.price.split()[0].strip().replace('"','').split("-")[0])
#                 except:
#                     try:
#                         self.lower_price = float(re.findall('priceRange":"(.*?)",',self.price)[0].split("-")[1].split(" ")[0])+self.tax_fee
#                     except:
#                         self.lower_price = float(self.price.split("-")[0])
#         try:
#             self.higher_price = float(self.price.split(",")[0].split("-")[1].strip().split(" ")[0])+float(self.price.split(",")[1].split("-")[1].strip().split(" ")[0])+self.tax_fee
#         except:
#             try:
#                 self.higher_price = float(re.findall('priceRange":"(.*?)",',self.price)[-1].split("-")[1].split(" ")[0])+float(re.findall('priceRange":"(.*?)",',self.price)[-1].split("-")[0])+self.tax_fee
#             except:
#                 try:
#                     self.higher_price =  float(self.price.split()[0])+self.tax_fee
#                 except:
#                     try:
#                         self.higher_price = float(self.price.split()[0].replace('"',''))+self.tax_fee
#                     except:
#                         try:
#                             self.higher_price = float(self.price.split("-")[1].strip().split(" ")[0])+self.tax_fee
#                         except:
#                             self.higher_price = float(self.price.split(",")[0].split()[0])+float(self.price.split(",")[1].split()[0])+self.tax_fee
#         try:
#             self.currency = self.price.split(",")[0].split("-")[1].strip().split(".00")[1].strip()
#         except:
#             try:
#                 self.currency = self.price.split(",")[0].split("-")[-1].split()[1]
#             except:
#                 try:
#                     self.currency = self.price.split()[-1].strip().replace('"','').replace(',','')
#                 except:
#                     try:
#                         self.currency = self.price.split(" ")[1]
#                     except: 
#                         self.currency = re.findall('priceRange":"(.*?)",',self.price)[0].split("-")[1].split(" ")[1]

# bot = TicketMaster()
# bot.detail_page()
# bot.seet_search()

# update_query = "UPDATE lightercreditco_db.scraper_status SET status=1 where scraper_name = 'ticketmaster.se'"
# cursor_conn.execute(update_query)
# connection_to_db.commit()
# cursor_conn.close()