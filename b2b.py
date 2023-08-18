from requests import session
from bs4 import BeautifulSoup as BS
import pandas
s = session()
headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Authorization': 'Basic cDFob3NwaXRhbGl0eTpzZWNyZXQ=',
        'Connection': 'keep-alive',
        # 'Cookie': 'XSRF-TOKEN=eyJpdiI6IkNHVXU4bzdtclpBWUt3WjI4cFIyZlE9PSIsInZhbHVlIjoiZjdjRG9rdjdWamphWmVoaHd4TzdyZGl1K0tRd29MdGlGSnRld01wWlRkUXA1Z2FMKzFlayttYzQ5eE44SktHSVdlUGFUVkNvQ3VTbUp3SVBJZEp2blhXLzc
#     vZFM5SVJML0pXbGQxU1ZwV0l4L01WdDl2ZGxwY2VEbnpvRnZ5VHciLCJtYWMiOiJmYjEyOWZiNTg2NWQ5ZTMzZGYyZmY4ODQ0MjQ2OTg3NTBiMzZiZmQyODJlMmNhNGU1NjQyYzVkOTdmMDEyZjBmIiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6Ik9IWFZ6ck
#     1lMnYraVhaZmgyYnVTb0E9PSIsInZhbHVlIjoiSkR6cFV0SUVyL3AyTitGNHl1enR1amZEOXVDcXcrKzZNSnBwTGhCN0huakNvWm9KWmdOQmljeFBLY1hwTTQyQ2o2NHBwM0hhMnh2SkNSSHFPOExrTmVvV3hQdVAvMFlodXBieVJ2czNjTFM1SEtZTXhERkRXUktFemlNT
#     ndqZVMiLCJtYWMiOiI2Njc2MGM0ZjA4OTEyMDNhMDJjNzQ0MGM0OTExNjhiNjcyMjZmMmQ3YTQyYTcxYjA3MmVhNjE4NjRlM2VkNGJmIiwidGFnIjoiIn0%3D',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
    }
s.headers.update(headers)
url = 'https://b2b.travelflow.com/p1-corporate-hospitality'
r = s.get(url)
soup = BS(r.text,'html.parser')
list1=[]
def b2b_crawle(url):
    r = s.get(url)
    soup = BS(r.text,'html.parser')
    h=[]
    n=[]
    j=[]
    k=[]
    l=[]
    m=[]
    for i in soup.find_all('div','p-2 events-title-container'):
        category1 = i.find('span').text.replace('\n',"").split(",")[0]
        h.append({'club_name':category1})
        category2 = i.find('span').text.replace('\n',"").split(",")[1]
        n.append({'club_year':category2})
        category3 = i.find('span').text.replace('        ','').split(",")[2]
        j.append({'club_time':category3})
        organizer = i.find('small').text.split("-")[0]
        k.append({'organizer_name':organizer})
        date = i.find('small').text.split("-")[1]
        l.append({'organizer_date':date})
        vanue = i.find('small').text.split("-")[2]
        m.append({'organizer_venue':vanue})
    d=[]
    for i in soup.find_all('tr')[1:]:
         b=i.find_all('td')
         if len(b)==1:
             d.append({"price": ''})
         else:
             d.append({"price": b[1].text.strip()})
    g=[]
    for i in soup.find_all('h5'):
         b= i.text
         g.append(b)
    e=[]
    for i in soup.find_all('tr')[1:]:
         b=i.find_all('td')
         if len(b)==1:
             e.append({"price_hotel": ''})
         else:
             e.append({"price_hotel": b[2].text.strip()})
    f=[]
    for i in soup.find_all('tr')[1:]:
         b=i.find_all('td')
         if len(b)==1:
             f.append({"stoke": ''})
         else:
             f.append({"stoke": b[3].text.strip()})
    item=dict()
    item ['club_name'] = h
    item ['clun_year'] = n
    item ['club_time'] = j
    item ['organizer_name'] = k
    item ['organizer_date'] = l
    item ['organizer_venue'] = m
    item ['price'] = d
    item ['price_pool'] = e
    item ['title'] = g
    item ['stock'] = f
    list1.append(item)
    print(list1)
     


     




b2b_crawle('https://b2b.travelflow.com/p1-corporate-hospitality')

df = pandas.DataFrame(list1)
df.to_excel('b2b.xlsx',index=False)