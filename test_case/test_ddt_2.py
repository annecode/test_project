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
        self.assertTrue(first <= second)

    @data((1, 1), (2, 4))
    @unpack
    def test_factorial(self, data, exceptdata):
        res = data**2
        print(res)
        self.assertEqual(res, exceptdata)

    @data(['anne'], ['hello'])
    @unpack
    def test_str(self, str1):
        print(str1)
        self.assertTrue(str1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
