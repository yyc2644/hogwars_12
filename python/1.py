import pytest

class Test_Cal():
    def test_1(self):
        print("开始执行 test1方法")
        x = 'this'
        # assert 'h'in x
        pytest.assume('h'in x)
    def test_2(self):
        print("开始执行 test2方法")
        x ='hello'
        assert 'e' in x
    def test_3(self):
        print("开始执行 test3方法")
        a ='hello'
        b = 'hello wprld'
        assert a in b