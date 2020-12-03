#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-12-03 14:57
# filename: test_project/run_test_class


import unittest
from test_case.test_group import TestGroup


if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestGroup)
    suite = unittest.TestSuite([suite1])
    unittest.TextTestRunner(verbosity=2).run(suite)