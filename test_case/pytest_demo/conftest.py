#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2021-01-13 19:07
# filename: test_project/conftest

import pytest


@pytest.fixture(scope="session")
def func():
    print("\nin session fixuture before testcase......")
    yield
    print("\nin session fixture after testcase......")
