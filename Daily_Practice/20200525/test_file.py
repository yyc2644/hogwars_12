#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/5/23 11:16 下午
# @Author  : https://github.com/yyc2644
# @File    : test_js.py
# @Software: PyCharm
import time
from selenium import webdriver


class Testbaidulogin:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_windows(self):
        # pass
        self.driver.get("https://image.baidu.com")
        self.driver.find_element_by_id("sttb").click()
        self.driver.find_element_by_id("stfile").send_keys("/Users/yicheng/Desktop/1.png")
        time.sleep(10)

        # # self.driver.find_element_by_link_text("登陆").click()
        # self.driver.find_element_by_link_text("登录").click()
        # self.driver.find_element_by_link_text("立即注册").click()
        # windows=self.driver.window_handles
