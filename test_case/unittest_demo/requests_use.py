#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-12-02 09:39
# filename: MyPython/requests_user


import time
import logging
import requests
import json
from requests.auth import HTTPBasicAuth


FORMAT = '%(asctime)s--%(levelname)s: %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

def decorator(func):
    def wrapper(*params):
        print('%s方法 is running...' % func.__name__)
        func(*params)
    return wrapper

@decorator
def get(host, url, args=None):
    r = requests.get(host+url, params=args)
    if r.status_code == 200:
        logging.info(r.json())
    else:
        logging.info('接口返回错误')

@decorator
def get_header(host, url, header):
    r = requests.get(host+url, headers=header)
    logging.info(r.text)

# 加代理
@decorator
def get_proxy(host, url, proxy):
    r = requests.get(host+url, proxies=proxy)
    logging.info(r.text)

# 加鉴权
@decorator
def get_auth(host, url):
    r = requests.get(host+url, auth=HTTPBasicAuth('user', 'password'))
    logging.info(r.text)

@decorator
def post_data(host, url, params):
    if isinstance(params, dict):
        data = json.dumps(params)   # 字典转换成json字符串
        r = requests.post(host+url, data=data)
        logging.info(r.text)
    else:
        r = requests.post(host+url, data=params)
        # logging.info(f'{params}不是字典')
        logging.info(r.text)

@decorator
def post_json(host, url, params):
    before = time.time()
    r = requests.post(host+url, data=params, timeout=1)  # 自动转换成json字符串
    after = time.time()
    if r.status_code == 200:
        logging.info(r.text)
        logging.info(f'接口耗时：{after - before}s')
    else:
        r.raise_for_status()

@decorator
def put(host, url, data):
    r = requests.put(host+url, data=data)
    logging.info(r.text)
    print(r.headers, r.cookies.get_dict())  # 获取headers和cookies

@decorator
def delete(host, url, data):
    r = requests.delete(host+url, data=data)
    logging.info(r.content)  # 返回二进制的内容，一般是图片、视频、音频等数据流

def session():
    s = requests.Session()  # 跨请求保持某些参数
    s.get("https://httpbin.org/cookies/set/sessioncookie/anneyang")
    r = s.get("https://httpbin.org/cookies")
    logging.info(r.text)


if __name__ == '__main__':
    host = 'https://httpbin.org/'
    args = {'name': 'anne', 'age': 20, 'attributes': ['eat', 'sing', 'run']}
    args1 = [('key1', 'value1'), ('key2', 'value2')]
    header = {'user_agent': 'my-app/0.0.1'}
    proxies = {'http': 'http://127.0.0.1:8080',
               'https': 'http://127.0.0.1:8080'}

    get(host, 'ip')
    get(host, 'get', args)
    get_header(host, 'get', header)
    # # get_proxy(host, 'get', proxies)
    get_auth(host, 'user')
    post_data(host, 'post', args)
    post_json(host, 'post', args1)
    put(host, 'put', args)
    delete(host, 'delete', args)
    session()