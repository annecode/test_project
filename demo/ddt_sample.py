#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-12-10 16:35
# filename: test_project/ddt_sample

import unittest
from ddt import ddt, data, unpack


@ddt
class MyTest(unittest.TestCase):
    @data((3, 1), (3, 2), (7, 5), (6, 9))
    @unpack
    def test_values(self, first, second):
        print(first, second)
        self.assertTrue(first > second)


if __name__ == '__main__':
    unittest.main()
