#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-12-04 11:10
# filename: test_project/http_requsts


import requests
import logging


FORMAT = '%(asctime)s--%(levelname)s: %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)


class HttpRequests(object):

    def __init__(self, host):
        self.host = host
        self.req = requests.Session()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }

    @staticmethod
    def k_v(data):
        if isinstance(data, dict):
            str = ''
            for k, v in data.items():
                str += f'{k}={v}&'
            return str[:-1]
        else:
            print('data必须是字典')

    # 将各种请求方法封装
    def api_request(self, method, url, *args):
        map = {
            "Get": self.get,
            "Post": self.post
        }
        api_method = map[method]
        return api_method(url, *args)

    def get(self, url, data=None, headers=None, cookies=None):
        uri = self.host + url
        response = requests.get(uri, params=data, headers=headers, cookies=cookies, verify=False)
        res_time = response.elapsed.total_seconds()
        # result = f'{response.url}接口响应是:\n{response.text}，接口耗时===>>> {res_time}'
        result = f'{response.url}接口耗时===>>> {res_time}'
        logging.info(result)
        return response.status_code, response.text, response.url

    # 封装post请求
    def post(self, url, data=None, body=None, files=None, headers=None, cookies=None):
        uri = self.host + url
        if body == 'json':
            response = requests.post(uri, json=data, files=files, headers=headers, cookies=cookies, verify=False)
        else:
            response = requests.post(uri, data=data, files=files, headers=headers, cookies=cookies, verify=False)
        res_time = response.elapsed.total_seconds()
        api = uri + '?' + self.k_v(data)
        result = f'{api}接口响应是\n:{response.text}接口耗时===>>> {res_time}'
        logging.info(result)
        return response.status_code, response.text, response.url


if __name__ == '__main__':
    url = 'http://route.showapi.com/'
    file = {"img": open("E:\\test\\anne_qrcode.png", 'rb')}
    payload = {
        "img": file,
        "showapi_appid": "467516",
        "showapi_sign": "5cd5bb087f864a08b16a3ecb27cf4172"
    }
    payload1 = {
        "page": "1",
        "maxResult": "2",
        "showapi_appid": "467516",
        "showapi_sign": "5cd5bb087f864a08b16a3ecb27cf4172"
    }
    api = HttpRequests(url)
    api.api_request("Post", "887-2", payload, file)
    api.api_request("Get", "341-1", payload1)
