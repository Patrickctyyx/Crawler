import requests
from bs4 import BeautifulSoup

page = 1
url = 'http://www.qiushibaike.com/8hr/page/' + str(page) + '/'

session = requests.session()
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36'
headers = {'User-Agent': user_agent}

html = session.get(url, headers=headers).text
bsObj = BeautifulSoup(html, 'lxml')

jokes_list = bsObj.findAll('div', {'class': 'article block untagged mb15'})

for joke in jokes_list:
    joke_author = joke.findAll('div', {'class': 'author clearfix'})[0].findAll('h2')[0].get_text()
    joke_text = joke.findAll('div', {'class': 'content'})[0].span.get_text()
    print(joke_author)
    print(joke_text + '\n')

# requests + bs4
# 作者 + 内容
