#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 11:56 上午
# @Author  : https://github.com/yyc2644
# @File    : sele.py
# @Software: PyCharm

import selenium
from selenium import webdriver
from time import sleep
# Chromedriver文件放在/usr/local/bin中，不需要配再单独配置环境变量了
from selenium.webdriver import ActionChains


class TestSelenium:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_link(self):
        # self.driver.get("https://nga.178.com/thread.php?fid=540")
        self.driver.get("https://home.testing-studio.com")
        # 定位练习--找到某个字段的n种方式
        test1 = self.driver.find_element_by_xpath('//*[@id="pagebtop"]//td[3]')
        print("test1=", test1.text)
        test2 = self.driver.find_element_by_xpath('//*[@id="pagebtop"]//td[last(5)]')
        print("test2=", test2.text)


class TestSelenium2:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_content(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click=self.driver.find_element_by_xpath("/html/body/form/input[3]")
        element_click2=self.driver.find_element_by_xpath("//input[@value='click me']")
        element_doubleclick=self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        element_righteclick=self.driver.find_element_by_xpath("//input[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(element_click)
        action.click(element_click2)
        action.double_click(element_doubleclick)
        action.context_click(element_righteclick)
        action.perform()
        sleep(3)





