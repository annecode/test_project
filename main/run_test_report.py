#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-12-17 17:05
# filename: test_project/run_test_report

import os
from _datetime import datetime
import unittest
from BeautifulReport import BeautifulReport


if __name__ == '__main__':
    current_time = datetime.now().strftime('%Y%m%d%H%M%S')
    file_report = '../report/'
    file_case = '../test_case/'
    path = os.path.join(os.path.dirname(file_report), 'beautiful_report')
    if not os.path.exists(path):
        os.mkdir(path)

    suite = unittest.TestSuite()
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestExcelOutput))
    loader = unittest.TestLoader()
    suite.addTests(loader.discover(file_case))
    runner = BeautifulReport(suite)
    runner.report(filename=f'测试报告_{current_time}', description='anne第二份报告', report_dir=path)
