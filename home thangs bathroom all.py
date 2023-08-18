
from requests import session
from bs4 import BeautifulSoup as BS
s=session()
s.headers['user-agent']="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0"
import pandas
list1=[]

     
def crawl_all_category (url):
    r=s.get(url)
    soup=BS(r.text,'html.parser')
    for i in soup.find_all('div','category-list'):
            sub='https://www.homethangs.com/'+i.find('a').get('href')
            print('main_sub',sub)
            sub_category1(sub)

def sub_category1(url1):
    r=s.get(url1)
    soup=BS(r.text,'html.parser')
    product = soup.find_all('table','categoryitem')
    if product:
         listpage_all.append(url1)


    sub1 = soup.find_all('div','category-list')
    if sub1:
        for i in sub1:
            sub2 = 'https://www.homethangs.com/'+i.find('a').get('href')
            # print('sub2',sub2)
            sub_category1(sub2)
            
def listpage(url2,page):
     r=s.get("{}&page={}".format(url2,page))
     print(r.url)

     soup = BS(r.text,'html.parser')
     product2 = soup.find_all('table','categoryitem')
     for j in product2:
          name = j.find('td','pother')
          if name:
               name=name.text
          else:
               'not ans'
          # print(name)


          price = j.find('b').find('span')
          if price:
               price=price.text
          else:
               'not ans'
          details=j.find('p','h1-link').text
          image=j.find('a').find('img').get('src')
        
          item=dict()
            
          item['Name']=name
          item['features']=details 
          item['image']=image
          item['price']=price

          # print(item)


     page+=1

     if int(soup.find('div','hql-total-page').text.split('1 of ')[1])>=page:
          listpage(url2,page)

listpage_all = []
                 

crawl_all_category("https://www.homethangs.com/bathroom-320.html")

for url in listpage_all:
     listpage(url,page=1)
