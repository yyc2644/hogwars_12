#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/6/2 10:32 下午
# @Author  : https://github.com/yyc2644
# @File    : test_main.py
# @Software: PyCharm

from Daily_Practice.page.app import App

class TestMain:
    def test_main(self):
        app=App()
        app.start().main().goto_search()