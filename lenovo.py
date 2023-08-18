from requests import session
from bs4 import BeautifulSoup as BS
s = session()
s.headers['user-agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0'
url = 'https://www.lenovo.com/in/en/d/deals?IPromoID=LEN598722&sort=sortBy&resultsLayoutType=grid'
r = s.get(url)
soup = BS(r.text,'html.parser')

def crawl_deals(url):
    r = s.get(url)
    soup = BS(r.text,'html.parser')
    for i in soup.find_all('a','text-capitalize font-weight-bold product__card__learn-more v-btn v-btn--text theme--light v-size--default primary--text'):
         b=i.get('href')
        #  print(b)
        #  product_page(b)
    
def product_page(url2):
     r = s.get(url2)
     soup = BS(r.text,'html.parser')
     for i in soup.find_all('div','backgroundColor subseriesHeader noeSpot'):
          name = i.find('h1','desktopHeader').text
          image = i.find('img','subSeries-Hero rollovercartItemImg').get('src')
          price = i.find('dd',attrs={'itemprop':'price'})
          if price:
               price = price.text
          else:
               price = 'not ans'
        #   print(price)

          details = i.find('div','hero-productDescription-body mediaGallery-productDescription-body').text
          print(details)

          



crawl_deals('https://www.lenovo.com/in/en/d/deals?IPromoID=LEN598722&sort=sortBy&resultsLayoutType=grid')