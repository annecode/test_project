#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-12-10 17:04
# filename: test_project/parameterized_sample


import unittest
from parameterized import parameterized
from bs4 import BeautifulSoup as bs
from common.http_requests import HttpRequests

list1 = ['anne', 'name', (2,)]


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


class MyTest(unittest.TestCase):

    @parameterized.expand([(3, 1), (1, 0), (2, 1), (4, 3)])
    def test_001_values(self, first, second):
        """测试比大小"""
        print(first, second)
        self.assertTrue(first > second)

    @parameterized.expand(list1)
    def test_002_values(self, value):
        """测试值是否为真"""
        print(value)
        self.assertTrue(value)


if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(MyTest('test_001_values'))
    # suite.addTest(MyTest('test_002_values'))

    suite1 = unittest.TestLoader().loadTestsFromTestCase(MyTest)
    suite = unittest.TestSuite(suite1)
    unittest.TextTestRunner(verbosity=2).run(suite)

