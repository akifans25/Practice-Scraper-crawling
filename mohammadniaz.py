from requests import session
from bs4 import BeautifulSoup as BS
list1 = []
image1 = []
import pandas
s = session()
s.headers['user-agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0'
url = 'https://www.muhammadniaz.net/'
r = s.get(url)
soup = BS(r.text,'html.parser')

def main_link_url_(url1):
    r = s.get(url1)
    soup = BS(r.text,'html.parser')
    for i in soup.find_all('li'):
        b = i.find('a').get('href')
        if b and b.startswith('https://www.muhammadniaz.net/category/games'):

            # print(b)
            list_page(b)

def list_page(url2):
    r = s.get(url2)
    soup = BS(r.text,'html.parser')
    for j in soup.find_all('h2','post-box-title'):
        c = j.find('a')
        if c:
            c=c.get('href')
            # print(c)
            product_page(c)
    
        
def product_page(url3):
    r = s.get(url3)
    soup = BS(r.text,'html.parser')
    name = soup.find('h1','name post-title entry-title').text
    
    comment = soup.find('span','post-comments').text
    
    views = soup.find('span','post-views').text
    
    for k in soup.find_all('p'):
        image= k.find('img')
        if image:
            image=image.get('data-src')
            image1.append(image)

    Recommended = soup.find('div','pane')
    if Recommended:
        Recommended = Recommended.text.split("=",)
    else:
        Recommended = 'not given'
    data = {
         'title' : name,
         'comments' : comment,
         'seeing' : views,
         'photos' : image1,
         'recomm' : Recommended,

    }
    list1.append(data)
    # print(list1)
    print(r.url)
    

main_link_url_('https://www.muhammadniaz.net/')

df = pandas.DataFrame(list1)
df.to_excel('mohdniaz.xlsx',index=False)