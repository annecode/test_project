#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-12-10 16:35
# filename: test_project/ddt_sample

import unittest
from ddt import ddt, data, unpack


@ddt
class MyTest(unittest.TestCase):
    @data((1, 1), (2, 4))
    @unpack
    def test_values(self, first, second):
        """测试两个数的大小"""
        self.assertTrue(first <= second)

    @data((1, 1), (3, 4))
    @unpack
    def test_factorial(self, data, exceptdata):
        """测试阶乘"""
        res = data**2
        print(res)
        self.assertEqual(res, exceptdata)

    @data(['anne'], ['hello'])
    @unpack
    def test_str(self, str1):
        """测试字符串传参"""
        print(str1)
        self.assertTrue(str1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
