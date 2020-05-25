#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 8:12 下午
# @Author  : https://github.com/yyc2644
# @File    : test_base.py
# @Software: PyCharm
from selenium import webdriver


class Base():
    def Setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)

    def Teardown(self):
        self.driver.quit()

