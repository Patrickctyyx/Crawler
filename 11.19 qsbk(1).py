import requests

page = 1
url = 'http://www.qiushibaike.com/8hr/page/' + str(page) + '/'

session = requests.session()
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36'
headers = {'User-Agent': user_agent}

req = session.get(url, headers=headers)
print(req.text)

# 第一点要注意的：伪造请求头

