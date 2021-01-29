#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2021-01-08 13:49
# filename: test_project/test_leap_year

import pytest


def is_leap_year(year):
    if not isinstance(year, int):
        raise TypeError("not int type")
    if year == 0:
        raise ValueError("must from 1 start")
    if abs(year) != year:
        raise ValueError("can not <0")
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("{} is leap year".format(year))
        return True
    else:
        print("{} is not leap year".format(year))
        return False


class Test_is_leap_year:
    # 在测试类里，使用以下申明，给类下的所有测试方法打上标签
    # pytestmark = pytest.mark.smoke  # 打单个标签
    pytestmark = [pytest.mark.smoke, pytest.mark.pre]  # 打多个标签

    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 重试2次，每次延时3s
    def test_001_exception_error(self):
        with pytest.raises(TypeError):
            print("等待重试1...")
        assert is_leap_year(2019) == True

    def test_002_exception_value(self):
        print("等待重试2...")
        with pytest.raises(ValueError) as exe_info:
            is_leap_year(1)
        assert "must from 1 start" in exe_info.value.args
        assert exe_info.type == ValueError

    def test_003_true(self):
        print("等待重试3...")
        assert is_leap_year(400) == True


if __name__ == '__main__':
    # is_leap_year(1612)
    pytest.main(['./test_leap_year.py', '-v', '--tb=line', '--reruns', '2', '--reruns-delay', '3'])
