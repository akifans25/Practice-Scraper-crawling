import requests
from requests import session
import pandas
list1 = []
s = session()
import json
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'X-INSTANA-T': '5d8a05ac8a05d908',
    'X-INSTANA-S': '5d8a05ac8a05d908',
    'X-INSTANA-L': '1,correlationType=web;correlationId=5d8a05ac8a05d908',
    'Connection': 'keep-alive',
    'Referer': 'https://pharmeasy.in/health-care/top-products-9297',
    # 'Cookie': 'XPESD=%7B%22session_id%22%3A%22s_w_llXAbzEr63G7g5g9zgWj6_1689160325000%22%2C%22session_id_flag%22%3A%22ct_id%22%2C%22media_source%22%3A%22alz-BFL%22%2C%22campaign%22%3A%22Bajaj%20finance%20limited%22%2C%22referrer%22%3A%22%22%2C%22session_start_time%22%3A%222023-07-12T11%3A12%3A05.379Z%22%7D; _gcl_au=1.1.308787353.1687864167; dtm_token_sc=AAALXsN5D_-vuAA1PPZmAAAAAAE; _ga_J4XE9SW84F=GS1.1.1689159973.3.1.1689162177.60.0.0; _ga=GA1.2.108747394.1687864167; dtm_token=AQEKX8J4Dv6uuQE0PfdnAQBBbQE; WZRK_G=99bc83b400364f4f8bfd58bf28154427; X-Default-City=1; X-Pincode=400001; _cg=4000; NPAB_Var=new; NPAB_XDI=tKTKXVW0ge6Luc4aIFYZR; _gaexp=GAX1.2.krbGK8E4RPqBjqnLe5ik9g.19600.0; XdI=llXAbzEr63G7g5g9zgWj6; _gid=GA1.2.749434471.1689159974; pe_utm_source=alz-BFL; pe_utm_data=%7B%22utm_campaign%22%3A%22Bajaj%20finance%20limited%22%2C%22utm_source%22%3A%22alz-BFL%22%7D; XPESS_v2=s_w_llXAbzEr63G7g5g9zgWj6_1689160325000; HAB_Var=Apothecary; HAB_XDI=Apothecary; WZRK_S_R9Z-WWR-854Z=%7B%22p%22%3A2%2C%22s%22%3A1689162018%2C%22t%22%3A1689162063%7D',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}
s.headers.update(headers)
url = 'https://pharmeasy.in/api/otc/getCategoryProducts?categoryId=9297&page={}'

r=s.get(url)
js = r.json()

page = 1
flag = True
while flag:
        r = s.get(url.format(page))
        js = r.json()
        if js.get('data').get('products'):
            print(js['data']['products'].__len__())
            for i in js['data']['products']:
                name = i.get('name')
                image = i.get('images')
                pics_dam = i.get('damImages')
                manufacturer = i.get('manufacturer')
                data = {
                    'title' : name,
                    'photo': image,
                    'ptoto_dam' : pics_dam,
                    'Manufacturer' : manufacturer, 
                }
                list1.append(data)
            print(list1)
        else:
            flag = False
        page+=1

df = pandas.DataFrame(list1)
df.to_excel('pharmesy.xlsx',index=False)

