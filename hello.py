from requests import Session
from bs4 import BeautifulSoup as BS
import pandas as pd

# The task is to scrape data from the website https://news.ycombinator.com/ and save it in a CSV file. The data should consist of records of random 5 blogs, and have to scrape the following parameters: title, image link, blog link, and the complete content of each blog post. -->
s = Session()
s.headers['user-agent'] ='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'

def crawl(url):
    r = s.get(url)
    soup = BS(r.text,'html.parser')
    title = soup.find('title').text
    if "catskull" in url:
        # print(r.text)
        body = soup.find('article').text.replace('\n',' ')
        imgs = ",".join([i.get('src') for i in soup.find('article').find_all('img')])
    if "arxiv" in url:
        body = soup.find('div',id='content-inner').text.replace('\n',' ')
        imgs = ",".join([i.get('src') for i in soup.find('div',id='content-inner').find_all('img')])
    if "eugeneyan" in url:
        body = soup.find('div','notebody').text.replace('\n',' ')
        imgs = ",".join([i.get('src') for i in soup.find('div','notebody').find_all('img')])
    if "politico" in url:
        body = soup.find('section','media-item media-item--story media-item--story-lead').text.replace('\n',' ')
        imgs = ",".join([i.get('src') for i in soup.find('section','media-item media-item--story media-item--story-lead').find_all('img')])
    if "austinhenley" in url:
        body = soup.find('body').text.replace('\n',' ')
        imgs = imgs = ",".join([i.get('src') for i in soup.find('body').find_all('img')])
    data = {
        "title":title,
        "blog_link":url,
        "image":imgs,
        "body":body
    }
    print(data)
    return data

urls = [
    "https://www.politico.com/news/2023/08/01/fitch-downgrades-u-s-debt-00109288",
    "https://catskull.net/html.html",
    "https://eugeneyan.com/writing/llm-patterns/",
    "https://arxiv.org/abs/2308.00676",
    "https://austinhenley.com/blog/90percent.html"
]

crawl_data = []
for i in urls:
    crawl_data.append(crawl(i))

df = pd.DataFrame(crawl_data)
df.to_csv("info_e_test_output.csv",index=False)