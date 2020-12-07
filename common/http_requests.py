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

    def __init__(self, host):
        self.host = host
        self.req = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
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

    def get(self, url, data, headers=None, cookies=None):
        uri = self.host + url
        response = requests.get(uri, params=data, headers=headers, cookies=cookies, verify=False)
        res_time = response.elapsed.total_seconds()
        result = f'{response.url}接口响应是:\n{response.text}，接口耗时===>>> {res_time}'
        logging.info(result)
        return response.status_code, response.text,response.url

    # 封装post请求
    def post(self, url, data, headers=None, cookies=None, body=None):
        global response
        uri = self.host + url
        if body == 'form':
            response = requests.post(uri, data=data, headers=headers, cookies=cookies, verify=False)
        elif body == 'json':
            response = requests.post(uri, json=data, headers=headers, cookies=cookies, verrify=False)
        res_time = response.elapsed.total_seconds()
        api = uri + '?' + self.k_v(data)
        result = f'{api}接口响应是\n:{response.text}接口耗时===>>> {res_time}s'
        logging.info(result)
        return response.status_code, response.text, response.url
