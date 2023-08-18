from requests import session
from bs4 import BeautifulSoup as BS
list1=[] 
s=session()
s.headers['user-agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0'
url='https://www.flipkart.com/clothing-and-accessories/topwear/tshirt/men-tshirt/pr?sid=clo,ash,ank,edy&otracker=categorytree&otracker=nmenu_sub_Men_0_T-Shirts'
r=s.get(url)
soup=BS(r.text,'html.parser')
for i in soup.find_all('div',"_1xHGtK _373qXS"):
    name=i.find('div','_2WkVRV').text
    price=i.find('div',"_3I9_wc").text.strip()
    details=i.find('a',"IRpwTa").text
    offs=i.find('div',"_3Ay6Sb").text
    item=dict()
    item['title']=name
    item['rate']=price
    item['getails']=details
    item['offs']=offs
    list1.append(item)
    print(list1)
    