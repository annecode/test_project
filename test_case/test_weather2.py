#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-12-04 16:31
# filename: test_project/test_config


import unittest
from common.http_requests import HttpRequests


class TestApi2(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = 'http://route.showapi.com'

    @classmethod
    def tearDownClass(cls) -> None:
        print('执行完成！')

    def test_joke_post(self):
        payload = {
          "page": "1",
          "maxResult": "2",
          "showapi_appid": "467516",
          "showapi_sign": "5cd5bb087f864a08b16a3ecb27cf4172"
        }
        url = '/341-1'
        obj = HttpRequests(TestApi2.url)
        res = obj.post(url, payload, body='form')
        self.assertEqual(200, res[0], '请求返回非200')
        self.assertIn('showapi_res_code', res[1], '响应不包含showapi_res_code')

    def test_joke_get(self):
        payload = {
            "page": "2",
            "maxResult": "2",
            "showapi_appid": "467516",
            "showapi_sign": "5cd5bb087f864a08b16a3ecb27cf4172"
        }
        url = '/341-1'
        obj = HttpRequests(TestApi2.url)
        res = obj.get(url, payload)
        self.assertEqual(200, res[0], '请求返回非200')
        self.assertIn('showapi_res_code', res[1], '响应不包含showapi_res_code')
