#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-12-03 14:57
# filename: test_project/run_test_class


import unittest
from test_case.test_joke1 import TestApi1
from test_case.test_joke2 import TestApi2
from test_case.test_qrcode import TestQRCode

if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestApi1)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestApi2)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(TestQRCode)
    suite = unittest.TestSuite([suite3])
    unittest.TextTestRunner(verbosity=2).run(suite)
