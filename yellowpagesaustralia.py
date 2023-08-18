from requests import session
from bs4 import BeautifulSoup as BS
all_data_list = []
import pandas
s = session()
# s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,/;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Referer': 'https://www.yellowpages.com.au./find/lawyers-solicitors/gold-coast-qld/page-1',
    # 'Cookie': 'yellow-guid=b5ad4b2d-c30c-4032-a8d5-217e22f7471f; s_fid=418C66866E6A67DD-3CEBD941E2D3413A; s_cc=true; _vwo_uuid_v2=D0A3A78D8ED4659ACF283515C3464D34C|b969786dab81c947cc43ccd596b782fe; __gsas=ID=2739c7a7d7598c12:T=1685704738:RT=1685704738:S=ALNI_MZrJDqvnzg2VWzsM9caRMup9uYNkg; RT="z=1&dm=www.yellowpages.com.au.&si=993e4631-c0a8-4100-b0c0-1f570fe2247c&ss=liemm4jf&sl=1&tt=5z4&rl=1&ld=6ej&nu=2j8ovhkz&cl=2you&ul=2ypc"; s_sq=telstrassyellowpagesprd%3D%2526c.%2526a.%2526activitymap.%2526page%253DSD%25253ADir%25253AYP%25253ASearch%25253AType%25253ABusiness%252520Listings%2526link%253DNext%2526region%253Droot%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DSD%25253ADir%25253AYP%25253ASearch%25253AType%25253ABusiness%252520Listings%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.yellowpages.com.au.%25252Ffind%25252Flawyers-solicitors%25252Fgold-coast-qld%25252Fpage-2%2526ot%253DA; BVImplmain_site=11347; clue="lawyers solicitors"; locationClue="gold coast qld"',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
}
s.headers.update(headers)
base_url = 'https://www.yellowpages.com.au/find/lawyers-solicitors/gold-coast-qld{}'
# url = 'https://www.yellowpages.com.au./'
import math
list1 = []
def list_links(url2):
    r = s.get(url2)
    soup = BS(r.text,'html.parser')
    total_page = soup.find('div','Box__Div-sc-dws99b-0 zzTlQ').find('p').text.split(' of')[1]
    nop = math.ceil(int(total_page)/35)
    for i in range(1,nop+1):
        r = s.get(url2.format(i))
        soup = BS (r.text,'html.parser')
        product = soup.find_all('div','Box__Div-sc-dws99b-0 iOfhmk MuiPaper-root MuiCard-root PaidListing MuiPaper-elevation1 MuiPaper-rounded')

    # print(product)
        for i in product:
                
                name = i.find('a').find('h3').text
                print(name)
        
                loc = i.find('div','Box__Div-sc-dws99b-0 bKFqNV').find('p')
                if loc:
                    loc = loc.text
                else:
                    loc = "not given"

                time = i.find('div','Box__Div-sc-dws99b-0 QzObd')

                if time:
                    time = time.text
                else:
                    time = "not given"
                
                    
                count = i.find('div','Box__Div-sc-dws99b-0 ypBcE MuiListItem-root')

                if count:
                    count = count.text
                else:
                    count = "not given"
                
                    
                loc = i.find('div','Box__Div-sc-dws99b-0 bKFqNV').find('p')
                if loc:
                    loc = loc.text
                else:
                    loc = "not given"

                time = i.find('div','Box__Div-sc-dws99b-0 QzObd')

                if time:
                    time = time.text
                else:
                    time = "not given"
                    
                        
                count = i.find('div','Box__Div-sc-dws99b-0 ypBcE MuiListItem-root')

                if count:
                    count = count.text
                else:
                    count = "not given"
                    
                ph = i.find('div','Box__Div-sc-dws99b-0 drWGzL')

                if ph:
                    ph = ph.text
                else:
                    ph = "not given"
                    
                item = dict()
                item ['name'] = name
                item ['location'] = loc
                item ['direction'] = count
                item ['phone no'] = ph
                all_data_list.append(item)
        #     print(all_data_list)



                print(all_data_list)




list_links(base_url)
df = pandas.DataFrame(all_data_list)
df.to_excel('australiayelow.xlsx',index=False)