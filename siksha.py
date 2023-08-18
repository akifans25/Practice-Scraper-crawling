from requests import session
from bs4 import BeautifulSoup as BS
import pandas
list2 = []
S = session()
S.headers['user-agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0'
url = 'https://www.shiksha.com/'
r = S.get(url)
soup = BS(r.text,'html.parser')
def main_caregory(url):
    r = S.get(url)
    soup = BS(r.text,'html.parser')
    for i in soup.find_all('a',attrs={'ea':'Top Ranked Colleges'}):
         b=i.get('href')
         if 'https' not in b:
             b='https://www.shiksha.com'+b
             list_page(b)
            #  print(b)

def list_page(url2):
    r = S.get(url2)
    soup = BS(r.text,'html.parser')
    for i in soup.find_all('a','rank_clg ripple dark'):
         list_category='https://www.shiksha.com/'+i.get('href')
        #  print(list_category)
         product_page(list_category)


def product_page(url3):
    r = S.get(url3)
    soup = BS(r.text,'html.parser')

    name = soup.find('h1','e70a13').text

    comment = soup.find('a','dc3573')
    if comment:
        comment = comment.text
    else:
        comment = 'not given'

    image = soup.find('div','c55b78')
    if image:
        image = image.find('img').get('src')
    else:
        image = 'not given'


    reviews = soup.find('span','f05f57 ece774 ece774')
    if reviews:
        reviews = reviews.text
    else:
        reviews = 'not given'

    place = soup.find('div','_94eae8')
    if place:
        place = place.text
    else:
        place = 'not given'


    est = soup.find('ul','e1a898')
    if est:
        est = est.text
    else:
        est = 'not given'

    information = soup.find('div','faq__according-wrapper')
    if information:
        information = information.text
    else:
        information = 'not given'
    list1=[]


    for i in soup.find('ul','_4b29'):
        all_info = i.find('a')
        if all_info:
            all_info = all_info.get('href')
            if 'https:' not in all_info:
                all_info = 'https://www.shiksha.com/'+all_info
                # print(all_info)
                list1.append(all_info)
    data = {
        'titel' : name,
        'comments' : comment,
        'images' : image,
        'review' : reviews,
        'place' : place,
        'informations' : information,


        'all_information' : list1
    }
    list2.append(data)     
    print(r.url)






main_caregory('https://www.shiksha.com/')

df = pandas.DataFrame(list2)
df.to_excel('siksha.xlsx',index=False)





