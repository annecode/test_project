#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne-home
# datetime: 2020-12-14 21:36
# filename: test_project/ddt_excel


import unittest
from ddt import ddt, data
from common.parse_excel import ParseExcel

excelPath = r'../test_data/data_excel.xlsx'
sheetName = 'testcase1'
excel = ParseExcel(excelPath, sheetName)


@ddt
class TestExcelOutput(unittest.TestCase):
    # excel.get_datas_from_sheet()方法返回一个嵌套列表，使用*excel进行解包，得到列表中的每个元素（即子列表-测试用例）
    @data(*excel.get_datas_from_sheet())
    def test_print(self, data):
        """测试excel数据里是否有anne"""
        name, age = data
        print(name, age, data)
        self.assertIn('anne', name)


if __name__ == '__main__':
    unittest.main(verbosity=2)
