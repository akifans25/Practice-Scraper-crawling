# import requests
# from requests import Session
# s = Session()
# import json
# import requests

# cookies = {
#     'AKA_A2': 'A',
#     '_gcl_au': '1.1.1275480300.1689678531',
#     'WZRK_S_865-K54-K75Z': '%7B%22p%22%3A9%7D',
#     'USER_DATA': '%7B%22attributes%22%3A%5B%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%22fcf876b6-4ecb-48fd-b759-fbf32ac22848%22%2C%22deviceAdded%22%3Atrue%7D',
#     'moe_uuid': 'fcf876b6-4ecb-48fd-b759-fbf32ac22848',
#     '_ga_F1NJ1E2HJ2': 'GS1.1.1689678532.1.1.1689680166.0.0.0',
#     '_ga': 'GA1.2.880693437.1689678532',
#     '_gid': 'GA1.2.21972947.1689678532',
#     '_hjSessionUser_2590087': 'eyJpZCI6IjUxZDIxYzRiLWE4NTktNTdhMi05MTc2LTlkOTk5ZTFkMWYyMyIsImNyZWF0ZWQiOjE2ODk2Nzg1MzI1NzMsImV4aXN0aW5nIjp0cnVlfQ==',
#     '_hjFirstSeen': '1',
#     '_hjIncludedInSessionSample_2590087': '0',
#     '_hjSession_2590087': 'eyJpZCI6IjJhYWNjZmMxLTlhNDQtNDUyNy04OGRlLThmODdmODZlYjY3NSIsImNyZWF0ZWQiOjE2ODk2Nzg1MzI1NzcsImluU2FtcGxlIjpmYWxzZX0=',
#     '_hjAbsoluteSessionInProgress': '0',
#     'OPT_IN_SHOWN_TIME': '1689678536666',
#     'SOFT_ASK_STATUS': '%7B%22actualValue%22%3A%22dismissed%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D',
#     '_ga_NXPBDLCSFK': 'GS1.1.1689678547.1.1.1689680195.29.0.0',
# }

# headers = {
#     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
#     'Accept-Language': 'en-US,en;q=0.5',
#     # 'Accept-Encoding': 'gzip, deflate, br',
#     'Content-Type': 'application/json',
#     'Origin': 'null',
#     'Connection': 'keep-alive',
#     # 'Cookie': 'AKA_A2=A; _gcl_au=1.1.1275480300.1689678531; WZRK_S_865-K54-K75Z=%7B%22p%22%3A9%7D; USER_DATA=%7B%22attributes%22%3A%5B%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%22fcf876b6-4ecb-48fd-b759-fbf32ac22848%22%2C%22deviceAdded%22%3Atrue%7D; moe_uuid=fcf876b6-4ecb-48fd-b759-fbf32ac22848; _ga_F1NJ1E2HJ2=GS1.1.1689678532.1.1.1689680166.0.0.0; _ga=GA1.2.880693437.1689678532; _gid=GA1.2.21972947.1689678532; _hjSessionUser_2590087=eyJpZCI6IjUxZDIxYzRiLWE4NTktNTdhMi05MTc2LTlkOTk5ZTFkMWYyMyIsImNyZWF0ZWQiOjE2ODk2Nzg1MzI1NzMsImV4aXN0aW5nIjp0cnVlfQ==; _hjFirstSeen=1; _hjIncludedInSessionSample_2590087=0; _hjSession_2590087=eyJpZCI6IjJhYWNjZmMxLTlhNDQtNDUyNy04OGRlLThmODdmODZlYjY3NSIsImNyZWF0ZWQiOjE2ODk2Nzg1MzI1NzcsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; OPT_IN_SHOWN_TIME=1689678536666; SOFT_ASK_STATUS=%7B%22actualValue%22%3A%22dismissed%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D; _ga_NXPBDLCSFK=GS1.1.1689678547.1.1.1689680195.29.0.0',
#     'Upgrade-Insecure-Requests': '1',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'none',
#     'Sec-Fetch-User': '?1',
#     # Requests doesn't support trailers
#     # 'TE': 'trailers',
# }

