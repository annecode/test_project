#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2021-01-13 18:16
# filename: test_project/test_fixture_autouse

import pytest


# yield之前，每条测试用例运行前执行；yield之后，每条测试用例运行后执行
@pytest.fixture(autouse=False)
def func1():
    print("execute func before testcase........")
    yield
    print("execute func after testcase.........")


def test_01(func):
    print("execute test_01")


def test_02():
    print("execute test_02")


def test_03():
    print("execute test_03")
