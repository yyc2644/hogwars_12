#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/5/11 10:30 下午
# @Author  : https://github.com/yyc2644
# @File    : conftest.py.py
# @Software: PyCharm
import pytest

def pytest_collection_modifyitems(session, config, items:list):
#     # print(items)
#     # print(type(items))
    for item in items:
        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)
        elif 'div' in item.nodeid:
            item.add_marker(pytest.mark.div)