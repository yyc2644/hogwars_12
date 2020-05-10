#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/5/9 9:22 下午
# @Author  : https://github.com/yyc2644
# @File    : test_pytest.py
# @Software: PyCharm
from python.calculate import Cal
import pytest


@pytest.fixture()
def check():
    print("这里时fixture")

def daying(check):
    print("打印字符串")


class TestCal:

    def test_add(self):
        self.cal = Cal()
        result = self.cal.yc_add(1, 2)
        print(result)
        assert 3==result
