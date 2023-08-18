from requests import session
from bs4 import BeautifulSoup as BS
import pandas
list1=[]
list2=[]
count=1


S=session()
S.headers['user-agent']='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/112.0'
url="http://yellowpages.in/"
r=S.get(url)
soup=BS(r.text,'html.parser')
for i in soup.find_all('a',"eachHomeCategory"):
    b=i.get("href")
    item=dict()
    item ['all link'] = "http://yellowpages.in/"+b
    list1.append(item)
print(list1)
for j in list1:
    c=j.get('all link')
    r=S.get(c)
    soup=BS(r.text,'html.parser')
    product=soup.find_all('div',"eachPopular")
    for num in product:
        Name=num.find('a',"eachPopularTitle").text.strip()
        Shop=num.find('div','openNow').text.strip()
        Contact=num.find('a','businessContact').text.strip()
        Address=num.find('address','businessArea').text.strip()
        Rating=num.find('div','eachPopularRatingBlock').text.strip()
        item=dict()
        item['Index'] = count
        item['Title'] = Name
        item['Timing'] = Shop
        item['Phone no'] = Contact
        item['Area'] = Address
        item['Rating'] = Rating
        list2.append(item)
        count+=1
print(list2)
df = pandas.DataFrame(list2)
df.to_excel('all yellow.xlsx', index=False)