#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-12-16 10:04
# filename: test_project/test_ddt_douban

import requests
import unittest
from bs4 import BeautifulSoup as bs
from common.http_requests import HttpRequests
from ddt import ddt, data


def get_urls():
    url_list = []
    host = "https://book.douban.com/"
    url = r"tag/编程?start=20&type=T"
    http = HttpRequests(host)
    result = http.get(url, headers=http.headers)
    html = result[1]
    soup = bs(html, "html.parser")  # 定义一个BeautifulSoup变量
    items = soup.find_all('a', attrs={'class': 'nbg'})
    for i in items:
        idl = i.get('href')
        # id_img = i.img.get('src')
        url_list.append(idl)
    return url_list


@ddt
class TestDoubanApi(unittest.TestCase):

    @data(*get_urls())
    def test_url(self, data):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
        }
        response = requests.get(data, headers=headers)
        res_time = response.elapsed.total_seconds()
        print("{0} 接口响应时间是：{1}".format(data, res_time))
        self.assertEqual(response.status_code, 200, '接口响应不是200')
        self.assertLessEqual(res_time, 1, '接口响应大于1s')


if __name__ == '__main__':
    unittest.main()
