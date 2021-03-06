#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-12-14 15:27
# filename: test_project/ddt_sample_file

import unittest
from ddt import ddt, file_data
from functools import reduce

file = '../../test_data/data.txt'


@ddt
class TestFactorial(unittest.TestCase):

    @file_data(file)
    def test_factorial(self, value):
        """测试从txt文件中读测试数据"""
        data, exceptdata = value.split('-')
        print(data, exceptdata)
        res = reduce(lambda x, y: x*y, range(1, int(data)+1))
        self.assertEqual(res, int(exceptdata))


if __name__ == '__main__':
    unittest.main(verbosity=2)
