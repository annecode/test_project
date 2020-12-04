#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-12-04 16:31
# filename: test_project/test_config


import unittest
from common.http_requests import HttpRequests


class TestDeviceConfig(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.host = 'http://192.168.4.102:21801'

    @classmethod
    def tearDownClass(cls) -> None:
        print('执行完成！')

    def test_skuChange(self):
        params = {'deviceId': '1815', 'name': 'device'}
        url = '/pms/skuChange/autoTest'
        obj = HttpRequests(TestDeviceConfig.host)
        obj.get(url, params)

    def test_getRow(self):
        params = {"deviceCode": "bpanne02", "cardSlot": 20}
        url = '/pms/skuChange/getRow'
        obj = HttpRequests(TestDeviceConfig.host)
        obj.post(url, params, body='form')
