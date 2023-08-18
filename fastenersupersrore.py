from requests import session
from bs4 import BeautifulSoup as BS
list1=[]
list2=[]
list3=[]
s=session()
s.headers=['Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0']
url='https://www.fastenersuperstore.com/'
r=s.get(url)
soup=BS (r.text,'html.parser')
for i in soup.find_all('a'):
    b=i.get('href')
    if b and b.startswith('/category'):
         if b not in list1:
            list1.append(b)
            item=dict()
            item['all_links']='https://www.fastenersuperstore.com/'+b
            list2.append(item)
for j in list2:
    c=j.get('all_links')
    r=s.get(c)
    soup=BS(r.text,'html.parser')
    products=soup.find_all('li')
    for num in products:
        if num.find('h2'):
            name=(num.find('h2').text)
        if num.find('span'):
            img=(num.find('img').get('src'))
        if num.find('p'):
            features=(num.find('p').text)
            item=dict()
            item['name']=name
            item['image']=img
            item['features']=features
            list3.append(item)
            print(list3)








