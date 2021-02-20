#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2021-02-20 17:11
# filename: test_project/add_order

import json
from common import http_requests
from common.public_method import get_timestamp, time_mktime


class cashinid(object):

    def __init__(self, device_id, msisdn, user_id):
        self.encrptKey = '8VLFNsnn8Ge8F0JD'
        self.host = 'http://cashinidtest.bluepay.asia/cashin/gateway.do'
        self.requests = http_requests.HttpRequests(self.host)
        self.device_id = device_id
        self.msisdn = msisdn
        self.user_id = user_id

    def authcode(self):
        payload = \
            {
                'method': 'bluepay.cashin.authcode',
                'biz_content': '{"user_id": {{user_id}},"terminal_id": {{device_id}}',
                'format': 'JSON',
                'charset': 'utf-8',
                'sign_type': 'md5',
                'timestamp': time_mktime(),
                'version': '1.0',
                'appid': '201706201229',
                'tid': get_timestamp(),
                'sign': '$:md5_cashin'
            }
        res = self.requests.api_request('Post', self.host, payload, 'form')
        globals()['auth_code'] = json.loads(res[1])['auth_code']
        assert res[0] == 200
        assert json.loads(res[1]['sub_code']) == '200'

    def recharge(self):
        payload = \
            {
                'method': 'bluepay.cashin.recharge',
                'biz_content': '{'
                               '"auth_code": {{gloabls()["auth_code"]}}, '
                               '"body": "", '
                               '"extend_params": "", '
                               '"goods_detail": "", '
                               '"phone_num": {{self.msisdn}}, '
                               '"present_code": "", '
                               '"product_id": "BLUEPAY191", '
                               '"scene": "vending_code", '
                               '"scene_type": "1", '
                               '"subject": "充值100000元优惠0元", '
                               '"tcid": {{get_timestamp()}}, '
                               '"terminal_id": {{self.device_id}}, '
                               '"type": "0", '
                               '"user_id": {{self.user_id}} '
                               '}',
                'format': 'JSON',
                'charset': 'utf-8',
                'sign_type': 'md5',
                'timestamp': time_mktime(),
                'version': '1.0',
                'appid': '201706201229',
                'tid': get_timestamp(),
                'sign': '$:md5_cashin'
            }
        biz_content = json.loads(payload['biz_content'])
        auth_code = biz_content['auth_code']
        res = self.requests.api_request('Post', self.host, payload, 'form')
        assert res[0] == 200
        assert json.loads(res[1]['sub_code']) == '200'


if __name__ == '__main__':
    device_id = 'bpinanne01'
    msisdn = '6281700001922'
    user_id = '500005134'
