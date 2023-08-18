from requests import session
from bs4 import BeautifulSoup as BS
s = session()
import requests
import json
import re
import pandas
list1 = []
# headers = {
#     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
#     'Accept': '*/*',
#     'Accept-Language': 'en-US,en;q=0.5',
#     # 'Accept-Encoding': 'gzip, deflate, br',
#     'x-algolia-api-key': '0e7364c3b87d2ef8f6ab2064f0519abb',
#     'x-algolia-application-id': 'XN5VEPVD4I',
#     'content-type': 'application/x-www-form-urlencoded',
#     'Origin': 'https://www.fashionnova.com',
#     'Connection': 'keep-alive',
#     'Referer': 'https://www.fashionnova.com/',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'cross-site',
# }

# data = '{"query":"","userToken":"anonymous-7faa53c6-a370-4e22-95d4-bbf6fae47036","ruleContexts":["collection","one-piece"],"analyticsTags":["collection","one-piece","desktop","Returning","India"],"clickAnalytics":true,"distinct":1,"page":0,"hitsPerPage":48,"facetFilters":["collections:one-piece"],"facetingAfterDistinct":true,"attributesToRetrieve":["handle","image","title"],"personalizationImpact":0}'

# response = requests.post(
#     'https://xn5vepvd4i-3.algolianet.com/1/indexes/products/query?x-algolia-agent=Algolia%20for%20JavaScript%20(4.14.2)%3B%20Browser',
#     headers=headers,
#     data=data,
# )
# s.headers.update(headers)
list_page_link=[]
# page = 1
# flag = True
# while flag:
def list_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'x-algolia-api-key': '0e7364c3b87d2ef8f6ab2064f0519abb',
        'x-algolia-application-id': 'XN5VEPVD4I',
        'content-type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.fashionnova.com',
        'Connection': 'keep-alive',
        'Referer': 'https://www.fashionnova.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
    }

    data = '{"query":"","userToken":"anonymous-7faa53c6-a370-4e22-95d4-bbf6fae47036","ruleContexts":["collection","one-piece"],"analyticsTags":["collection","one-piece","desktop","Returning","India"],"clickAnalytics":true,"distinct":1,"page":0,"hitsPerPage":48,"facetFilters":["collections:one-piece"],"facetingAfterDistinct":true,"attributesToRetrieve":["handle","image","title"],"personalizationImpact":0}'

    response = requests.post(
        'https://xn5vepvd4i-3.algolianet.com/1/indexes/products/query?x-algolia-agent=Algolia%20for%20JavaScript%20(4.14.2)%3B%20Browser',
        headers=headers,
        data=data,
    )
    s.headers.update(headers)
    response = requests.post(url,headers=headers,data=data)
    js = response.json()
    for i in js['hits']:
        # title = i.get('title')
        handle = 'https://www.fashionnova.com/products/'+i.get('handle')
        # print(handle)
        list_page_link.append(handle)
        # print(list_page_link)

        # product_page(list_page_link)

    # flag = False
    # page+=1
