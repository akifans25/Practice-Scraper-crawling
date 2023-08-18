from requests import session
from bs4 import BeautifulSoup as BS
import pandas
s = session()
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.bing.com/',
    'Alt-Used': 'www.srx.com.sg',
    'Connection': 'keep-alive',
    # 'Cookie': 'JSESSIONID=02673683AAE41658646D0A02175B5350; _gcl_au=1.1.1821257492.1690801631; _ga_8ZKHWT9KV9=GS1.1.1690801632.1.1.1690801691.1.0.0; _ga=GA1.3.1863254134.1690801632; ajs_anonymous_id=7cc165f1-ded6-47f2-85c0-3b0ef43fee3d; _ga_Z5QMQCJLLJ=GS1.1.1690801632.1.1.1690801691.1.0.0; _ga_GG21BH9GS5=GS1.1.1690801632.1.1.1690801691.1.0.0; _ga_1W2PTZ5R3Q=GS1.1.1690801633.1.1.1690801691.0.0.0; __utma=210509015.1863254134.1690801632.1690801635.1690801635.1; __utmb=210509015.3.9.1690801687218; __utmc=210509015; __utmz=210509015.1690801635.1.1.utmcsr=bing|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; _gid=GA1.3.248806949.1690801635; iconColor=12; _hjSessionUser_3253557=eyJpZCI6IjY3MmRhM2U4LTQ1YTktNWY1ZC1hNmQ1LWM4MGNhZGE4ZmZlZCIsImNyZWF0ZWQiOjE2OTA4MDE2Mzc5NjUsImV4aXN0aW5nIjp0cnVlfQ==; _hjFirstSeen=1; _hjIncludedInSessionSample_3253557=0; _hjSession_3253557=eyJpZCI6ImJkZjEyYWI4LWFmZDItNDQ2Yi1iNGFjLTllY2EzYzQ2ZjI1MCIsImNyZWF0ZWQiOjE2OTA4MDE2Mzc5NjgsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _ga_XW0YWPFYJ7=GS1.3.1690801638.1.1.1690801693.0.0.0; _uetsid=668546902f9211ee8d0bebce8f3c12f9; _uetvid=668545a02f9211eebe3cbf91ff71dce4; _gat_UA-1739236-6=1',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}
s.headers.update(headers)
url = 'https://www.srx.com.sg/'

r = s.get(url)

def  main_category(url1):
    r = s.get(url1)
    soup = BS(r.text,'html.parser')
    for i in soup.find('div',attrs={'id':'homepage-search-property-types'}).find_all('a'):
        main_link_url = 'https://www.srx.com.sg'+i.get('href')
        # print(main_link_url)
        list_page(main_link_url,page=1)
def list_page(url2,page):
    # r = s.get(url2)
    flag = True
    while flag:
        r= s.get('{}?page={}'.format(url2,page))

        # print(r.url)
        soup = BS(r.text,'html.parser')
        for j in soup.find_all('div','col-xs-6 col-6 col-sm-5 col-md-5 listingPhotoMain listingPhotoView'):
            list_page_link = j.find('a').get('href')

        # print(list_page_link)
            product_page(list_page_link)
            page+=1
            if int(soup.find_all('li','hidden-xs')[3].text.strip())>=page:
                list_page(url2,page)
            else:
                flag = False
            page+=1

list1 = []
def product_page(url3):
    r = s.get('https://www.srx.com.sg{}'.format(url3))
    # print(r.url)
    soup = BS(r.text,'html.parser')
    name =  soup.find('h1','listing-name')
    if name:
        name = name.text
    else:
        name = 'not givin'
    # print(name)

    for i in soup.find('div',attrs={'id':'photos-inner'}).find_all('img'):
        image_links = i.get('src')
        # print(image_links)


    price = soup.find('div','listing-price')
    if price:
        price = price.text.strip()
    else:
        price = 'not givin'
    # print(price)


    bads_bath = soup.find('div',attrs={'id':'bed-bath-div'})
    if bads_bath:
        bads_bath = bads_bath.text.split()
    else:
        bads_bath = 'notr givin'
    # print(bads_bath)

    phone_num = soup.find('a','featuredAgentCall')
    if phone_num:
        phone_num = phone_num.get('href')
    else:
        phone_num = 'not givin'
    print(phone_num)
    data = {
        'title' : name,
        'img' : image_links,
        'money' : price,
        'bads_baths' : bads_bath,
        'call' : phone_num,
    }
    list1.append(data)


main_category('https://www.srx.com.sg/')
df = pandas.DataFrame(list1)
df.to_excel('srx._all.xlsx',index=False)