from requests import session
from bs4 import BeautifulSoup as BS
import pandas
s = session()
s.headers['user-agent'] ='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0'
url = 'https://www.rdklu.com/'
base_url = 'https://www.rdklu.com{}'
r = s.get(url)
soup = BS(r.text,'html.parser')
list1 = []

def main_category(url1):
    r = s.get(url1)
    soup = BS(r.text,'html.parser')
    for i in soup.find_all('a','mobile-nav__link mobile-nav__link--top-level'):
        main_category_link = i.get('href')
        if main_category_link and main_category_link.startswith('/collections/mens') or main_category_link.startswith('/collections/womens') or main_category_link.startswith('/collections/tie-and-dye') or main_category_link.startswith('/collections/series') or main_category_link.startswith('/collections/new-arrivals-2') or main_category_link.startswith('/collections/rdklu-smart-jackets'):
            main_category_link = 'https://www.rdklu.com'+main_category_link
            print(main_category_link)
            list_page(main_category_link)


def list_page(url2):
    r = s.get(url2)
    soup = BS(r.text,'html.parser')
    for j in soup.find_all('a','grid-product__link'):
        list_page_link = 'https://www.rdklu.com'+j.get('href')
        print(list_page_link)
        product_page(list_page_link)
    next_page = [_next for _next in soup.find_all('span','next') if 'Next' in _next.text.strip()]
    if next_page:
        next_url = base_url.format(next_page[0].find('a').get('href'))
        print(next_url)
        list_page(next_url)
     

image_link = []
def product_page(url3):
    r = s.get(url3)
    soup = BS(r.text,'html.parser')
    name = soup.find('div','product-block product-block--header')
    if name:
        name = name.text.strip()
    else:
        name = 'not givin'

    price = soup.find('span','product__price on-sale')
    if price:
        price = price.text.strip()
    else:
        price = 'not givin'

    size = soup.find('div','variant-wrapper variant-wrapper--dropdown js')
    if size:
        size = size.text.split()
    else:
        size = 'not givin'

    for i in soup.find_all('div','product__thumb-item'):
        image = i.find('a')
        if image:
            image = image.get('href')
        else:
            image = 'not givin'
        image_link.append(image)

    discription = soup.find('div','rte')
    if discription:
        discription = discription.text.strip()
    else:
        discription = 'not givin'

    data = {
        'title' : name,
        'rate' : price,
        'Size' : size,
        'ptoto' : image_link,
        'dis' : discription,
    }
    list1.append(data)
    print(r.url)    


main_category('https://www.rdklu.com/')

df = pandas.DataFrame(list1)
df.to_excel('rdkul22.xlsx',index=False)







# from requests import session
# from bs4 import BeautifulSoup as BS
# import pandas
# s = session()
# s.headers['user-agent'] ='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0'
# base_url = 'https://www.rdklu.com{}'
# url = 'https://www.rdklu.com/'
# r = s.get(url)
# soup = BS(r.text,'html.parser')
# list1 = []
# def main_category(url1):
#     r = s.get(url1)
#     soup = BS(r.text,'html.parser')
#     for i in soup.find_all('div','grid__item small--one-half medium-up--one-quarter'):
#         main_category_link = 'https://www.rdklu.com'+ i.find('a').get('href')
#         print(main_category_link)
#         listpage_category(main_category_link)

# def listpage_category(url2):
#     r = s.get(url2)
#     print('_________+_____',r.url)
#     soup = BS(r.text,'html.parser')
#     for i in soup.find_all('a','grid-product__link'):
#         listpage_category_link = 'https://www.rdklu.com'+ i.get('href')
#         print(listpage_category_link)
#         product_page(listpage_category_link)

#     next_page = [_next for _next in soup.find_all('span','next') if 'Next' in _next.text.strip()]
#     if next_page:
#         next_url = base_url.format(next_page[0].find('a').get('href'))
#         print(next_url)
#         listpage_category(next_url)
        
# image_link = []
# def product_page(url3):
#     r = s.get(url3)
#     soup = BS(r.text,'html.parser')
#     name = soup.find('div','product-block product-block--header')
#     if name:
#         name = name.text.strip()
#     else:
#         name = 'not givin'

#     price = soup.find('span','product__price on-sale')
#     if price:
#         price = price.text.strip()
#     else:
#         price = 'not givin'

#     size = soup.find('div','variant-wrapper variant-wrapper--dropdown js')
#     if size:
#         size = size.text.split()
#     else:
#         size = 'not givin'

#     for i in soup.find_all('div','product__thumb-item'):
#         image = i.find('a')
#         if image:
#             image = image.get('href')
#         else:
#             image = 'not givin'
#         image_link.append(image)

#     discription = soup.find('div','rte')
#     if discription:
#         discription = discription.text.strip()
#     else:
#         discription = 'not givin'

#     data = {
#         'title' : name,
#         'rate' : price,
#         'Size' : size,
#         'ptoto' : image_link,
#         'dis' : discription,
#     }
#     list1.append(data)
#     print(r.url)    

# main_category('https://www.rdklu.com/')

# df = pandas.DataFrame(list1)
# df.to_excel('rdkul.xlsx',index=False)