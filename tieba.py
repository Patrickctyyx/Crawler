from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import re


class Tieba(object):

    def __init__(self):
        self.baseURL = 'http://tieba.baidu.com'
        self.targetTieba = '/f?kw=%E5%A5%B3%E7%A5%9E'
        self.pagestr = '&ie=utf-8&pn='
        self.page = 0
        self.maxpage = 5
        self.allURLs = []

    def getBSobj(self, url):
        html = urlopen(url)
        bsObj = BeautifulSoup(html, 'lxml')
        return bsObj

    def getAllUrls(self):
        url = self.baseURL + self.targetTieba + self.pagestr + str(self.page * 50)
        bsObj = self.getBSobj(url)
        links = bsObj.findAll('a')
        for link in links:
            try:
                prelink = link.attrs['href']
                if re.match(r'/p/\d{10}', prelink):
                    link = self.baseURL + re.match(r'/p/\d{10}', prelink).group() + '?see_lz=1'
                    self.allURLs.append(link)
            except KeyError as e:
                pass

    def savePics(self, url):
        bsObj = self.getBSobj(url)
        allPics = bsObj.findAll('img', {'class': 'BDE_Image'})
        for src in allPics:
            img = src.attrs['src']
            dir = 'pics/' + str(img)[-10:]
            urlretrieve(img, dir)
            print('Download successfully!')

    def start(self):
        while self.page < self.maxpage:
            self.getAllUrls()
            print(self.allURLs)
            for url in self.allURLs:
                self.savePics(url)
            self.page += 1
            self.allURLs = []


if __name__ == '__main__':
    tieba = Tieba()
    tieba.start()

