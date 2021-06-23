#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-11-26 18:01
# filename: MyPython/run_class_testcase

import unittest
from test_case.unittest_demo.testclass_1 import TestCalculator1
from test_case.unittest_demo.testclass_2 import TestCalculator2

if __name__ == '__main__':
    # 根据给定的测试类，获取其中所有以“test”开头的测试方法，并返回一个测试套件
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestCalculator1)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestCalculator2)

    # 将多个测试类加载到测试套件中
    # 通过调整suite1和suite2的顺序，可以设定执行顺序
    suite = unittest.TestSuite([suite2, suite1])

    # 执行测试套件
    # unittest.TextTestRunner(verbosity=2).run(suite)
    with open('UnittestTxtReport.txt', 'a') as f:
        unittest.TextTestRunner(stream=f, verbosity=2).run(suite)
