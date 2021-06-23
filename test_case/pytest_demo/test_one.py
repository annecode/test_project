#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne-home
# datetime: 2021-01-04 20:59
# filename: test_project/test_one

import pytest
import requests
import time
from test_case.pytest_demo.mark import *
from test_case.pytest_demo.skip import *


@test
@prod
def anne_001_passing():
    """无条件的跳过用例不执行"""
    assert (1, 2, 3) == (1, 2, 3)
    assert {1: 'a', 2: 'b'} == {1: 'a', 2: 'b'}


@skip
def test_002_failing():
    time.sleep(0.1)
    flag = True
    assert flag


def test_003_name():
    pytest.skip("不想执行~~~~~~")
    name = ['anne', 'yang', 'liao']
    time.sleep(1)
    assert 'anne' not in name, 'why not exits'


@test
def test_004_bd():
    r = requests.get('http://www.baidu.com/')
    # print(r.headers)
    # assert 'baidu' not in r.text
    pytest.assume('name' not in r.text, '断言不通过')
    pytest.assume('bp' in r.text, '断言不通过again')


def test_005_zero_divsion():
    # 上下文管理器，代码没有检查到除数为0的异常，断言失败，用例不通过；若检查到异常，则断言通过
    with pytest.raises(ZeroDivisionError):
        pytest.assume(1 / 1)
        # pytest.assume(1 / 0)
        raise ZeroDivisionError("second argument must != 0")


# @pytest.mark.flaky(reruns=2, reruns_delay=2)
def test_006_value_error():
    # 上下文管理器生成一个ExceptionInfo对象，该对象可用于检查捕获的异常的详细信息
    value = 15
    with pytest.raises(ValueError) as exc_info:
        if value > 10:
            raise ValueError(1, "value must be <=10")
    print("||{}===={}===={}".format(exc_info.type, exc_info.value, exc_info.value.args[1]))
    assert exc_info.type is ValueError
    assert exc_info.value.args[1] == "value must be <=10"


if __name__ == '__main__':
    pytest.main(['./test_one.py::anne_001_passing', '-s', '-v'])
