#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2021-01-13 19:07
# filename: test_project/conftest

import pytest


@pytest.fixture(scope="session")
def func():
    print("\n=========================in session fixuture before testcase......")
    yield
    print("===========================in session fixture after testcase......")
