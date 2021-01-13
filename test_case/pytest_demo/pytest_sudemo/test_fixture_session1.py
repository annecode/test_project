#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2021-01-13 19:09
# filename: test_project/test_fixture_session1

import pytest


def test_01(func):
    print("in outer class test_01")


def test_02():
    print("in outer class test_02")


class TestExample:
    def test_01(self, func):   # 这个fixture不会执行
        print("in inner class test_01")

    def test_02(self):
        print("in inner class test_02")
