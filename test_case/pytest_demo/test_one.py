#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne-home
# datetime: 2021-01-04 20:59
# filename: test_project/test_one

import pytest
import sys
from collections import namedtuple
Task = namedtuple('Task', ['name', 'age', 'sex', 'hobby'])
Task.__new__.__defaults__ = (None, None, False, None)  # 创建默认task对象


@pytest.mark.run_case1
def test_passing():
    """无条件的跳过用例不执行"""
    assert (1, 2, 3) == (1, 2, 3)


@pytest.mark.skip()
def test_failing():
    assert (3, 2, 1) == (1, 2, 3)