# json_data = {
#     'query': '\n        {\n          listing(\n              page:2,\n              size:24,\n              gender:2,\n              isKids:false,\n              isWeb: true,\n              sort:DEFAULT,\n              category: [996],\n              artist: [],\n              tags: []\n              filters:{\n                category: [],\n                artist: [],\n                tags: [],\n                size: [],\n                price: []\n                gender: [],\n                fabric: [],\n                color: [],\n                discount: [],\n                pattern: [],\n                sleeve: [],\n                neck: [],\n                fittype: [],\n              },\n              tiptile:1\n              ){\n            products{\n              id\n              product\n              artist{name,slug}\n              category{name}\n              price\n              genderType\n              stock\n              avgRating\n              ratingCount\n              prodQty\n              prodType\n              splPrice\n              exclusivePrice\n              sortOrder\n              images\n              imagesNew\n              extraPrice\n              isPrintable\n              jitValue\n              product_slug: productSlug\n              tiptiles {id type name navLink image mobileImage colWidth isClickable promotionName}\n              \n            }\n            pagination {\n              currentPage\n              totalPages\n              totalProduct\n            }\n            filters{\n              options{\n                name\n                slug\n              }\n              alias\n              field\n            }\n            isMaleDataAvailable\n            isFemaleDataAvailable\n            isKidDataAvailable\n          }\n        }\n        ',
#     'localcart': {
#         'products': {
#             'items': [],
#             'index': {
#                 '147501': None,
#                 '152694': None,
#                 '161509': None,
#                 '168951': None,
#                 '168952': None,
#                 '172671': None,
#                 '173539': None,
#             },
#         },
#         'giftvouchers': {
#             'items': [],
#             'index': {},
#         },
#         'complementary_products': {
#             'items': [],
#             'index': {},
#         },
#         'widgets': {
#             'items': [],
#             'index': {},
#         },
#         'meta': {
#             'items': [
#                 {
#                     'name': 'hyperlocal_order',
#                     'hl_charges': 0,
#                     'hl_charges_applied': False,
#                     'is_shipping_chargable': False,
#                     'shipping_charge': 0,
#                     'hl_charge': 100,
#                     'updated_at': '2023-07-18T17:06:06.090513',
#                 },
#                 {
#                     'name': 'site_config',
#                     'exclusive': True,
#                     'exclusive_product': 147501,
#                     'exclusive_products': [
#                         {
#                             'prod_id': '152694',
#                             'price': 149,
#                             'duration': 30,
#                             'name': 'Monthly',
#                             'description': [
#                                 'Get Instant Access for a Month',
#                             ],
#                         },
#                         {
#                             'prod_id': '161509',
#                             'price': 299,
#                             'duration': 90,
#                             'name': 'Quarterly',
#                             'description': [
#                                 'Get Instant Access for 3 Months',
#                             ],
#                         },
#                         {
#                             'prod_id': '147501',
#                             'price': 299,
#                             'duration': 365,
#                             'name': 'Yearly',
#                             'description': [
#                                 'Get Instant Access for a Year',
#                             ],
#                         },
#                         {
#                             'prod_id': '173539',
#                             'price': 0,
#                             'duration': 90,
#                             'name': 'Quarterly',
#                             'description': [
#                                 'Get Instant Access for 3 Months',
#                             ],
#                         },
#                     ],
#                     'exclusive_product_upgrade': {
#                         '168951': {
#                             'expiry_delta': 330,
#                         },
#                         '168952': {
#                             'expiry_delta': 270,
#                         },
#                         '172671': {
#                             'expiry_delta': 365,
#                         },
#                     },
#                     'exclusive_products_upgrade': [
#                         {
#                             'prod_id': '172671',
#                             'price': 199,
#                             'duration': 365,
#                             'name': 'Upgrade by Yearly',
#                             'description': [
#                                 'Get Instant Access',
#                             ],
#                         },
#                         {
#                             'prod_id': '168951',
#                             'price': 100,
#                             'duration': 330,
#                             'name': 'Upgrade from Monthly to Yearly',
#                             'description': [
#                                 'Get Instant Access',
#                             ],
#                         },
#                         {
#                             'prod_id': '168952',
#                             'price': 50,
#                             'duration': 270,
#                             'name': 'Upgrade from Quarterly to Yearly',
#                             'description': [
#                                 'Get Instant Access',
#                             ],
#                         },
#                     ],
#                     'is_exclusive_discount_visible': 'True',
#                     'free_membership_removed': False,
#                     'updated_at': '2023-07-18T17:06:06.091885',
#                 },
#                 {
#                     'name': 'active_pricelists',
#                     'pricelists': [],
#                     'updated_at': '2023-07-18T17:06:06.090625',
#                 },
#                 {
#                     'name': 'calculations',
#                     'sub_total': 0,
#                     'main_sub_total': 0,
#                     'base_sub_total': 0,
#                     'gst_total': 0,
#                     'total': 0,
#                     'rounding_off': 0,
#                     'gift_wrap_amount': 0,
#                     'coupon_discount': 0,
#                     'giftvoucher_value': 0,
#                     'referral_code': 0,
#                     'shipping_charges': 0,
#                     'cod_charges': 15,
#                     'hl_charges': 0,
#                     'used_reward_points': 0,
#                     'total_savings': 0,
#                     'exclusive_savings': 0,
#                     'extra_price': 0,
#                     'app_discount': 0,
#                     'used_tss_points': 0,
#                     'used_tss_money': 0,
#                     'app_discount_percent': 0,
#                     'app_cashback': 0,
#                     'app_cashback_percent': 10,
#                     'gift_voucher_value': 0,
#                     'tss_points_discount': 20,
#                     'app_discount_status': False,
#                     'updated_at': '2023-07-18T17:06:06.090599',
#                 },
#                 {
#                     'name': 'reward_points',
#                     'used_points': 0,
#                     'total_points': 0,
#                     'updated_at': '2023-07-18T17:06:06.090564',
#                 },
#                 {
#                     'name': 'tss_money',
#                     'used_tss_money': 0,
#                     'total_tss_money': 0,
#                     'updated_at': '2023-07-18T17:06:06.090577',
#                 },
#                 {
#                     'name': 'tss_points',
#                     'used_tss_points': 0,
#                     'total_tss_points': 0,
#                     'updated_at': '2023-07-18T17:06:06.090588',
#                 },
#             ],
#             'index': {
#                 'exclusive_user': None,
#                 'exclusive_bkp': None,
#                 'coupon': None,
#                 'gift_voucher': None,
#                 'hyperlocal_order': 0,
#                 'payment_details': None,
#                 'calculations': 3,
#                 'active_pricelists': 2,
#                 'site_config': 1,
#                 'tss_points': 6,
#                 'reward_points': 4,
#                 'tss_money': 5,
#             },
#         },
#         'event_id': 'pageview_168968016606244492530822754',
#     },
# }

