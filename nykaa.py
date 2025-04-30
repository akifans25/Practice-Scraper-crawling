from requests import session
from bs4 import BeautifulSoup as BS
s = session()
import re
import requests
list1 = []
import pandas
def main(url):
    cookies = {
    'bcookie': '3c7b4e13-0cc0-4909-be12-a5d5ae4debe6',
    'EXP_ADP_RV_REORDER': 'B',
    'EXP_ADP_RV_SEGMENT': 'B',
    'EXP_AB_AUTOFILL': 'B',
    'EXP_ADP_RV_VIEW_SIMILAR': 'A',
    'EXP_ADP_RV_PLP_CONFIGURABLE_NO_RESULTS': 'A',
    'EXP_CART_LOGIN_SEGMENT': 'A',
    'EXP_AB_WISHLIST': 'A',
    'EXP_AB_PRICE_REVEAL_NEW': 'A',
    'EXP_PLP_INLINE_FILTER': 'A',
    'EXP_EDD_DELIVERY_WIDGET': 'A',
    'EXP_ADP_RV_MULTI_COUPONS': 'A',
    'EXP_ADP_RV_SEARCH_BAR_NEW': 'A',
    'EXP_VIEW_TRANSITION': 'A',
    'EXP_INCORRECT_SLUG_REDIRECT': 'A',
    'EXP_PRIVE_MULTI_COUPONS': 'A',
    'EXP_SLP_RELATED_SEARCHES': 'CONTROL',
    'EXP_UPDATED_AT': '1694502047742',
    'EXP_SSR_CACHE': '797b0be9f87167ee3ff0af828e8f05b4',
    '__cfruid': 'db9423d34e57a5b13b8e83316c528b944a46c3d2-1694517602',
    'AMCV_FE9A65E655E6E38A7F000101%40AdobeOrg': '-432600572%7CMCIDTS%7C19613%7CMCMID%7C75897260445342361690155450952129183773%7CMCAAMLH-1695167688%7C12%7CMCAAMB-1695167688%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1694570088s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.5.2',
    'SITE_VISIT_COUNT': '18',
    'run': '61',
    'EXP_REVIEW_COLLECTION': '1',
    'D_LST': '1',
    'D_PDP': '1',
    's_nr365': '1694562887956-Repeat',
    'd_info': '1440_900',
    'PHPSESSID': 'PMQCj9Bk5soaubw1694455596063',
    'head_data_react': '{"id":"","nykaa_pro":false,"group_id":""}',
    'pro': 'false',
    'AMCVS_FE9A65E655E6E38A7F000101%40AdobeOrg': '1',
    's_cc': 'true',
    '_gcl_au': '1.1.1916338347.1694500751',
    '_ga': 'GA1.2.443952602.1694500752',
    '_gid': 'GA1.2.675084075.1694500752',
    '_ga_LKNEBVRZRG': 'GS1.1.1694562758.4.1.1694562891.60.0.0',
    'mfKey': '1wkkmng.1694500751797',
    '_ga_JQ1CQHSXRX': 'GS1.2.1694562758.4.1.1694562891.60.0.0',
    '_clck': '8d9a5o|2|fey|0|1349',
    's_sq': 'fsnecommerceprod%3D%2526c.%2526a.%2526activitymap.%2526page%253DNykaa%2526link%253D2%2526region%253Dlist-wrapper%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DNykaa%2526pidt%253D1%2526oid%253Dfunctioncn%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DA',
    'mf_visitid': '1494iiv.1694548159170',
    'mf_utms': '%7B%22productId%22%3A%229285523%22%2C%22pps%22%3A%221%22%7D',
    '_clsk': '1u3enoc|1694562892740|2|1|u.clarity.ms/collect',
    '_gat_UA-31866293-9': '1',
}

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/117.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.nykaa.com/makeup/lips/lipstick/c/249',
        'X-NewRelic-ID': 'undefined',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjEyMjUxNTkiLCJhcCI6IjEwMDE0NzQ3MTciLCJpZCI6IjM2OTQyMDZhMmU5ZTRlYTAiLCJ0ciI6IjVlZWIzOGUwMjRkOWVlNzQ5NjcyOTU5N2E1YTAwODAwIiwidGkiOjE2OTQ1NjI5MTM5MjZ9fQ==',
        'traceparent': '00-5eeb38e024d9ee7496729597a5a00800-3694206a2e9e4ea0-01',
        'tracestate': '1225159@nr=0-1-1225159-1001474717-3694206a2e9e4ea0----1694562913926',
        'x-csrf-token': '1AUPmjvnNxjeEpxc',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Connection': 'keep-alive',
        # 'Cookie': 'bcookie=3c7b4e13-0cc0-4909-be12-a5d5ae4debe6; EXP_ADP_RV_REORDER=B; EXP_ADP_RV_SEGMENT=B; EXP_AB_AUTOFILL=B; EXP_ADP_RV_VIEW_SIMILAR=A; EXP_ADP_RV_PLP_CONFIGURABLE_NO_RESULTS=A; EXP_CART_LOGIN_SEGMENT=A; EXP_AB_WISHLIST=A; EXP_AB_PRICE_REVEAL_NEW=A; EXP_PLP_INLINE_FILTER=A; EXP_EDD_DELIVERY_WIDGET=A; EXP_ADP_RV_MULTI_COUPONS=A; EXP_ADP_RV_SEARCH_BAR_NEW=A; EXP_VIEW_TRANSITION=A; EXP_INCORRECT_SLUG_REDIRECT=A; EXP_PRIVE_MULTI_COUPONS=A; EXP_SLP_RELATED_SEARCHES=CONTROL; EXP_UPDATED_AT=1694502047742; EXP_SSR_CACHE=797b0be9f87167ee3ff0af828e8f05b4; __cfruid=db9423d34e57a5b13b8e83316c528b944a46c3d2-1694517602; AMCV_FE9A65E655E6E38A7F000101%40AdobeOrg=-432600572%7CMCIDTS%7C19613%7CMCMID%7C75897260445342361690155450952129183773%7CMCAAMLH-1695167688%7C12%7CMCAAMB-1695167688%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1694570088s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.5.2; SITE_VISIT_COUNT=18; run=61; EXP_REVIEW_COLLECTION=1; D_LST=1; D_PDP=1; s_nr365=1694562887956-Repeat; d_info=1440_900; PHPSESSID=PMQCj9Bk5soaubw1694455596063; head_data_react={"id":"","nykaa_pro":false,"group_id":""}; pro=false; AMCVS_FE9A65E655E6E38A7F000101%40AdobeOrg=1; s_cc=true; _gcl_au=1.1.1916338347.1694500751; _ga=GA1.2.443952602.1694500752; _gid=GA1.2.675084075.1694500752; _ga_LKNEBVRZRG=GS1.1.1694562758.4.1.1694562891.60.0.0; mfKey=1wkkmng.1694500751797; _ga_JQ1CQHSXRX=GS1.2.1694562758.4.1.1694562891.60.0.0; _clck=8d9a5o|2|fey|0|1349; s_sq=fsnecommerceprod%3D%2526c.%2526a.%2526activitymap.%2526page%253DNykaa%2526link%253D2%2526region%253Dlist-wrapper%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DNykaa%2526pidt%253D1%2526oid%253Dfunctioncn%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DA; mf_visitid=1494iiv.1694548159170; mf_utms=%7B%22productId%22%3A%229285523%22%2C%22pps%22%3A%221%22%7D; _clsk=1u3enoc|1694562892740|2|1|u.clarity.ms/collect; _gat_UA-31866293-9=1',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
        
    }


    a = re.search('\/c\/(.*?)\?',link).group(1)
    num = 0
    flag = True
    while flag:

        params = {
            'category_id': str(a),
            'client': 'react',
            'filter_format': 'v2',
            'page_no': ''+str(num)+'',
            'platform': 'website',
            'sort': 'popularity',
        }

        response = requests.get('https://www.nykaa.com/app-api/index.php/products/list', params=params, cookies=cookies, headers=headers)


        list_links = 'https://www.nykaa.com/makeup/lips/lipstick/c/249?page_no=1&sort=popularity&eq=desktop'
        # list_links = 'https://www.nykaa.com/makeup/lips/liquid-lipstick/c/263?page_no=1&sort=popularity&eq=desktop'

        js = response.json()
        response = requests.get(list_links)
            
        for i in js['response']['products']:
            links = i.get('product_url')
            print(links,'------------>',num)
            name = i.get('name')
            price = i.get('final_price')
            ratings = i.get('rating')
            totalrating = i.get('rating_count')
            off = i.get('discount')
        for j in js ['response']['products'][0]['media']:
            imagelink = j.get('url')
        data = {'name': name,
                'link' : links,
                'price' : price,
                'ratung' : ratings,
                'totalrating' : totalrating,
                'offs' : off,
                'image' : imagelink
        }
        list1.append(data)
        # print(list1)
            

        num+=1
        if len(js['response']['products']) == 0:
            break


link = 'https://www.nykaa.com/makeup/lips/liquid-lipstick/c/263?page_no=1&sort=popularity&eq=desktop'
pro = main(link)
# main ()

df = pandas.DataFrame(list1)
df.to_excel('nykaa._linkwise.xlsx',index=False)