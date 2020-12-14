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
        print(first, second)
        self.assertTrue(first < second)

    @data((1, 1), (2, 4))
    @unpack
    def test_factorial(self, data, exceptdata):
        res = data**2
        self.assertEqual(res, exceptdata)


if __name__ == '__main__':
    unittest.main(verbosity=1)
