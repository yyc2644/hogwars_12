#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/6/2 10:21 下午
# @Author  : https://github.com/yyc2644
# @File    : main.py
# @Software: PyCharm
from Daily_Practice.page.base_page import BasePage
from selenium.webdriver.common.by import By


class Main(BasePage):
    def goto_search(self):
        self.find(By.ID, 'tv_search')
