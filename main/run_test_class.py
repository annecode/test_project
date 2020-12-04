#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-12-03 14:57
# filename: test_project/run_test_class


import unittest
from test_case.test_group import TestGroup
from test_case.test_config import TestDeviceConfig


if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestGroup)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestDeviceConfig)
    suite = unittest.TestSuite([suite2])
    unittest.TextTestRunner(verbosity=2).run(suite)
