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

    def k_v(self, data):
        """
        将字典里的key和value进行拼接
        :param data: 接口中请求body
        :return: 拼接后的参数串
        """
        if isinstance(data, dict):
            str = ''
            for k, v in data.items():
                str += f'{k}={v}&'
            print(str[:-1])
            return str[:-1]
        else:
            print('data必须是字典')

    # 封装get请求
    def get(self, url, data, headers=None, cookies=None):
        uri = self.host + url
        r = requests.get(uri, params=data, headers=headers, cookies=cookies)
        if r.status_code == 200:
            res_time = r.elapsed.total_seconds()
            result = f'{r.url}接口响应是:\n{r.text}，接口耗时===>>> {res_time}'
            logging.info(result)
            return result
        else:
            print(f'{r.url}无响应！')

    # 封装post请求
    def post(self, url, data, headers=None, cookies=None, body=None):
        uri = self.host + url
        if body == 'form':
            r = requests.post(uri, data=data, headers=headers, cookies=cookies)
        elif body == 'json':
            r = requests.post(uri, json=data, headers=headers, cookies=cookies)
        if r.status_code == 200:
            res_time = r.elapsed.total_seconds()
            result = f'{r.url}接口响应是\n:{r.text}，接口耗时===>>> {res_time}s'
            logging.info(result)
            return result
        else:
            print(f'{r.url}无响应！')


if __name__ == '__main__':
    data = {'name': 'anne', 'age': 20}
    host = 'http://192.168.4.102:21801'
    r = HttpRequests(host)
    print(r.k_v(data))
