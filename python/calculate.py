#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/5/9 8:28 下午
# @Author  : https://github.com/yyc2644
# @File    : calculate.py
# @Software: PyCharm

class Cal:
    def yc_add(self, a, b):
        return a + b

    def yc_sub(self, a, b):
        return a - b

    def yc_div(self, a, b):
        if b==0:
            print("分母不能为0")
        else:
            return a / b

    def yc_mul(self, a, b):
        return a * b

    def yc_pow(self, a, b):
        for i in b:
            a = a * a
        return a

    def yc_abs(self, a):
        a = abs(a)
        return a
