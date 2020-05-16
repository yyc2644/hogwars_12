#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/5/13 9:34 下午
# @Author  : https://github.com/yyc2644
# @File    : test_read.py
# @Software: PyCharm
#py的读写测试

import json
str='''[{
	"function": "__u",
	"vtp_enableMultiQueryKeys": false,
	"vtp_enableIgnoreEmptyQueryParam": false
}]'''

# print(type(str))
# data = json.loads(str)
# print(type(data))
# print(data)

loadjson=json.load(open('1.json'))
print(loadjson)
print(type(loadjson))



# with open('2.xlsx') as f:
#     while True:
#         line =f.read()
#         if line:
#             print(line)
#         else:
#             break

