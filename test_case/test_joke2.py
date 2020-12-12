#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-12-04 16:31
# filename: test_project/test_joke2


import unittest
from common.http_requests import HttpRequests


class TestApi2(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url_index = 'http://route.showapi.com/'
        cls.http = HttpRequests(cls.url_index)
        cls.showapi_appid = "467516"
        cls.showapi_sign = "5cd5bb087f864a08b16a3ecb27cf4172"

    def setUp(self) -> None:
        self.payload = {
            "page": "1",
            "maxResult": "2",
            "showapi_appid": TestApi2.showapi_appid,
            "showapi_sign": TestApi2.showapi_sign
        }

    def test_joke_post(self):
        url = '341-1'
        res = TestApi2.http.post(url, self.payload)
        self.assertEqual(200, res[0], '请求返回非200')
        self.assertIn('showapi_res_code', res[1], '响应不包含showapi_res_code')

    def test_joke_get(self):
        url = '341-1'
        res = TestApi2.http.get(url, self.payload)
        self.assertEqual(200, res[0], '请求返回非200')
        self.assertIn('showapi_res_code', res[1], '响应不包含showapi_res_code')
