#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 8:09 下午
# @Author  : https://github.com/yyc2644
# @File    : test_windows.py
# @Software: PyCharm

from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Testbaidulogin:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_windows(self):
        self.driver.get("https://www.baidu.com/")
        # self.driver.find_element_by_link_text("登陆").click()
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_link_text("立即注册").click()
        windows=self.driver.window_handles
        #切换窗口
        self.driver.switch_to.window(windows[-1])
        self.driver.find_element(By.XPATH,"//*[@id='TANGRAM__PSP_4__userName']").send_keys("qwer1234")
        self.driver.find_element(By.XPATH,"//*[@id='TANGRAM__PSP_4__phone']").send_keys("13800138000")
        self.driver.find_element(By.XPATH,"//*[@id='TANGRAM__PSP_4__password']").send_keys("qwer1234")
        self.driver.find_element(By.XPATH,"//*[@id='TANGRAM__PSP_4__verifyCodeSend']").click()

        #切换回原来的窗口
        self.driver.switch_to.window(windows[0])

        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys()
        sleep(5)

class TestAllbrowser:
    def setup(self):
        pass
    def teardown(self):
        pass
    def test_browser(self):
        self.chrome=webdriver.Chrome()
        self.firefox=webdriver.Firefox()







