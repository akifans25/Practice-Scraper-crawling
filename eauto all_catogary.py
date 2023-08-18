from requests import session
from bs4 import BeautifulSoup as BS
import pandas
s = session()
list1 = []
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',   
    'Referer': 'https://www.google.com/',
    'Alt-Used': 'eauto.co.in',
    'Connection': 'keep-alive',
    # 'Cookie': 'keep_alive=d54fdd1a-fce1-4c9b-b2d6-c65788089a82; secure_customer_sig=; localization=IN; _cmp_a=%7B%22purposes%22%3A%7B%22a%22%3Atrue%2C%22p%22%3Atrue%2C%22m%22%3Atrue%2C%22t%22%3Atrue%7D%2C%22display_banner%22%3Afalse%2C%22merchant_geo%22%3A%22IN%22%2C%22sale_of_data_region%22%3Afalse%7D; _y=8706c450-1329-4a60-948a-ec975486e108; _s=e91c3041-0bfe-47e2-b149-7824d5bb3688; _shopify_y=8706c450-1329-4a60-948a-ec975486e108; _shopify_s=e91c3041-0bfe-47e2-b149-7824d5bb3688; _orig_referrer=https%3A%2F%2Fwww.bing.com%2F; _landing_page=%2F; _gcl_au=1.1.157208665.1688988821; _shopify_sa_t=2023-07-10T12%3A18%3A46.260Z; _shopify_sa_p=; _ga_YBW8RQ2NHL=GS1.1.1688988821.1.1.1688991531.0.0.0; _ga=GA1.1.154980345.1688988822; _ga_5LFGY39ZV1=GS1.1.1688988821.1.1.1688991526.21.0.0; po_visitor=UCLm2TL2ZMKS; _ga_LPSGMH9SYD=GS1.1.1688988822.1.1.1688991526.0.0.0; _gid=GA1.3.632790121.1688988824; _ga_BDQ916D75Z=GS1.3.1688988824.1.1.1688991528.60.0.0; mp_07dbb3be67b77ace43eaed584e41c1a1_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A1893f9b60491d11-05cfcb6efa5b0e8-9762632-1fa400-1893f9b604a1d11%22%2C%22%24device_id%22%3A%20%221893f9b60491d11-05cfcb6efa5b0e8-9762632-1fa400-1893f9b604a1d11%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Feauto.co.in%2Fpages%2Ffaqs-frequently-asked-questions%22%2C%22%24initial_referring_domain%22%3A%20%22eauto.co.in%22%7D; _hjSessionUser_2599484=eyJpZCI6IjlhOGM0ODJmLTZkMTQtNTVlMy04ZTA3LTIxNjRlMmNmZWYzZSIsImNyZWF0ZWQiOjE2ODg5ODkyOTU0MjEsImV4aXN0aW5nIjpmYWxzZX0=; _clck=1j2gq0b|2|fd6|0|1286; _clsk=wuzhm0|1688989299822|1|1|k.clarity.ms/collect; __cf_bm=gFhEnxbHEosiZLGZaQmvikq17L_lGWixqbtatCt3djo-1688991524-0-AZnOIoDNVMrra0MNWYQ7aI32nnaBB8QUtoDiYqO2M9zqICqpjQHS1oP9Yq8ly0gcpvurMllil1853aeFeZV2Q+Y=; _uetsid=9dddca701f1511eeae0d7968f3af4362; _uetvid=9dddf7601f1511eea904176d07c77377',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'If-None-Match': 'W/"cacheable:55699f4d126e05bf16baaad002a1c04e"',
}
s.headers.update(headers)
base_url = 'https://eauto.co.in{}'
url = 'https://eauto.co.in/'
r = s.get(url)

def main_catogary(url1):
    r = s.get(url1)
    soup = BS(r.text,'html.parser')
    for i in soup.find_all('li'):
        main_catogary_link = i.find('a','nav-bar__link link')
        if main_catogary_link:
            main_catogary_link = main_catogary_link.get('href')
            if main_catogary_link and main_catogary_link.startswith('/pages/online-spare-parts-price-by-bike-model') or main_catogary_link.startswith('/collections') or main_catogary_link.startswith('/pages/bike-body-parts'):
                print(main_catogary_link)
                sub_category1(main_catogary_link)
            

def sub_category1(url2):
    r = s.get('https://eauto.co.in/{}'.format(url2))
    # r = s.get(url2)
    soup = BS(r.text,'html.parser')
    for i in soup.find_all('a','quick-links__link'):
        sub_category1_link = 'https://eauto.co.in'+ i.get('href')
        # print(sub_category1_link)
        list_page(sub_category1_link)

def list_page(url3):
    r = s.get(url3)
    soup = BS(r.text,'html.parser')
    for i in soup.find_all('a','product-item__title text--strong link'):
        list_page_link = 'https://eauto.co.in'+i.get('href')
        # print(list_page_link)
        product_page(list_page_link)

    next_page = [_next for _next in soup.find_all('a','pagination__next link') if 'Next' in _next.text.split()]
    if next_page:
        next_url = base_url.format(next_page[0].get('href'))
        print(next_url)
        list_page(next_url)

        product_page(list_page_link)


def product_page(url4):
    r = s.get(url4)
    soup = BS(r.text,'html.parser')
    name = soup.find('h1','product-meta__title heading h1')
    if name:
        name = name.text
    else:
        name = 'not givin'
    # print(name)

    review = soup.find('div','jdgm-prev-badge')
    if review:
        review = review.text
    else:
        review = 'not givin'

    price = soup.find('span','price price--highlight')
    if price:
        price = price.text.split()
    else:
        price = 'not givin'
    

    compatibility =  soup.find('div','vehicle_model_main')
    if compatibility:
        compatibility = compatibility.text.split()
    else:
        compatibility = 'not givin'

    for i in soup.find_all('div','aspect-ratio'):
        image = i.find('img')
        if image:
            image = image.get('data-src')

    for i in soup.find('tbody').find_all('tr'):
        if len(i.find_all('td')) == 2:
            key = i.find_all('td')[0]
            valu = i.find_all('td')[1]
            product_information = ('{} : {}'.format(key.text.strip(),valu.text.strip()))

    data = {
        'title' : name,
        'stars' : review,
        'rate' : price,
        'CC' : compatibility,
        'photo' : image, 
        'information' : product_information,
    }
    list1.append(data)
    print(r.url)

main_catogary('https://eauto.co.in/')

df = pandas.DataFrame(list1)
df.to_excel('eauto.xlsx',index=False)