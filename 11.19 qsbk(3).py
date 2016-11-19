import requests
from bs4 import BeautifulSoup


class QSBK(object):

    def __init__(self):
        self.page = 1
        self.user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (' \
                          'KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36'
        self.headers = {'User-Agent': self.user_agent}
        self.jokes = []
        self.enable = False

    def get_page(self, page):
        url = 'http://www.qiushibaike.com/8hr/page/' + str(page) + '/'
        session = requests.Session()
        html = session.get(url, headers=self.headers).text
        bsObj = BeautifulSoup(html, 'lxml')
        return bsObj

    def get_content(self, page):
        bsObj = self.get_page(page)
        all_jokes = bsObj.findAll('div', {'class': 'article block untagged mb15'})
        full_jokes_info = []
        for joke in all_jokes:
            author = joke.findAll('div', {'class': 'author clearfix'})[0].findAll('h2')[0].get_text()
            text = joke.findAll('div', {'class': 'content'})[0].span.get_text()
            vote_num = joke.findAll('span', {'class': 'stats-vote'})[0].i.get_text()
            comment_num = joke.findAll('span', {'class': 'stats-comments'})[0].i.get_text()
            otherinfo = '{} 好笑 · {} 评论'.format(vote_num, comment_num)
            full_jokes_info.append([author, text, otherinfo])
        return full_jokes_info

    def load_page(self):
        if self.enable is True:
            if len(self.jokes) < 2:
                page_content = self.get_content(self.page)
                if page_content:
                    self.jokes.append(page_content)
                    self.page += 1

    def get_a_joke(self, full_jokes):
        for full_joke in full_jokes:
            next_story = input()
            self.load_page()
            if next_story == 'Q':
                self.enable = False
                return
            print('作者：' + full_joke[0])
            print(full_joke[1])
            print(full_joke[2] + '\n\n')

    def start(self):
        print('正在读取糗事百科,按回车查看新段子，Q退出')
        self.enable = True
        self.load_page()
        while self.enable:
            full_jokes = self.jokes[0]
            self.jokes.pop(0)
            self.get_a_joke(full_jokes)

qsbk = QSBK()
qsbk.start()


