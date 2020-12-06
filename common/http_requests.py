#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-12-04 11:10
# filename: test_project/request_method


import requests
import logging

FORMAT = '%(asctime)s--%(levelname)s: %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)


class HttpRequests(object):
    """
封装http请求
    """
    def __init__(self, host):
        self.host = host
        self.req = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
        }

    @staticmethod
    def k_v(data):
        """
拼接请求参数
        :param data: 请求参数
        :return: 拼接后的字符串
        """
        if isinstance(data, dict):
            str = ''
            for k, v in data.items():
                str += f'{k}={v}&'
            return str[:-1]
        else:
            print('data必须是字典')

    def get(self, url, data, headers=None, cookies=None):
        """
封装get请求
        :param url: 请求接口，不包含host
        :param data: 请求参数
        :param headers: headers
        :param cookies: cookies
        :return: 接口响应数据
        """
        uri = self.host + url
        r = requests.get(uri, params=data, headers=headers, cookies=cookies)
        res_time = r.elapsed.total_seconds()
        api = uri + '?' + self.k_v(data)
        result = f'{api}接口响应是:\n{r.text}，接口耗时===>>> {res_time}'
        logging.info(result)
        return r.status_code, r.text, r.url

    # 封装post请求
    def post(self, url, data, headers=None, cookies=None, body=None):
        """
封装post请求
        :param url: 请求接口，不包含host
        :param data: 请求参数
        :param headers: headers
        :param cookies: cookies
        :param body: 请求参数的类型
        :return: 接口响应数据
        """
        uri = self.host + url
        if body == 'form':
            r = requests.post(uri, data=data, headers=headers, cookies=cookies)
        elif body == 'json':
            r = requests.post(uri, json=data, headers=headers, cookies=cookies)
        res_time = r.elapsed.total_seconds()
        api = uri + '?' + self.k_v(data)
        result = f'{api}接口响应是\n:{r.text}接口耗时===>>> {res_time}s'
        logging.info(result)
        return r.status_code, r.text, r.url


if __name__ == '__main__':
    data = {
        "maxResult": "2",
        "page": "1",
        "showapi_appid": "467516",
        "showapi_sign": "5cd5bb087f864a08b16a3ecb27cf4172"
        }
    host = 'https://route.showapi.com'
    r = HttpRequests(host)
    r.post('/341-1', data, body='form')
