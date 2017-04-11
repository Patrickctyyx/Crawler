#! /usr/bin/env python3

from selenium import webdriver
import time
import os
from mailalert import sendMail


class HomeworkIndicator:

    def __init__(self, urls, names):

        self.driver = webdriver.Chrome('/home/patrick/Softwares/chromedriver')
        self.urls = urls
        self.hw_len = [0 for i in self.urls]
        self.names = names

    def login(self):

        self.driver.get('http://study.jnu.edu.cn')

        name = self.driver.find_element_by_name('user_id')
        paswd = self.driver.find_element_by_name('password')

        name.send_keys(os.environ.get('STUDY_NAME'))
        paswd.send_keys(os.environ.get('STUDY_PASS'))

        path = '//tbody/tr[3]/td[2]/input'
        self.driver.find_element_by_xpath(path).click()

    def start(self):

        self.login()

        path = '//ul/li[@class=\'clearfix read\']'
        i = 0
        for url, hw, name in zip(self.urls, self.hw_len, self.names):
            self.driver.get(url)
            self.hw_len[i] = len(self.driver.find_elements_by_xpath(path))
            i += 1

        while 1:
            i = 0
            for url, hw, name in zip(self.urls, self.hw_len, self.names):
                self.driver.get(url)
                cnt = len(self.driver.find_elements_by_xpath(path))
                if cnt > hw:
                    self.hw_len[i] = cnt
                    body = '【{}】作业有新内容了！'.format(name)
                    print('已发送邮件！')
                    sendMail('作业更新提醒！', body)
                i += 1
                time.sleep(3)
            time.sleep(3600)


if __name__ == '__main__':

    urls = ['http://study.jnu.edu.cn/webapps/blackboard/content/listConte'
            'nt.jsp?course_id=_18789_1&content_id=_340261_1',
            # 'http://study.jnu.edu.cn/webapps/blackboard/content/listConte'
            # 'nt.jsp?course_id=_18755_1&content_id=_192521_1',
            'http://study.jnu.edu.cn/webapps/blackboard/content/listConte'
            'nt.jsp?course_id=_18755_1&content_id=_251306_1']
    names = ['计组', '汇编实验']
    indicator = HomeworkIndicator(urls, names)
    indicator.start()
