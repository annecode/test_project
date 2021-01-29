#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2021-01-26 11:04
# filename: test_project/run_test_pytest

import pytest
from datetime import datetime


if __name__ == '__main__':
    current_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    file_path = "../test_case/pytest_demo/"
    report = f"../report/pytest_report/report_{current_time}.html"
    pytest.main([f'{file_path}', '-v', '-s', '--tb=line', f'--html={report}'])
