from requests import session
from bs4 import BeautifulSoup as BS
s = session()
import pandas
headers = {
         'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0',
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
         'Accept-Language': 'en-US,en;q=0.5',
         # 'Accept-Encoding': 'gzip, deflate, br',
         'Connection': 'keep-alive',
         'Referer': 'https://www.adidas.co.in/',
         'Upgrade-Insecure-Requests': '1',
         'Sec-Fetch-Dest': 'iframe',
         'Sec-Fetch-Mode': 'navigate',
         'Sec-Fetch-Site': 'cross-site',
     }
s.headers.update(headers)
base_url = 'https://www.adidas.co.in{}'
url = 'https://www.adidas.co.in/'
r = s.get(url)
soup = BS(r.text,'html.parser')
list1=[]
list2=[]
whole_data = []

def main_link(url1):
    r = s.get(url1)
    soup = BS(r.text,'html.parser')
    for i in soup.find_all('a','_link_fgjdp_1 _column_link_5dar6_23'):
        b = i.get('href')
        if 'blog' not in b and 'sports_bras_guide' not in b and 'adiclub' not in b and 'collaborations' not in b:
            b = 'https://www.adidas.co.in'+ b
            print(b)
            list1.append(b)
        # list_page(b)
def list_page(url2):
    r = s.get(url2)
    print("_______________________++++++++++++",r.url)
    soup = BS(r.text,'html.parser')
    for j in soup.find_all('a','product-card-content-badges-wrapper___2RWqS'):
        list_page_link ='https://www.adidas.co.in'+j.get('href')
        print(list_page_link)
        list2.append(list_page_link)

        
    next_page = [_next for _next in soup.find_all('a','active gl-cta gl-cta--tertiary') if 'Next' in _next.text.strip()]
    if next_page:
        next_url = base_url.format(next_page[0].get('href'))
        # print(next_url)
        list_page(next_url)

def product_page(url3):
    r = s.get(url3)
    soup = BS(r.text,'html.parser')
    for i in soup.find_all('div','content-wrapper___3TFwT'):
        try:
            name = i.find('h1','name___120FN')
            if name:
                name = name.text
            else:
                name = 'not given'
        except:
            name = ""
        color_item = i.find('div','single-color-label___29kFh')
        if color_item:
            color_item = color_item.text
        else:
            color_item = 'not given'
        prize_of_item = i.find('div','gl-price-item notranslate')
        if prize_of_item:
            prize_of_item = prize_of_item.text
        else:
            prize_of_item = 'not given'
       
    all_image_link = []
    for j in soup.find_all('div','content___3m-ue'):
        image_link = j.find('img').get('src')
        if image_link and image_link.startswith('https:'):
            # if image_link not in all_image_link:
            all_image_link.append(image_link)
    item = dict()
    item['title'] = name
    item['Colour'] = color_item
    item['Prize'] = prize_of_item
    item['Image'] = all_image_link
    whole_data.append(item)
    print("product_page::--",r.url)
main_link('https://www.adidas.co.in/')
for url in list1[:241]:
    list_page(url)
for list_links_link in list2:
    product_page(list_links_link)

    
df = pandas.DataFrame(whole_data)
df.to_excel('adidas.xlsx',index=False)

