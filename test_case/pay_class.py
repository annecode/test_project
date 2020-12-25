#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-12-25 15:21
# filename: test_project/pay_class


class Payment(object):
    def __init__(self, balance, fee, channel):
        self.balance = balance
        self.fee = fee
        self.channel = channel

    def pay(self):
        if self.channel == 'zfb':
            return self.balance + self.fee
        elif self.channel == 'wx':
            return self.balance * (1 + self.fee)
        else:
            return self.balance + 10

    def pay_level(self):
        result = self.pay()
        try:
            if result >= 100:
                return "1-Level"
            elif 50 <= result < 100:
                return "2-Level"
            else:
                return "too low, not enough"
        except:
            return "unkown error"
