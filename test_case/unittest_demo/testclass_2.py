#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-11-26 18:05
# filename: MyPython/testclass_2

import sys
import unittest
from calculator import Calculator


class TestCalculator2(unittest.TestCase):

    def setUp(self):
        self.result = Calculator(10, 5)   # 类实例化

    @unittest.skip('不执行加法用例')
    def test_001_add(self):
        """Test method add(a, b)"""
        self.assertEqual(self.result.add(), 15, "计算错误！")

    # 除非条件为真：是linux系统，否则都跳过
    @unittest.skipUnless(sys.platform.startswith('linux'), 'linux系统才可执行')
    def test_002_minus(self):
        """Test method minus(a, b)"""
        self.assertEqual(self.result.minus(), 5, "计算错误")

    @unittest.expectedFailure  # 让此用例执行失败
    def test_003_multi(self):
        """Test method multi(a, b)"""
        # self.skipTest('不允许这个方法')
        self.assertEqual(self.result.multi(), 50, "计算错误")

    @unittest.skipIf(sys.platform.startswith('win32'), 'windows系统不可执行')
    def test_004_divsion(self):
        """Test method divsion(a, b)"""
        self.assertEqual(self.result.divsion(), 3, "计算错误")

    def teardown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print('\n仅测试套件前执行一次。')

    @classmethod
    def tearDownClass(cls):
        print('\n仅测试套件后执行一次')


if __name__ == '__main__':
    # unittest.main(verbosity=2)
    suite = unittest.TestSuite()
    suite.addTest(TestCalculator2('test_001_add'))
    suite.addTest(TestCalculator2('test_002_minus'))
    suite.addTest(TestCalculator2('test_003_multi'))
    suite.addTest(TestCalculator2('test_004_divsion'))
    with open('UnittestTxtReport.txt', 'a') as f:
        unittest.TextTestRunner(stream=f, verbosity=2).run(suite)
