#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 11:29 下午
# @Author  : https://github.com/yyc2644
# @File    : testbase.py
# @Software: PyCharm

# class
from time import sleep
from appium import webdriver
from appium.webdriver import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestXueqiu:
    def Setup(self):
        print("setup")
        desired_caps = {}
        desired_caps['noReset'] = 'true'
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'view.WelcomeActivityAlias'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def Teardown(self):
        print("teardown")
        self.driver.quit()

    def testSearch(self):
        el1 = self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search").click()
        el1.click()
        el2 = self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text")
        el2.sendkeys("alibaba")
        el3 = self.driver.find_element(MobileBy.XPATH, "//*[@text='阿里巴巴']")
        el3.click()
        el4 = self.driver.find_element(MobileBy.XPATH, "//*[@text='加自选']")
        el4.click()
