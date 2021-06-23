#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: 千泷（杨婷）
# @Email: qianlong.yang@tuya.com
# @Time: 2021-06-09 16:47
# @File: get_email_otp

import time
import requests
import json
import re
import logging

FORMAT = "%(asctime)s--%(levelname)s：%(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)

def get_verification_code(email, count=1):

    url = 'https://www.snapmail.cc/emailList/' + email + f"?count={count}"
    logging.info(f"请求地址：{url}")
    response = requests.get(url)
    if response.status_code == 200:
        email_text = json.loads(response.text)[0]['html']
        validation_code = re.search('<td style=\"font-size:36px;font-weight:800;color: #178BFE;\">([0-9]{6})', email_text)
        if validation_code:
            logging.info(f'【{email}】的验证码：' + validation_code.group(1) + '\n')
        else:
            logging.error("没有获取到验证码！！！")
    else:
        logging.error("接口异常！！！")


if __name__ == '__main__':
    test_email = "work@lista.cc"
    get_verification_code(test_email)
