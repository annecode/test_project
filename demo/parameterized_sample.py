#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-12-10 17:04
# filename: test_project/parameterized_sample


import unittest
from parameterized import parameterized


class MyTest(unittest.TestCase):
    @parameterized.expand([(3, 1), (1, 0), (4, 3)])
    def test_values(self, first, second):
        print(first, second)
        self.assertTrue(first > second)


if __name__ == '__main__':
    unittest.main(verbosity=2)
