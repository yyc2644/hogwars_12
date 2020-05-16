#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/5/15 11:03 下午
# @Author  : https://github.com/yyc2644
# @File    : normal.py
# @Software: PyCharm
#内置函数的练习

import os
# os.mkdir('text.txt')
print(os.listdir('/'))

import time

print(time.time())
#输出当前时间
# 输出当前日期
# 输出一周前的时间
print("当前时间为",time.strftime("%Y年%m月%d日 %H:%M:%S",time.localtime()))
print("一周前的时间为",time.strftime("%Y年%m月%d日 %H:%M:%S",time.localtime(time.time()-24*60*60*7) ))
