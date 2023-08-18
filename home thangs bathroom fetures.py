from requests import session
from bs4 import BeautifulSoup as BS
list1=[]
s=session()
s.headers['user-agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0'
url="https://www.homethangs.com/vanities-384.html"
r=s.get(url)
soup=BS(r.text,'html.parser')


def nextcrawl(url,page):
    r=s.get(url)
    soup=BS(r.text,'html.parser')
    products=soup.find_all('table','categoryitem')
    if products:
        for i in soup.find_all('table','categoryitem'):
            price=i.find('b').text.strip()
            details=i.find('p',"h1-link").text
            brand=i.find('td','pother').text
            image=i.find('a').find('img').get('src')
            sales=i.find('img').get('src')
            item=dict()
            item['brand']=brand
            item['price']=price
            item['details']=details
            item['img']=image
            item['sales']=sales
            list1.append(item)
            print(list1)


        page+=1
        next_pages_url = "{}&page={}".format(url,page)
        nextcrawl(next_pages_url,page)
nextcrawl(url,page=1)
    



