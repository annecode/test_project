#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2021-01-06 16:53
# filename: test_project/test_three

import pytest
import random
import string
from test_case.pytest_demo.mark import *


# 针对模块级别，初始化
def setup_module():
    print('setup_module')


# 针对模块级别，清理环境
def teardown_module():
    print('teardown_module')


# 针对函数级别
def setup_function():
    print('setup_function')


def teardown_function():
    print('teardown_function')


def test_number():
    print('莫须有的数字')
    assert 1 == 1


@pre  # 会作用于类中的所有用例
class TestDemo():
    # 针对类级别
    def setup_class(self):
        print('setup_class')

    def teardown_class(self):
        print('teardown_class')

    # 针对类中的方法级别
    def setup_method(self):
        print('setup_method')

    def teardown_method(self):
        print('teardown_method')

    # 针对用例级别
    def setup(self):
        print('setup')

    def teardown(self):
        print('teardown')

    @test
    def test_01_add(self):
        print('莫须有的加法')
        assert 1 == 1

    @prod
    def test_02_random_number(self):
        number_list = []
        for i in range(10):
            number_list.append(random.choice(string.digits))  # 随机选择数字
            number_list.append(random.choice(string.ascii_lowercase))  # 随机选择小写字母
            number_list.append(random.choice(string.ascii_uppercase))  # 随机选择大写字母
            number_list.append(random.choice(string.ascii_letters))  # 随机选择大小写字母
        number_list = ''.join(number_list)  # 列表转成字符串
        print(number_list)
        assert '8' in number_list


if __name__ == '__main__':
    pytest.main(['-v', '-s'])
