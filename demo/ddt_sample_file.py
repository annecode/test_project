#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-12-14 15:27
# filename: test_project/ddt_sample_file

import unittest
from ddt import ddt, file_data, unpack
from functools import reduce

file = '../test_data/data.txt'


@ddt
class TestFactorial(unittest.TestCase):

    @file_data(file)
    @unpack
    def test_factorial(self, value):
        data, exceptdata = value.split('-')
        print(data, exceptdata)
        res = reduce(lambda x, y: x*y, range(1, int(data)+1))
        self.assertEqual(res, int(exceptdata))


if __name__ == '__main__':
    unittest.main(verbosity=2)
