#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-12-03 11:00
# filename: test_project/test_group


import unittest
import requests

from common.public_method import log_print, random_letter_number, time_mktime


class TestGroup(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url_pdc = 'http://bluepdcidtest.bluepay.asia'
        cls.url_group = 'http://groupbuyidtest.bluepay.asia'

    @classmethod
    def tearDownClass(cls):
        print('finished!')

    @log_print
    def test_commodity_info_list(self):
        """测试commodity/info/list接口"""""
        payload = {
          "queryParam": "10873",
          "pageNumber": "1",
          "pageSize": "50",
          "shelfStatus": "1"
        }
        r = requests.post(TestGroup.url_pdc + '/commodity/info/list', json=payload)
        self.assertEqual(200, r.status_code, '请求返回非200')
        self.assertIn('status', r.text, '响应不包含status')
        return r.json()

    @log_print
    def test_shoppingArea_store(self):
        """测试shoppingArea/store接口"""
        payload = {
          "gpId": "763819,763818,763816",
          "title": f"ANNE-{random_letter_number(4, 1)}",
          "subTitle": f"ANNE-{random_letter_number(4, 0)}",
          "type": "1",  # 1导购区，2新品区
          "sort": "3",
          "picture": "https://bluemart.oss-ap-southeast-1.aliyuncs.com/upload/bluemart/20200702/1593682774284.png",
          "startTime": f"{time_mktime()}",
          "endTime": f"{time_mktime(1)}"
        }
        r = requests.post(TestGroup.url_group + '/groupBuy/banz/shoppingArea/store', json=payload)
        self.assertEqual(200, r.status_code, '请求返回非200')
        print(payload)
        return r.json()


if __name__ == '__main__':
    unittest.main()
