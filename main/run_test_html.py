#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-12-17 15:13
# filename: test_project/run_test_html

import os
import unittest
from _datetime import datetime
from lib.HTMLTestRunner import HTMLTestRunner


if __name__ == '__main__':
    current_time = datetime.now().strftime('%Y%m%d%H%M%S')
    file_report = '../report/'
    file_case = '../test_case/'
    path = os.path.join(os.path.dirname(file_report), 'html_report')
    if not os.path.exists(path):
        os.mkdir(path)
    filenmae = os.path.join(path, f'result_{current_time}.html')

    suite = unittest.defaultTestLoader.discover(file_case, 'test_*.py')
    with open(filenmae, 'w') as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='<anne>接口-测试报告',
            description='第一份测试报告'
        )
        runner.run(suite)
