#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-11-22 14:50
# filename: MyPython/testclass_1

import unittest
from .calculator import Calculator


# 定义测试类，父类为unittest.TestCase
class TestCalculator1(unittest.TestCase):

    # 定义setUp()方法用于测试用例执行的初始化工作
    # 所有类中方法的入参是self，定义方法的变量也要"self.变量"
    def setUp(self):
        # print('TestCalculator1 test start...')
        self.result = Calculator(10, 5)   # 类实例化

    # 定义测试用例，以"test_"开头命名的方法，方法的入参为self
    # 可使用unittest.TestCase类下面的各种断言方法对测试结果进行判断
    # 可定义多个测试用例
    def test_001_add(self):
        """Test method add(a, b)"""
        self.assertEqual(self.result.add(), 15, "计算错误！")

    def test_002_minus(self):
        """Test method minus(a, b)"""
        self.assertEqual(self.result.minus(), 5, "计算错误")

    def test_003_multi(self):
        """Test method multi(a, b)"""
        self.assertEqual(self.result.multi(), 50, "计算错误")

    def test_004_divsion(self):
        """Test method divsion(a, b)"""
        self.assertEqual(self.result.divsion(), 2, "计算错误")

    # 定义teardown()方法用于测试用例执行后的善后工作
    def teardown(self):
        pass


if __name__ == '__main__':
    # unittest.main()方法会搜索该模块下所有test开头的测试用例方法，并自动执行他们，verbosity打印信息等级，越大越详细
    # unittest.main(verbosity=1)

    # 构造测试集，类实例化
    suite = unittest.TestSuite()

    # 将用例添加到测试套件的方法：第一种写法
    # suite.addTest(TestCalculator1('test_004_divsion'))
    # suite.addTest(TestCalculator1('test_002_minus'))
    # suite.addTest(TestCalculator1('test_003_multi'))
    # suite.addTest(TestCalculator1('test_001_add'))

    # 第二种写法
    tests = [TestCalculator1('test_001_add'), TestCalculator1('test_002_minus'), TestCalculator1('test_003_multi'), TestCalculator1('test_004_divsion')]
    suite.addTests(tests)

    # 执行测试集合
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
