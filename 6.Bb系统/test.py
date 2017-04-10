#! /usr/bin/env python3

from selenium import webdriver
import time
import os
from mailalert import sendMail

driver = webdriver.PhantomJS('/home/patrick/Softwares/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
# driver = webdriver.Chrome('/home/patrick/Softwares/chromedriver')
driver.get('http://study.jnu.edu.cn')
name = driver.find_element_by_name('user_id')
paswd = driver.find_element_by_name('password')
name.send_keys(os.environ.get('STUDY_NAME'))
paswd.send_keys(os.environ.get('STUDY_PASS'))
path = '//tbody/tr[3]/td[2]/input'
driver.find_element_by_xpath(path).click()

driver.get('http://study.jnu.edu.cn/webapps/blackboard/content/'
           'listContent.jsp?course_id=_18789_1&content_id=_340261_1')

path2 = '//ul/li[@class=\'clearfix read\']'
homeworklen = len(driver.find_elements_by_xpath(path2))
print(homeworklen)

while 1:

    if len(driver.find_elements_by_xpath(path2)) > homeworklen:
        sendMail('作业更新提醒！', '计组作业有新内容了！')
        homeworklen = len(driver.find_elements_by_xpath(path2))
    time.sleep(3600)




