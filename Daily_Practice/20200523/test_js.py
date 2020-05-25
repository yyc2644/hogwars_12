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
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_windows(self):
        # pass
        self.driver.get("https://www.12306.cn/index/")
        self.driver.execute_script(
            "a=document.getElementById('train_date');"
            "a.removeAttribute('readonly');"
            "a.value=20190513")
        time.sleep(5)

        # # self.driver.find_element_by_link_text("登陆").click()
        # self.driver.find_element_by_link_text("登录").click()
        # self.driver.find_element_by_link_text("立即注册").click()
        # windows=self.driver.window_handles
