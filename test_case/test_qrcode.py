#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-12-10 11:29
# filename: test_project/test_qrcode

import json
import unittest
from common.http_requests import HttpRequests


class TestQRCode(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.host = 'https://route.showapi.com/'
        cls.http = HttpRequests(cls.host)
        cls.showapi_appid = "467516"
        cls.showapi_sign = "5cd5bb087f864a08b16a3ecb27cf4172"

    @unittest.skip("不执行")
    def test_01_generate(self):
        """生成二维码接口测试"""
        url = '887-1'
        payload = {
            "content": "anne test generate qrcode",
            "size": "5",
            "imgExtName": "png",
            "showapi_appid": TestQRCode.showapi_appid,
            "showapi_sign": TestQRCode.showapi_sign
        }
        res = TestQRCode.http.post(url, payload)
        globals()["imgUrl"] = json.loads(res[1])["showapi_res_body"]["imgUrl"]
        self.assertEqual(0, json.loads(res[1])["showapi_res_code"], "showapi_res_code状态码非0")
        self.assertIn("imgUrl", res[1], "响应中不包含imgUrl字段")

    @unittest.skip("不执行")
    def test_02_get_imgUrl(self):
        """识别二维码图片地址接口测试"""
        url = '887-3'
        payload = {
            "imgUrl": globals()["imgUrl"],
            "showapi_appid": TestQRCode.showapi_appid,
            "showapi_sign": TestQRCode.showapi_sign
        }
        res = TestQRCode.http.post(url, payload)
        self.assertEqual(0, json.loads(res[1])["showapi_res_code"], "showapi_res_code状态码非0")
        self.assertIn("retText", res[1], "响应中不包含retText字段")

    def test_03_get_imgUrl(self):
        """识别二维码文件接口测试"""
        url = '887-2'
        file_path = 'E:\\test\\anne_qrcode.png'
        file = {"img": open("%s" % file_path, 'rb')}
        payload = {
            "img": file,
            "showapi_appid": TestQRCode.showapi_appid,
            "showapi_sign": TestQRCode.showapi_sign
        }
        res = TestQRCode.http.post(url, payload, file)
        self.assertEqual(0, json.loads(res[1])["showapi_res_code"], "showapi_res_code状态码非0")
        self.assertIn("retText", res[1], "响应中不包含retText字段")


if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestQRCode)
    suite = unittest.TestSuite([suite1])
    unittest.TextTestRunner(verbosity=2).run(suite)
