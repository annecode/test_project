#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-12-03 14:57
# filename: test_project/run_test_class


import unittest

if __name__ == '__main__':

    test_dir = '../test_case/'
    suite = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    unittest.TextTestRunner(verbosity=2).run(suite)
