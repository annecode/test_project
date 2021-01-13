#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2021-01-13 15:01
# filename: test_project/test_fixture

import pytest


@pytest.fixture()
def get_list():
    data = [1, 2, 3]
    assert data == [1, 2, 3]  # 若fixture中断言失败，则对应的测试用例也会失败
    return data


@pytest.fixture()
def get_dict():
    user_info = {"name": "anne", "age": 1}
    return user_info


@pytest.fixture()
def call_each(get_list):
    print("======call_each======")
    age = get_list[0]
    return age, get_list


def test_get_list(get_list):
    value = 1
    assert value in get_list


def test_get_dict(get_dict):
    value = 1
    assert get_dict["age"] == value


def test_info(get_list, get_dict):
    print(get_list, get_dict)
    print(type(get_list), type(get_dict))
    assert 1 in get_list
    assert get_dict["name"] == "anne"


def test_call_each(call_each):
    age = call_each[0]
    list0 = call_each[1]
    print(call_each)
    assert age in list0
