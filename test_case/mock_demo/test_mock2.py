#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-12-25 09:23
# filename: test_project/test_mock2

import unittest
from unittest import mock
from test_case.pay_class import Payment


class TestPayLevel(unittest.TestCase):
    @unittest.skip('不执行')
    def test_001_first_level(self):
        """测试一级水平"""
        payment = Payment(50, 10, 'zfb')
        payment.pay = mock.Mock(return_value=120)
        result = payment.pay_level()
        print(result)
        self.assertEqual(result, "1-Level")

    @unittest.skip('不执行')
    def test_002_second_level(self):
        """测试二级水平"""
        payment = Payment(40, 0.5, 'wx')
        payment.pay = mock.Mock(return_value=60)
        result = payment.pay_level()
        print(result)
        self.assertEqual(result, "2-Level")

    @unittest.skip('不执行')
    def test_003_no_level(self):
        """测试其他水平"""
        payment = Payment(10, 0, 'dana')
        payment.pay = mock.Mock(side_effect=payment.pay)
        result = payment.pay_level()
        print(result)
        self.assertEqual(result, "too low, not enough")

    @mock.patch("test_case.pay_class.Payment")
    def test_004_wrong(self, mock_Payment):
        """使用装饰器进行mock"""
        pay_class = mock_Payment.return_value
        pay_class.pay.return_value = 120
        res = Payment(70, 0.7, 'wx')
        result = res.pay_level()
        print(pay_class.pay(), result)
        self.assertEqual(result, '1-Level')


if __name__ == '__main__':
    unittest.main()




