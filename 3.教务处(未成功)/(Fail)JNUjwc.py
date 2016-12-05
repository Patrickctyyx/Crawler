# 没能成功登录，问题暂时没找到，留个坑

from urllib.request import urlretrieve
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


def save_captach():
    captchaUrl = url + bsObj.findAll('img', {'alt': '看不清再换一张'})[0].attrs['src']
    urlretrieve(captchaUrl, '/home/patrick/音乐/Crawler/capt')


def login():
    hiddens = bsObj.findAll('input', {'type': 'hidden'})
    values = []
    for hidden in hiddens:
        values.append((hidden.attrs['name'], hidden.attrs['value']))

    passwd = input(u'请手动输入密码\n>')
    captcha = input(u'请手动输入验证码\n>')

    postdata = {
        values[0][0]: values[0][1],
        values[1][0]: values[1][1],
        values[2][0]: values[2][1],
        'txtYHBS': '2015053961',
        'txtYHMM': passwd,
        'txtFJM': captcha,
        'btnLogin': '登    录'
    }
    # login
    rst = session.post('http://jwxt.jnu.edu.cn/Login.aspx', data=postdata, headers=headers)

    print(rst.text)
    print('POST' + str(rst.status_code))  # 500

    test = session.get(url + 'IndexPage.aspx')
    print(test.text)
    print('GET' + str(test.status_code))

    data = {
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': '/wEPDwUKLTEyOTk3ODU5Mw9kFgICAw9kFgYCAQ9kFg4CBQ8PFgIeB0VuYWJsZWRoZGQCBw8PFgIeB1Rvb2xUaXAFCeWGhe'
                       'aLm+eUn2RkAgkPDxYEHgRUZXh0BQoyMDE1MDUzOTYxHwEFBDIwMTVkZAILDw8WAh8BBQPnp4tkZAINDw8WBB8CBQnnqIvlp'
                       'KnpmLMfAQUY5L+h5oGv56eR5a2m5oqA5pyv5a2m6ZmiZGQCDw8PFgIfAWVkZAIRDw8WBB8CBTHkv6Hmga/np5HlrabmioDm'
                       'nK/lrabpmaIg6K6h566X5py656eR5a2m5LiO5oqA5pyvHwEFGOiuoeeul+acuuenkeWtpuS4juaKgOacr2RkAgMPDxYCHgd'
                       'WaXNpYmxlaGQWAgIDDzwrAA0AZAIFDw8WAh8DaGQWAgIFDzwrAA0AZBgCBQZHVlpIQ0oPZ2QFBkdWTFNDSg9nZNWB6Op6hM'
                       'vjyFmeAEqE/p59m6Q0'
    }
    reqst = session.post('http://jwxt.jnu.edu.cn/Secure/Cjgl/Cjgl_Cjcx_WdCj.aspx', data=data)
    print(reqst.status_code)

    reqst2 = session.get('http://jwxt.jnu.edu.cn/Secure/Cjgl/Cjgl_Cjcx_WdCj.aspx')
    print(reqst2.text)


if __name__ == '__main__':
    save_captach()
    login()
