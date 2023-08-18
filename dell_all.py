from requests import session
from bs4 import BeautifulSoup as BS
s = session()
s.headers['user-agent'] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'
base_url = 'https://www.dell.com/en-in/shop{}'
url = 'https://www.dell.com/en-in/shop'
r = s.get(url)
soup = BS(r.text,'html.parser')

def main_category(url1):
    r = s.get(url1)
    soup = BS(r.text,'html.parser')
    for i in soup.find_all('div','category-img-circle col-lg-6 col-md-6 col-sm-6'):
        main_category_link = 'https://www.dell.com'+i.find('a').get('href')
        if main_category_link and not main_category_link.endswith('/deals/deals'):
            # print(main_category_link)
            sub_category(main_category_link)

list1 = []
list2 = []
def sub_category(url2):
    r = s.get(url2)
    # print('r_urls---->',r.url)
    soup = BS(r.text,'html.parser')
    for j in soup.find_all('div','cat-fran-card-img'):
        sub_category_link = j.find('a').get('href')
        if 'https:' not in sub_category_link:
            sub_category_link_2 = 'https:{}'.format(sub_category_link)
        else:
            sub_category_link_2 = sub_category_link
        # print(sub_category_link_2)
        list1.append(sub_category_link_2)

    for l in soup.find_all('div','category__text-area'):
        b = l.find('a').get('href')
        if 'https:' not in b:
            c = 'https:{}'.format(b)
        else:
            c = b
        # print(c)
        
        list1.append(c)

def list_page(url3):
    r = s.get(url3)
    print('sub_cat-------',r.url)
    soup = BS(r.text,'html.parser')
    # list3 = []
    # for k in soup.find_all('h3','ps-title'):
    #     list_page_link = 'https:'+ k.find('a').get('href')

    deals_link = 'https://www.dell.com/en-in/shop/deals/deals'
    # list3.append(deals_link)
    list_page(deals_link)
            # list3.append(list_page_link)
            # list3.append(i)
    # for i in deals_link:
    #     print(i)
            # print(list3)
    product_page(list_page_link)

def product_page(url4):
    r = s.get(url4)
    soup = BS(r.text,'html.parser')
    name = soup.find('h1','mb-md-0 mr-4 d-inline')
    if name:
        name = name.text
    else:
        name = 'not givin'
    # print(name)

    for i in soup.find_all('div','gallery-modal'):
        b = 'https:'+i.find('img').get('src')
        # print(b)
    
    price = soup.find('span','h3 font-weight-bold mb-1 text-nowrap sale-price')
    if price:
        price = price.text
    else:
        price = 'not givin'
    # print(price)

    for i in soup.find_all('div','mb-4 mt-2'):
        b = i.find('a').get('href')
        if 'https:' not in b:
            c = 'https:{}'.format(b)
        else:
            c = b
        # print(c)
    
    processor = soup.find('div','d-flex flex-wrap options')
    if processor:
        processor = processor.text
    else:
        processor = 'not givin'
    # print(processor)

    rating = soup.find('a','rating-container')
    if rating:
        rating = rating.text
    else:
        rating = 'not givin'
    # print(rating)




main_category('https://www.dell.com/en-in/shop')
for url in list1:
    list_page(url)