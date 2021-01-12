#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne-home
# datetime: 2021-01-04 22:38
# filename: test_project/test_two


import pytest
import sys
from collections import namedtuple
from test_case.pytest_demo.mark import *
from test_case.pytest_demo.skip import *
Task = namedtuple('Task', ['name', 'age', 'sex', 'hobby'])
Task.__new__.__defaults__ = (None, None, False, None)  # 创建默认task对象


@skipif
def test_001_defaults():
    """默认值的校验，如果是linux，就跳过此用例不执行"""
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2


@pytest.mark.xfail(reason='excepted execute failure')
def test_002_access():
    """利用属性名访问对象成员，预期执行失败，实际也执行失败，pytest控制台打印x"""
    t = Task('anne', 19)
    assert t.name == 'anne'
    assert t.age == 18
    assert (t.sex, t.hobby) == (False, None)


@test
@prod
def test_003_asdict():
    """:return 返回一个字典， 预期执行失败，但执行成功，pytest控制台打印X"""
    t_task = Task('tang', 4, 'female', 'play')
    t_dict = t_task._asdict()
    excepted = {
        'name': 'tang',
        'age': 4,
        'sex': 'female',
        'hobby': 'play'
    }
    assert t_dict == excepted


@prod
def test_004_replace():
    """replace()改变数据"""
    t_before = Task('anne', 19, 'female')
    t_after = t_before._replace(age=18, hobby='play')
    t_excepted = Task('anne', 18, 'female', 'play')
    assert t_after == t_excepted
