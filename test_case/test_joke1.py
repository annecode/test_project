#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-12-03 11:00
# filename: test_project/test_joke1


import unittest
import requests
from common.public_method import log_print


class TestApi1(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = 'http://route.showapi.com/'

    # @classmethod
    # def tearDownClass(cls):
    #     print('finished!')

    @log_print
    def test_joke(self):
        payload = {
          "page": "1",
          "maxResult": "2",
          "showapi_appid": "467516",
          "showapi_sign": "5cd5bb087f864a08b16a3ecb27cf4172"
        }
        r = requests.post(TestApi1.url + '/341-1', data=payload)
        self.assertEqual(200, r.status_code, '请求返回非200')
        self.assertIn('showapi_res_code', r.text, '响应不包含showapi_res_code')


if __name__ == '__main__':
    unittest.main()
