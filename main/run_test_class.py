#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-12-03 14:57
# filename: test_project/run_test_class


import unittest
from test_case.test_weather1 import TestApi1
from test_case.test_weather2 import TestApi2


if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestApi1)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestApi2)
    suite = unittest.TestSuite([suite2])
    unittest.TextTestRunner(verbosity=1).run(suite)
