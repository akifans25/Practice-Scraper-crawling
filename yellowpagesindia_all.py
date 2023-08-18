from requests import session
from bs4 import BeautifulSoup as BS
import pandas
list1=[]
s = session()
s.headers['user-agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0'

    
def crawl_all(url1):
    r=s.get(url1)
    soup=BS(r.text,'html.parser')

    for i in soup.find_all('li'):
        main1= i.find('a','eachHomeCategory')
        if main1 and main1.get('href'):
            print(main1.get('href'))


            crawl_all_1(main1.get('href'))

def crawl_all_1(url2):
    cat_url ='http://yellowpages.in/{}'.format(url2)
    print(cat_url)
    r=s.get(cat_url)

    soup=BS(r.text,'html.parser')
    product=soup.find_all('div','eachPopular')
    for j in product:
        Name=j.find('a',"eachPopularTitle").text.strip()
        Shop=j.find('div','openNow').text.strip()
        Contact=j.find('a','businessContact').text.strip()
        Address=j.find('address','businessArea').text.strip()
        Rating=j.find('div','eachPopularRatingBlock').text.strip()
        item=dict()
        # item['Index'] = count
        item['Title'] = Name
        item['Timing'] = Shop
        item['Phone no'] = Contact
        item['Area'] = Address
        item['Rating'] = Rating
        print(item)



crawl_all("http://yellowpages.in/")

df = pandas.DataFrame(list1)
df.to_excel('yellopages.xlsx',index=False)
