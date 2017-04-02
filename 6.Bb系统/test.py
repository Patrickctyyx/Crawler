#! /usr/bin/env python3

from selenium import webdriver
import time
import os

driver = webdriver.Chrome('/home/patrick/Softwares/chromedriver')
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
    time.sleep(3600)
    if len(driver.find_elements_by_xpath(path2)) > homeworklen:
        # send a email
        homeworklen = len(driver.find_elements_by_xpath(path2))




