#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-11-27 09:16
# filename: MyPython/run_dir_testcase

import unittest
# import os
# from testclass_1 import TestCalculator1
# from testclass_2 import TestCalculator2

if __name__ == '__main__':
    # 方式一：
    # 实例化测试套件对象
    # suite = unittest.TestSuite()
    # # 1. 实例化TestLoader对象
    # # 2. 使用discover找到一个目录下的所有测试用例
    # loader = unittest.TestLoader()
    # # 3. 使用addTests将找到的测试用例放在测试套件下
    # suite.addTests(loader.discover(os.getcwd()))

    # 方式二：
    test_dir = '../'
    suite = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    # suite.addTests(test_dir)

    # 运行测试套件, stream
    with open('UnittestTxtReport.txt', 'a') as f:
        unittest.TextTestRunner(stream=f, verbosity=2).run(suite)