# response = requests.post('https://api.thesouledstore.com/api/v2/graphql', cookies=cookies, headers=headers, json=json_data)

# # Note: json_data will not be serialized by requests
# # exactly as it was in the original request.
# #data = '{"query":"\\n        {\\n          listing(\\n              page:2,\\n              size:24,\\n              gender:2,\\n              isKids:false,\\n              isWeb: true,\\n              sort:DEFAULT,\\n              category: [996],\\n              artist: [],\\n              tags: []\\n              filters:{\\n                category: [],\\n                artist: [],\\n                tags: [],\\n                size: [],\\n                price: []\\n                gender: [],\\n                fabric: [],\\n                color: [],\\n                discount: [],\\n                pattern: [],\\n                sleeve: [],\\n                neck: [],\\n                fittype: [],\\n              },\\n              tiptile:1\\n              ){\\n            products{\\n              id\\n              product\\n              artist{name,slug}\\n              category{name}\\n              price\\n              genderType\\n              stock\\n              avgRating\\n              ratingCount\\n              prodQty\\n              prodType\\n              splPrice\\n              exclusivePrice\\n              sortOrder\\n              images\\n              imagesNew\\n              extraPrice\\n              isPrintable\\n              jitValue\\n              product_slug: productSlug\\n              tiptiles {id type name navLink image mobileImage colWidth isClickable promotionName}\\n              \\n            }\\n            pagination {\\n              currentPage\\n              totalPages\\n              totalProduct\\n            }\\n            filters{\\n              options{\\n                name\\n                slug\\n              }\\n              alias\\n              field\\n            }\\n            isMaleDataAvailable\\n            isFemaleDataAvailable\\n            isKidDataAvailable\\n          }\\n        }\\n        ","localcart":{"products":{"items":[],"index":{"147501":null,"152694":null,"161509":null,"168951":null,"168952":null,"172671":null,"173539":null}},"giftvouchers":{"items":[],"index":{}},"complementary_products":{"items":[],"index":{}},"widgets":{"items":[],"index":{}},"meta":{"items":[{"name":"hyperlocal_order","hl_charges":0,"hl_charges_applied":false,"is_shipping_chargable":false,"shipping_charge":0,"hl_charge":100,"updated_at":"2023-07-18T17:06:06.090513"},{"name":"site_config","exclusive":true,"exclusive_product":147501,"exclusive_products":[{"prod_id":"152694","price":149,"duration":30,"name":"Monthly","description":["Get Instant Access for a Month"]},{"prod_id":"161509","price":299,"duration":90,"name":"Quarterly","description":["Get Instant Access for 3 Months"]},{"prod_id":"147501","price":299,"duration":365,"name":"Yearly","description":["Get Instant Access for a Year"]},{"prod_id":"173539","price":0,"duration":90,"name":"Quarterly","description":["Get Instant Access for 3 Months"]}],"exclusive_product_upgrade":{"168951":{"expiry_delta":330},"168952":{"expiry_delta":270},"172671":{"expiry_delta":365}},"exclusive_products_upgrade":[{"prod_id":"172671","price":199,"duration":365,"name":"Upgrade by Yearly","description":["Get Instant Access"]},{"prod_id":"168951","price":100,"duration":330,"name":"Upgrade from Monthly to Yearly","description":["Get Instant Access"]},{"prod_id":"168952","price":50,"duration":270,"name":"Upgrade from Quarterly to Yearly","description":["Get Instant Access"]}],"is_exclusive_discount_visible":"True","free_membership_removed":false,"updated_at":"2023-07-18T17:06:06.091885"},{"name":"active_pricelists","pricelists":[],"updated_at":"2023-07-18T17:06:06.090625"},{"name":"calculations","sub_total":0,"main_sub_total":0,"base_sub_total":0,"gst_total":0,"total":0,"rounding_off":0,"gift_wrap_amount":0,"coupon_discount":0,"giftvoucher_value":0,"referral_code":0,"shipping_charges":0,"cod_charges":15,"hl_charges":0,"used_reward_points":0,"total_savings":0,"exclusive_savings":0,"extra_price":0,"app_discount":0,"used_tss_points":0,"used_tss_money":0,"app_discount_percent":0,"app_cashback":0,"app_cashback_percent":10,"gift_voucher_value":0,"tss_points_discount":20,"app_discount_status":false,"updated_at":"2023-07-18T17:06:06.090599"},{"name":"reward_points","used_points":0,"total_points":0,"updated_at":"2023-07-18T17:06:06.090564"},{"name":"tss_money","used_tss_money":0,"total_tss_money":0,"updated_at":"2023-07-18T17:06:06.090577"},{"name":"tss_points","used_tss_points":0,"total_tss_points":0,"updated_at":"2023-07-18T17:06:06.090588"}],"index":{"exclusive_user":null,"exclusive_bkp":null,"coupon":null,"gift_voucher":null,"hyperlocal_order":0,"payment_details":null,"calculations":3,"active_pricelists":2,"site_config":1,"tss_points":6,"reward_points":4,"tss_money":5}},"event_id":"pageview_168968016606244492530822754"}}'
# #response = requests.post('https://api.thesouledstore.com/api/v2/graphql', cookies=cookies, headers=headers, data=data)



