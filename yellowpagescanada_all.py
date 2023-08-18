from requests import session
from bs4 import BeautifulSoup as BS
import pandas
list1=[]
s = session()
s.headers['user-agent'] ='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0'
base_url = 'https://www.yellowpages.ca{}'
url = 'https://www.yellowpages.ca/'

# r = s.get(url)
# soup = BS(r.text,'html.parser')


def main_link(url1):
    r = s.get(url1)
    soup = BS(r.text,'html.parser')
    for i in soup.find_all('a','jsQuickLinks'):
        b = 'https://www.yellowpages.ca'+i.get('href')
        # print(b)
        list_page(b)


def list_page(url2):
    r = s.get(url2)
    print(r.url)
    soup = BS(r.text,'html.parser')
    for j in soup.find_all('a','listing__name--link listing__link jsListingName'):
        list_page_link = 'https://www.yellowpages.ca'+j.get('href')
        if list_page_link:
            list_page_link = list_page_link
        else:
            list_page_link = 'not givin'
        # print(list_page_link)
        product_page(list_page_link)
    next_page = soup.find('div','view_more_section_noScroll')
    next_page = [_next for _next in soup.find_all('a','ypbtn btn-theme pageButton') if 'Next' in _next.text.strip()]

    if next_page:
        next_url = base_url.format(next_page[0].get('href'))
        # print(next_url)
        list_page(next_url)
        product_page(list_page_link)

def product_page(url3):
    r = s.get(url3)
    soup = BS(r.text,'html.parser')
    name = soup.find('span','merchantNamejsShowCTA')
    if name:
        name = name.text
    else:
        name = 'not givin'
    image = 'not given'
    for k in soup.find_all('a','merchant-logo-link'):
        image_ = k.find('img')
        if image:
            image = image_.get('src')
        else:
            image = 'not given'

    
    timing = soup.find('div','merchant__status tooltip__toggle see-hours')
    if timing:
        timing = timing.text.strip().replace('\xa0',"")
    else:
        timing = 'not givin'
    

    mobile = soup.find('li','mlr__submenu__item')
    if mobile:
        mobile = mobile.text
    else:
        mobile = 'not givin'


    rating = soup.find('div','merchant__overall_rating_container merchant__details__rating__content jsStarsContainer jsBusinessDetailsRating')
    if rating:
        rating = rating.text.strip()
    else:
        rating = 'not givin'

    details = soup.find('div','merchant__details__section merchant__details__section--teaser')
    if details:
        details = details.text.strip()
    else:
        details = 'not givin'

    data = {
        'title' : name,
        'photo' : image,
        'opening' : timing,
        'number' : mobile,
        'stars' : rating,
        'summary' : details,
    }
    list1.append(data)
    print(r.url)




main_link(url)

df = pandas.DataFrame(list1)
df.to_excel('canada_all.xlsx',index=False)