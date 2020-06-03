#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 11:19 下午
# @Author  : https://github.com/yyc2644
# @File    : base_page.py
# @Software: PyCharm

from appium.webdriver.webdriver import WebDriver


class BasePage:
    _driver: WebDriver

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value):
        self._driver.find_element(locator, value).cl
