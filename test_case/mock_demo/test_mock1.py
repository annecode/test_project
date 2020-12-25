#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-12-24 10:53
# filename: test_project/test_mock1

import unittest
from unittest import mock


class Count:
    def add(self, a, b):
        return a + b


class MockDemo(unittest.TestCase):
    def test_001_add(self):
        """mock加法计算方法，return_value返回"""
        count = Count()
        # result1 = count.add(4, 6)
        count.add = mock.Mock(return_value=13)
        result = count.add(4, 6)
        print(result)
        self.assertEqual(13, result)

    def test_002_add(self):
        """mock加法计算方法，side_effect返回"""
        count = Count()
        count.add = mock.Mock(return_value=13, side_effect=count.add)  # side_effect返回值会覆盖return_value的值
        result = count.add(4, 6)
        print(result)
        self.assertEqual(13, result)


if __name__ == '__main__':
    unittest.main()
