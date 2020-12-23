#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-12-22 16:56
# filename: test_project/mock_server

import requests
from unittest import mock


def send_url():
    url = "http://127.0.0.1:7555/"
    return requests.get(url)

response = send_url()
print(response)

# send_url = mock.Mock(return_value='hello world')
# send_url = mock.Mock(return_value={'code': 500, 'code_des': 'server error'})
# send_url = mock.Mock(side_effect=ConnectionError('URL地址不通'))
# send_url = mock.Mock(side_effect=AssertionError('断言异常'))
send_url = mock.Mock(side_effect=[1, 3, 5])
# print(type(send_url), send_url)
# response = send_url()
# print(response)
assert send_url() == 1
assert send_url() == 3
assert send_url() == 5
