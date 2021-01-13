#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2021-01-13 18:40
# filename: test_project/test_fixture_class

import pytest


@pytest.fixture(scope="class")
def func():
    print("\nrun func before run testcase.....")
    yield
    print("run func after run testcase.....")


def test_01(func):
    print("in outer class test_01")


def test_02():
    print("in outer class test_02")


class TestDemo:
    def test_01(self, func):
        print("in inner class test_01")

    def test_02(self):
        print("in inner class test_02")
