#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 11:33 下午
# @Author  : https://github.com/yyc2644
# @File    : app.py
# @Software: PyCharm
from appium import webdriver

from Daily_Practice.page.base_page import BasePage
from Daily_Practice.page.main import Main


class App(BasePage):
    _package = 'com.xueqiu.android'
    _activity = 'view.WelcomeActivityAlias'

    def start(self):
        if self._driver is None:
            caps = dict()
            caps['platformName'] = 'Android'
            caps['appPackage'] = self._package
            caps['appActivity'] = self._activity
            caps['noReset'] = 'True'
            self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)

        else:
            self._driver.start_activity(self._package,self._activity)

        self._driver.implicitly_wait(10)
        return self

    def main(self) -> Main:
        return Main(self._driver)
