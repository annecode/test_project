#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne-home
# datetime: 2021-01-04 20:59
# filename: test_project/test_one

import pytest
import requests


@pytest.mark.run_case1
def test_passing():
    """无条件的跳过用例不执行"""
    assert (1, 2, 3) == (1, 2, 3)


@pytest.mark.skip()
def test_failing():
    assert (3, 2, 1) == (1, 2, 3)


def test_001_name():
    name = ['anne', 'yang', 'liao']
    assert 'anne' in name


def test_002_bd():
    r = requests.get('http://www.baidu.com/')
    # print(r.text)
    assert 'baidu' in r.text


if __name__ == '__main__':
    pytest.main(['-v', '-s'])
