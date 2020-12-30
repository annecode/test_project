#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-12-25 09:23
# filename: test_project/test_mock2

import unittest
from unittest import mock
from test_case.pay_class import Payment


class TestPayLevel(unittest.TestCase):
    # 不在同级目录下，要写相对路径，如：路径.模块.类
    @mock.patch("test_case.pay_class.Payment")
    def test_001_wrong(self, mock_Payment):
        """使用装饰器进行mock，路径具体到类名"""
        pay_class = mock_Payment.return_value  # 先返回实例，替换类名称
        pay_class.pay.return_value = 120  # 通过实例调用方法，对方法的返回值进行替换
        res = Payment(70, 0.7, 'wx')  # 实例化待测类
        result = res.pay_level()  # 测试pay_level方法
        print(pay_class.pay(), result)
        self.assertEqual(result, '1-Level')

    # 路径.模块.类.方法
    @mock.patch("test_case.pay_class.Payment.pay")
    def test_002_second_level(self, mock_pay):
        """使用装饰器进行mock，路径具体到方法名"""
        mock_pay.return_value = 60  # 直接模拟类中的方法
        res = Payment(40, 0.5, 'wx')
        result = res.pay_level()
        print(mock_pay(), result)
        self.assertEqual(result, "2-Level")

    @mock.patch.object(Payment, 'pay')
    def test_003_no_level(self, mock_obj1):
        """使用object()方法，直接传类，方法，mock所有类型的对象"""
        mock_obj1.return_value = 20
        payment = Payment(10, 0, 'dana')
        result = payment.pay_level()
        print(mock_obj1(), result)
        self.assertEqual(result, "too low, not enough")

    def test_004_first_level(self):
        """不使用装饰器，使用object()方法"""
        with mock.patch.object(Payment, 'pay') as mock_obj1:
            mock_obj1.return_value = 140
            payment = Payment(50, 10, 'zfb')
            result = payment.pay_level()
            print(mock_obj1(), result)
            self.assertEqual(result, "1-Level")


if __name__ == '__main__':
    unittest.main(verbosity=1)




