#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/5/9 8:44 下午
# @Author  : https://github.com/yyc2644
# @File    : test_Cal.py
# @Software: PyCharm
'''补全测试用例【 加减乘除】
使用 fixture 装置完成计算机器实例的初始化
改造 pytest 的运行规则 ,测试用例命名以 calc_开始，【加， 减 ，乘，除】分别为 calc_add, calc_sub，…
自动添加标签(add, sub, mul, div四种)，只运行标签为 add 和 div的测试用例。
'''

from python.calculate import Cal
import pytest

class TestCal():

    @pytest.fixture()
    def yc_self(self):
        self.cal = Cal()

    @pytest.mark.parametrize('a, b, c',[(0,0,0),(1,1,2),(-1,1,0),(-1,-1,-2),(0.1,0.1,0.2)])
    def test_add_1(self,yc_self,a,b,c):
        result = self.cal.yc_add(a,b)
        assert result == c

    @pytest.mark.parametrize('a, b, c',[(0,0,0),(1,1,0),(-1,1,-2),(-1,-1,0),(0.1,0.1,0)])
    def test_sub_1(self,yc_self,a,b,c):
        result = self.cal.yc_sub(a,b)
        assert result == c

    @pytest.mark.parametrize('a, b, c', [(0, 0, 0), (1, 1, 1), (-1, 1, -1), (-1, -1, 1), (0.1, 0.1, 0.01)])
    def test_mul_1(self, yc_self, a, b, c):
        result = self.cal.yc_mul(a, b)
        assert result == c

    @pytest.mark.parametrize('a, b, c', [(0, 0, 0), (1, 1, 1), (-1, 1, -1), (-1, -1, 1), (0.1, 0.1,1)])
    def test_div_1(self, yc_self, a, b, c):
        result = self.cal.yc_div(a, b)
        assert result == c

