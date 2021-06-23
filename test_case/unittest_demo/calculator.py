#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-11-22 15:01
# filename: MyPython/calculator


class Calculator(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def minus(self):
        return self.a - self.b

    def multi(self):
        return self.a * self.b

    def divsion(self):
        return self.a / self.b

# res = Calculator(10, 5)
# res.add()

