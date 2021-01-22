#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2021-01-22 13:42
# filename: test_project/test_parametrize

import pytest


def str_reverse(s):
    l, r = 0, len(s) - 1
    temp = list(s)
    while l <= r:
        temp[l], temp[r] = temp[r], temp[l]
        l += 1
        r -= 1
    return "".join(temp)


# 多个装饰器，笛卡尔积，当前用例与其他装饰器的每条用例组合执行，本条测试方法共3*3=9条用例
@pytest.mark.parametrize('data1, excepted1', [("hello world", "dlrow olleh"), ("a", "a"), (" anne ", " enna ")])
@pytest.mark.parametrize('data2, excepted2', [("123*345", "543*321"), ("http//", "//ptth"), ("@@@~~~", "~~~@@@")])
def test_str_reverse(data1, data2, excepted1, excepted2):
    res1 = str_reverse(data1)
    res2 = str_reverse(data2)
    assert res1 == excepted1, f"1: {res1}与{excepted1}不一致"
    assert res2 == excepted2, f"2: {res2}与{excepted2}不一致"


@pytest.mark.parametrize('data, excepted', [
    ("123*345", "543*3211"),
    ("http//", "//ptth"),
    ("@@@~~~", "~~~@@@")
])
def test_str_reverse1(data, excepted):
    res = str_reverse(data)
    assert res == excepted, f"3: {res}与{excepted}不一致"


if __name__ == '__main__':
    pytest.main()
