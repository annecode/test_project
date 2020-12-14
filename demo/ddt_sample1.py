#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-12-14 14:49
# filename: test_project/ddt_sample1


import ddt
import unittest


@ddt.ddt
class TestAdd(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @ddt.data([1, 2, 3, 6], [2, 3, 4, 6])
    @ddt.unpack
    def test_add(self, data1, data2, data3, exceptdata):
        sum = data1 + data2 + data3
        self.assertEqual(sum, exceptdata)


if __name__ == '__main__':
    unittest.main()
