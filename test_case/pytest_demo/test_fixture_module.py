#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2021-01-13 18:56
# filename: test_project/test_fixture_module

import pytest


@pytest.fixture(scope="module")
def func():
    print("\nin fixture before testcase......")
    yield
    print("in fixture after testcase......")


def test_01():
    print("in outer class test_01")


def test_02():
    print("in outer class test_02")


class TestDemo1:
    def test_01(self, func):
        print("in inner class test_01")

    def test_02(self):
        print("in inner class test_02")


class TestDemo2:
    def test_01(self):
        print("in inner class test_01")

    def test_02(self):
        print("in inner class test_02")