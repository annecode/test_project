#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2021-01-13 18:24
# filename: test_project/test_fixture_function

import pytest


@pytest.fixture()
def func1():
    print("\nrun func1 before execute testcase.....")
    yield
    print("run func1 after execute testcase......")


@pytest.fixture(scope="function")
def func2():
    print("\nrun func2 before execute testcase......")
    yield
    print("run func2 after execute testcase......")


def test_01(func1):
    print("run test_01 in outer class")


def test_02(func2):
    print("run test_02 in outer class")


def test_03():
    print("run test_03 in outer class")


class TestDemo:
    def test_01(self, func1):
        print("run test_01 in inner class")

    def test_02(self, func2):
        print("run test_02 in inner class")

    def test_03(self):
        print("run test_03 in inner class")
