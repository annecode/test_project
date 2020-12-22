#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-12-22 16:56
# filename: test_project/mock_server

import requests
from unittest import mock


def send_url():
    url = "http://127.0.0.1:5001/"
    return requests.get(url)


# response = send_url()
# print(response)

# sendUrl = mock.Mock(return_value='hello world')
sendUrl = mock.Mock(return_value={'code': 400, 'code_des': 'api wrong'})
# print(type(sendUrl), sendUrl)
response = sendUrl()
print(response)
