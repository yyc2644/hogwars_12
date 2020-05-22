#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/5/21 7:14 下午
# @Author  : https://github.com/yyc2644
# @File    : appium_test1.py
# @Software: PyCharm
from time import sleep
from  appium import webdriver


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.xueqiu.android'
desired_caps['appActivity'] = 'view.WelcomeActivityAlias'
# desired_caps['platformVersion'] = '6.0'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(10)
driver.quit()
