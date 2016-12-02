from http import cookiejar
from urllib.parse import urlencode
from urllib.request import build_opener, HTTPCookieProcessor, urlretrieve
from bs4 import BeautifulSoup
import requests

session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.3'
    '6 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}
url = 'http://jwxt.jnu.edu.cn/'
req = session.get(url, headers=headers)
bsObj = BeautifulSoup(req.text, 'lxml')
captchaUrl = url + bsObj.findAll('img', {'alt': '看不清再换一张'})[0].attrs['src']
# urlretrieve(captchaUrl, '/home/patrick/音乐/Crawler/capt')

hiddens = bsObj.findAll('input', {'type': 'hidden'})
print(hiddens)
values = []
for hidden in hiddens:
    values.append((hidden.attrs['name'], hidden.attrs['value']))
print(values)


passwd = input(u'请手动输入密码\n>')
captcha = input(u'请手动输入验证码\n>')
postdata = urlencode({
    values[0][0]: values[0][1],
    values[1][0]: values[1][1],
    values[2][0]: values[2][1],
    'txtYHBS': '2015053961',
    'txtYHMM': passwd,
    'txtFJM': captcha,
    'btnLogin': '%B5%C7++++%C2%BC'
})