# list1=[]
def product_page(url2):


    cookies = {
        'shopify_pay_redirect': 'false',
        'secure_customer_sig': '',
        'localization': 'IN',
        '_y': '8bbfcbda-2011-4b10-bee5-04e30210c3a9',
        '_shopify_y': '8bbfcbda-2011-4b10-bee5-04e30210c3a9',
        '_attn_': 'eyJ1Ijoie1wiY29cIjoxNjY1NzI4MDQxNDI3LFwidW9cIjoxNjY1NzI4MDQxNDI3LFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcImMxOGJlYmQ1NjNmODQwNjA5YTI2ZjVhNTU3Mzk4YmQ5XCJ9In0=',
        '__attentive_id': 'c18bebd563f840609a26f5a557398bd9',
        '_ga_CHPZC04957': 'GS1.1.1691751283.31.1.1691751880.60.0.0',
        '_ga': 'GA1.2.690341277.1665728042',
        '__attentive_cco': '1665728041825',
        'syte_uuid': '67405190-4b87-11ed-b26b-9ffbed796710',
        '_scid': 'f4d422fb-d7c4-4062-8b9d-838b391aa285',
        '2c.cId': '64d0d6ab4873cf7e38fbb914',
        '_tt_enable_cookie': '1',
        '_ttp': '516a6278-8e35-4a9d-a919-d9322af68aff',
        'tkbl_cvuuid': 'fe39937d-ed69-42f8-8d1e-237e6e1d7a16',
        '_shopmsg.session': '3ac368c5-9d0e-420d-83c5-ce8c59ee7861',
        '_sctr': '1%7C1691346600000',
        'syte_ab_tests': '{}',
        'cto_bundle': 'ODlwT19hdHdNJTJCRHlCSjFJd1NiNHJ2SnhBNjhKdTZvR3BLRE4weUhXSFo0NE02b0k4dHcweUZMZEtxcG9jV3ZJdGFjbTltaFklMkY5RFlHTCUyRmVmOWNFJTJGMWJINE5HVzlMdlNyVkdOSUNaVXdpaG5iRlRDOUFKcThYdmZ4ZHlXNWl6d21PT2xZcnZPU0d5NVlNQzB3STJnZDVtWUFtZyUzRCUzRA',
        'ajs_anonymous_id': '86e2ec666d243978806877d08b55ccb9-55246279cf545b71e93c35073953f27641a577c284ce6db40ad97aaa1cb01a34',
        '_ce.s': 'v~4bbf2edf481609a25fa447df11c1ad2dffdb5f91~vpv~5~v11.rlc~1669897159755~v11slnt~1667366743788~ir~1~gtrk.la~larsf22y',
        '_pin_unauth': 'dWlkPU9HUTFNalZpWkdVdE56UXdNeTAwWkRBNExXSTBOMll0TlRJMk9XTXhOVGs0TTJZMQ',
        'tpc_a': 'de7da9f59fb54ed39aa11c4bb9098965.1670655249.Uwg.1670655249',
        'cart_currency': 'USD',
        '_cmp_a': '%7B%22purposes%22%3A%7B%22a%22%3Atrue%2C%22p%22%3Atrue%2C%22m%22%3Atrue%2C%22t%22%3Atrue%7D%2C%22display_banner%22%3Afalse%2C%22merchant_geo%22%3A%22US%22%2C%22sale_of_data_region%22%3Afalse%7D',
        '_orig_referrer': 'https%3A%2F%2Fwww.google.com%2F',
        '_landing_page': '%2F',
        '_gcl_au': '1.1.898630124.1691408039',
        '_ALGOLIA': 'anonymous-7faa53c6-a370-4e22-95d4-bbf6fae47036',
        '_gid': 'GA1.2.265897916.1691408045',
        '_gaexp': 'GAX1.2.uU7PPhATQMuk45yKEOeHOA.19602.x499!NOHXRS5DSwW43FpoWpH3iQ.19608.x941',
        'shopify_pay_redirect': 'false',
        'sailthru_set': 'Thu%20Aug%2010%202023%2017:27:29%20GMT+0530%20(India%20Standard%20Time)',
        'locale_bar_accepted': '1',
        'tooltip_displayed': 'true',
        'fromCollectionToPDPBreadcrumb': '%3Ca%20href%3D%22https%3A%2F%2Fwww.fashionnova.com%2F%22%20data-breadcrumbs-home-url%3D%22%22%20title%3D%22Women%22%20class%3D%22breadcrumbs__item%22%3E%0AWomen%0A%3C%2Fa%3E%0A%3Cspan%20class%3D%22breadcrumbs__separator%22%20aria-hidden%3D%22true%22%3E%3C%2Fspan%3E%0A%3Ca%20href%3D%22%2Fcollections%2Fswimwear%22%20class%3D%22breadcrumbs__item%22%3ESwim%3C%2Fa%3E%3Cspan%20class%3D%22breadcrumbs__separator%22%20aria-hidden%3D%22true%22%3E%3C%2Fspan%3E%3Ca%20href%3D%22%2Fcollections%2Fone-piece%22%20class%3D%22breadcrumbs__item-last%22%3E%0A%3Cspan%3EOne-piece%20swimsuits%3C%2Fspan%3E%0A%3C%2Fa%3E',
        '__attentive_dv': '1',
        'keep_alive': '520e7c62-9dbf-45d8-857c-da6b121f6941',
        '_s': '2c084dbe-c471-4786-9d05-4d9a87e11b5d',
        '_shopify_s': '2c084dbe-c471-4786-9d05-4d9a87e11b5d',
        '_shopify_sa_t': '2023-08-11T11%3A04%3A39.831Z',
        '_shopify_sa_p': '',
        '__attentive_pv': '4',
        '__attentive_ss_referrer': 'https://www.google.com/',
        'isReturning': '1',
        'stimgs': '{%22sessionId%22:31923826%2C%22didReportCameraImpression%22:false%2C%22newUser%22:false}',
        'sailthru_pageviews': '4',
        'po_visitor': '0qZZmcU0uBuM',
        '_scid_r': 'f4d422fb-d7c4-4062-8b9d-838b391aa285',
        'sailthru_content': '516b1ad12dec54ec53b9022593e28d4ea51acdfca024618ae47fa5ead471029af3c236f1bc87980061b4bccf304a9d2915a966ebb54aabab4926a1e10e9330a0c5400ab110a491db3350ead18369fc58620d0d3a2bc4e76c7d248bf1567c19a29c1c29e0ae14abf9879a79ecf4f0ae782a8fae0ac3b25a761bd6e64fad25f8bf915b34cf345c030109ab557d94473dd53bb82fd7e55ab0082159f8c708c54e73c336ec10f3f6795fa0f7de9ad1bf6ead3394f60bb144e7b8e28246f28953cdce9cdd3e7de07b2a5df0b717e7c388590a087d00144c93e5e2ae5e7828cfa565ecc2e531d148e22fda2ce0bfa88e952752bb2be2b0ca4b41c868d2a41b0083b88f',
        'sailthru_visitor': '046ab226-f210-4e5e-b485-a0369d321770',
        '_gat_UA-45937828-1': '1',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.fashionnova.com/products/barbie-sun-and-fun-1-piece-swimsuit-white',
        'sentry-trace': 'c6b9701a0ca8478ea6db9b280d1ee8d4-88afcb6eaab547d5-0',
        'baggage': 'sentry-environment=production,sentry-public_key=2ea17cd9213249ae8c87675605a7e5b8,sentry-trace_id=c6b9701a0ca8478ea6db9b280d1ee8d4',
        'Alt-Used': 'www.fashionnova.com',
        'Connection': 'keep-alive',
        # 'Cookie': 'shopify_pay_redirect=false; secure_customer_sig=; localization=IN; _y=8bbfcbda-2011-4b10-bee5-04e30210c3a9; _shopify_y=8bbfcbda-2011-4b10-bee5-04e30210c3a9; _attn_=eyJ1Ijoie1wiY29cIjoxNjY1NzI4MDQxNDI3LFwidW9cIjoxNjY1NzI4MDQxNDI3LFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcImMxOGJlYmQ1NjNmODQwNjA5YTI2ZjVhNTU3Mzk4YmQ5XCJ9In0=; __attentive_id=c18bebd563f840609a26f5a557398bd9; _ga_CHPZC04957=GS1.1.1691751283.31.1.1691751880.60.0.0; _ga=GA1.2.690341277.1665728042; __attentive_cco=1665728041825; syte_uuid=67405190-4b87-11ed-b26b-9ffbed796710; _scid=f4d422fb-d7c4-4062-8b9d-838b391aa285; 2c.cId=64d0d6ab4873cf7e38fbb914; _tt_enable_cookie=1; _ttp=516a6278-8e35-4a9d-a919-d9322af68aff; tkbl_cvuuid=fe39937d-ed69-42f8-8d1e-237e6e1d7a16; _shopmsg.session=3ac368c5-9d0e-420d-83c5-ce8c59ee7861; _sctr=1%7C1691346600000; syte_ab_tests={}; cto_bundle=ODlwT19hdHdNJTJCRHlCSjFJd1NiNHJ2SnhBNjhKdTZvR3BLRE4weUhXSFo0NE02b0k4dHcweUZMZEtxcG9jV3ZJdGFjbTltaFklMkY5RFlHTCUyRmVmOWNFJTJGMWJINE5HVzlMdlNyVkdOSUNaVXdpaG5iRlRDOUFKcThYdmZ4ZHlXNWl6d21PT2xZcnZPU0d5NVlNQzB3STJnZDVtWUFtZyUzRCUzRA; ajs_anonymous_id=86e2ec666d243978806877d08b55ccb9-55246279cf545b71e93c35073953f27641a577c284ce6db40ad97aaa1cb01a34; _ce.s=v~4bbf2edf481609a25fa447df11c1ad2dffdb5f91~vpv~5~v11.rlc~1669897159755~v11slnt~1667366743788~ir~1~gtrk.la~larsf22y; _pin_unauth=dWlkPU9HUTFNalZpWkdVdE56UXdNeTAwWkRBNExXSTBOMll0TlRJMk9XTXhOVGs0TTJZMQ; tpc_a=de7da9f59fb54ed39aa11c4bb9098965.1670655249.Uwg.1670655249; cart_currency=USD; _cmp_a=%7B%22purposes%22%3A%7B%22a%22%3Atrue%2C%22p%22%3Atrue%2C%22m%22%3Atrue%2C%22t%22%3Atrue%7D%2C%22display_banner%22%3Afalse%2C%22merchant_geo%22%3A%22US%22%2C%22sale_of_data_region%22%3Afalse%7D; _orig_referrer=https%3A%2F%2Fwww.google.com%2F; _landing_page=%2F; _gcl_au=1.1.898630124.1691408039; _ALGOLIA=anonymous-7faa53c6-a370-4e22-95d4-bbf6fae47036; _gid=GA1.2.265897916.1691408045; _gaexp=GAX1.2.uU7PPhATQMuk45yKEOeHOA.19602.x499!NOHXRS5DSwW43FpoWpH3iQ.19608.x941; shopify_pay_redirect=false; sailthru_set=Thu%20Aug%2010%202023%2017:27:29%20GMT+0530%20(India%20Standard%20Time); locale_bar_accepted=1; tooltip_displayed=true; fromCollectionToPDPBreadcrumb=%3Ca%20href%3D%22https%3A%2F%2Fwww.fashionnova.com%2F%22%20data-breadcrumbs-home-url%3D%22%22%20title%3D%22Women%22%20class%3D%22breadcrumbs__item%22%3E%0AWomen%0A%3C%2Fa%3E%0A%3Cspan%20class%3D%22breadcrumbs__separator%22%20aria-hidden%3D%22true%22%3E%3C%2Fspan%3E%0A%3Ca%20href%3D%22%2Fcollections%2Fswimwear%22%20class%3D%22breadcrumbs__item%22%3ESwim%3C%2Fa%3E%3Cspan%20class%3D%22breadcrumbs__separator%22%20aria-hidden%3D%22true%22%3E%3C%2Fspan%3E%3Ca%20href%3D%22%2Fcollections%2Fone-piece%22%20class%3D%22breadcrumbs__item-last%22%3E%0A%3Cspan%3EOne-piece%20swimsuits%3C%2Fspan%3E%0A%3C%2Fa%3E; __attentive_dv=1; keep_alive=520e7c62-9dbf-45d8-857c-da6b121f6941; _s=2c084dbe-c471-4786-9d05-4d9a87e11b5d; _shopify_s=2c084dbe-c471-4786-9d05-4d9a87e11b5d; _shopify_sa_t=2023-08-11T11%3A04%3A39.831Z; _shopify_sa_p=; __attentive_pv=4; __attentive_ss_referrer=https://www.google.com/; isReturning=1; stimgs={%22sessionId%22:31923826%2C%22didReportCameraImpression%22:false%2C%22newUser%22:false}; sailthru_pageviews=4; po_visitor=0qZZmcU0uBuM; _scid_r=f4d422fb-d7c4-4062-8b9d-838b391aa285; sailthru_content=516b1ad12dec54ec53b9022593e28d4ea51acdfca024618ae47fa5ead471029af3c236f1bc87980061b4bccf304a9d2915a966ebb54aabab4926a1e10e9330a0c5400ab110a491db3350ead18369fc58620d0d3a2bc4e76c7d248bf1567c19a29c1c29e0ae14abf9879a79ecf4f0ae782a8fae0ac3b25a761bd6e64fad25f8bf915b34cf345c030109ab557d94473dd53bb82fd7e55ab0082159f8c708c54e73c336ec10f3f6795fa0f7de9ad1bf6ead3394f60bb144e7b8e28246f28953cdce9cdd3e7de07b2a5df0b717e7c388590a087d00144c93e5e2ae5e7828cfa565ecc2e531d148e22fda2ce0bfa88e952752bb2be2b0ca4b41c868d2a41b0083b88f; sailthru_visitor=046ab226-f210-4e5e-b485-a0369d321770; _gat_UA-45937828-1=1',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'If-None-Match': 'W/"cacheable:a836d87deeb29b5230ba801844875895"',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    params = {
        'view': 'pdp-json',
    }

    response = requests.get(
        'https://www.fashionnova.com/products/barbie-sun-and-fun-1-piece-swimsuit-white',
        params=params,
        cookies=cookies,
        headers=headers,
    )

    # s.headers.update(headers)
    response = requests.get(url2,params=params,cookies=cookies,headers=headers)

    js = response.json()
    for i in js['products']:
        name = i.get('title')
        
        price = i.get('presentation_price')
        presentation_price = re.search('\>(.*?)\<',price).group(1)

        second_price = i.get('presentation_compare_at_price')
        presentation_compare_at_price = re.search('\>(.*?)\<',second_price).group(1)

        products_details = i.get('description')
        discription = re.findall('\>(.*?)\<',products_details)

        for j in js['products'][0]['variants']:
            size = j.get('title')

        for k in js['products'][0]['images']:
            images = k.get('src')
        try:
            image = re.search('\//(.*?)\?',images).group(1)
        except:
            image = ''     
        # print(image)
        for m in js['products'][0]['swatches']:
            swatches = 'https:/xn5vepvd4i-3.algolianet.com'+ m
        try:

            color_link = re.search('(.*?)\:#',swatches).group(1)
        except:
            color_link = ''
        # print(color_link)


        data ={
            'title': name,
            'price1' : presentation_price,
            'price2' : presentation_compare_at_price,
            'product_details' : discription,
            'lenth' : size,
            'photos' : image,
            'wtatches' : color_link

        }
        list1.append(data)
        print(list1)



     


list_page('https://xn5vepvd4i-3.algolianet.com/1/indexes/products/query?x-algolia-agent=Algolia for JavaScript (4.14.2); Browser')
for url in list_page_link:
    product_page(url)

df = pandas.DataFrame(list1)
df.to_excel('fashionnova.xlsx',index=False)