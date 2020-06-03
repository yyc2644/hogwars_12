#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 9:51 下午
# @Author  : https://github.com/yyc2644
# @File    : test_work.py
# @Software: PyCharm

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestXueqiu:
    def setup_class(self):
        print("setup")
        desired_caps = {}
        desired_caps['noReset'] = 'true'
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'view.WelcomeActivityAlias'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        print("teardown")
        # self.driver.quit()

    def testSearch(self):
        el1 = self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search")
        el1.click()
        el2 = self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text")
        el2.send_keys("alibaba")
        el3 = self.driver.find_element(MobileBy.XPATH, "//*[@text='阿里巴巴']")
        el3.click()
        el4 = self.driver.find_element(MobileBy.XPATH, "//*[@text='加自选']")
        el4.click()
