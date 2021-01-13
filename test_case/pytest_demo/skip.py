#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2021-01-12 18:39
# filename: test_project/skip

import pytest
import sys

skipif = pytest.mark.skipif(condition=sys.platform.startswith('linux'), reason="linux system can't run")
skip = pytest.mark.skip(reason="本次不执行！")
