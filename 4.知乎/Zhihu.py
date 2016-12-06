import requests
from bs4 import BeautifulSoup
import time
from urllib.request import urlretrieve
import os.path

agent = 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
headers = {
    'Host': 'www.zhihu.com',
    'Referer': 'http://www.zhihu.com/',
    'User-Agent': agent
}
session = requests.Session()
req = session.get('https://www.zhihu.com/', headers=headers)
bsObj = BeautifulSoup(req.text, 'lxml')

_xsrf = bsObj.findAll('input', {'name': '_xsrf'})[0].attrs['value']

t = str(int(time.time() * 1000))
captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
pic = session.get(captcha_url, headers=headers)
bsObj2 = BeautifulSoup(pic.text, 'lxml')
print(bsObj2)
