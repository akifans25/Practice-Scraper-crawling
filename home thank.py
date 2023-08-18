# from requests import session
# from bs4 import BeautifulSoup as BS
# list1=[]
# s=session()
# s.headers['user-agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0'
# url='https://www.homethangs.com/bathroom-faucets-357.html'
# r=s.get(url)
# soup=BS(r.text,'html.parser')

# def nextcrawl(url,page):
#     r=s.get(url)
#     soup=BS(r.text,'html.parser')
#     products=soup.find_all('table','categoryitem')
#     if products:

#         for i in soup.find_all('table','categoryitem'):
#             name=i.find('td','pother').text
#             price=i.find('b').text.strip()
#             details=i.find('p','h1-link').text
#             image=i.find('a').find('img').get('src')
#             item=dict()
#             item['title']=name
#             item['price']=price
#             item['details']=details
#             item['img']=image
#             list1.append(item)
#             print(list1)


#         page+=1
#         next_pages_url = "{}&page={}".format(url,page)
#         nextcrawl(next_pages_url,page)
# nextcrawl(url,page=1)