# js = response.json()
# list1 = []
# for i in js['data']['listing']['products']:
#     product = i.get('product')
#     price = i.get('price')
#     avgRating = i.get('avgRating')
#     category = i.get('category')
#     images = i.get('images')
#     genderType = i.get('genderType')
#     jitValue = i.get('jitValue')
#     data = {
#         'name' : product,
#         'rate' : price,
#         'avgrating' : avgRating,
#         'photo' : images,
#         'gentype' : genderType,
#         'jit' : jitValue, 
#     }
#     list1.append(data)
#     print(list1)
                











import requests
from requests import Session
s = Session()
import json
import requests

cookies = {
    '_gcl_au': '1.1.1275480300.1689678531',
    'USER_DATA': '%7B%22attributes%22%3A%5B%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%22fcf876b6-4ecb-48fd-b759-fbf32ac22848%22%2C%22deviceAdded%22%3Atrue%7D',
    '_ga_F1NJ1E2HJ2': 'GS1.1.1689768067.5.1.1689768584.0.0.0',
    '_ga': 'GA1.2.880693437.1689678532',
    '_gid': 'GA1.2.21972947.1689678532',
    '_hjSessionUser_2590087': 'eyJpZCI6IjUxZDIxYzRiLWE4NTktNTdhMi05MTc2LTlkOTk5ZTFkMWYyMyIsImNyZWF0ZWQiOjE2ODk2Nzg1MzI1NzMsImV4aXN0aW5nIjp0cnVlfQ==',
    'OPT_IN_SHOWN_TIME': '1689764299386',
    'SOFT_ASK_STATUS': '%7B%22actualValue%22%3A%22dismissed%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D',
    '_ga_NXPBDLCSFK': 'GS1.1.1689768064.6.1.1689768835.59.0.0',
    'moe_uuid': 'fcf876b6-4ecb-48fd-b759-fbf32ac22848',
    '_hjIncludedInSessionSample_2590087': '0',
    'AKA_A2': 'A',
    '_hjSession_2590087': 'eyJpZCI6ImQ1YzY3Y2QyLWVhYzUtNGU5Yi1hNjQ1LTgzMzliYWUxNjVjNCIsImNyZWF0ZWQiOjE2ODk3NjgwNjg2NzcsImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '0',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    # 'Cookie': '_gcl_au=1.1.1275480300.1689678531; USER_DATA=%7B%22attributes%22%3A%5B%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%22fcf876b6-4ecb-48fd-b759-fbf32ac22848%22%2C%22deviceAdded%22%3Atrue%7D; _ga_F1NJ1E2HJ2=GS1.1.1689768067.5.1.1689768584.0.0.0; _ga=GA1.2.880693437.1689678532; _gid=GA1.2.21972947.1689678532; _hjSessionUser_2590087=eyJpZCI6IjUxZDIxYzRiLWE4NTktNTdhMi05MTc2LTlkOTk5ZTFkMWYyMyIsImNyZWF0ZWQiOjE2ODk2Nzg1MzI1NzMsImV4aXN0aW5nIjp0cnVlfQ==; OPT_IN_SHOWN_TIME=1689764299386; SOFT_ASK_STATUS=%7B%22actualValue%22%3A%22dismissed%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D; _ga_NXPBDLCSFK=GS1.1.1689768064.6.1.1689768835.59.0.0; moe_uuid=fcf876b6-4ecb-48fd-b759-fbf32ac22848; _hjIncludedInSessionSample_2590087=0; AKA_A2=A; _hjSession_2590087=eyJpZCI6ImQ1YzY3Y2QyLWVhYzUtNGU5Yi1hNjQ1LTgzMzliYWUxNjVjNCIsImNyZWF0ZWQiOjE2ODk3NjgwNjg2NzcsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

response = requests.get('https://mapi.thesouledstore.com/api/v2/web_menu/webmenu', cookies=cookies, headers=headers)
s.headers.update(headers)
js = response.json()

def main_category(url):
    response = requests.get(url)
    js = response.json()
    for i in js['data']:
        for j in i['categories']:
            for k in j['sub_categories']:
                all_link = ('https://www.thesouledstore.com'+k.get('url_key'))
                print(all_link)
                
                # sub_category(all_link)
list1 = []
def sub_category(url1):
    response = requests.get(url1)
    js = response.json()
    for i in js['data']:
        product = i.get('product')
        price = i.get('price')
        avgRating = i.get('avgRating')
        category = i.get('category')
        images = i.get('images')
        genderType = i.get('genderType')
        jitValue = i.get('jitValue')
        data = {
            'name' : product,
            'rate' : price,
            'avgrating' : avgRating,
            'photo' : images,
            'gentype' : genderType,
            'jit' : jitValue, 
        }
        list1.append(data)
        print(list1)
           

main_category('https://mapi.thesouledstore.com/api/v2/web_menu/webmenu')

