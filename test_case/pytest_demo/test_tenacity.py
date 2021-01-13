#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2021-01-08 18:10
# filename: test_project/test_tenacity

import time
from tenacity import retry, wait_fixed, stop_after_attempt, stop_after_delay



@retry
def test_001_retry():
    print("等待重试，重试无间隔执行...")
    raise Exception


@retry(wait=wait_fixed(2))
def test_002_retry():
    print("等待重试，固定间隔2s...")
    raise Exception


@retry(stop=stop_after_attempt(3))
def test_003_retry():
    print("等待重试，上次总共尝试次数>=3，停止...")
    raise Exception


@retry(stop=stop_after_delay(4))
def test_004_retry():
    print("等待重试，从第1次尝试开始，累积用时>=4s，停止...")
    time.sleep(3)
    raise Exception


# &：2个条件都满足才会停止
# |：任何一个满足都会停止
@retry(stop=(stop_after_delay(5) & stop_after_attempt(3)))
def test_005_retry():
    print("等待重试，从第一次尝试开始，累积用时>=5s，停止...")
    # print("等待重试，判断上次总共尝试次数>=3，停止...")
    time.sleep(1)
    raise Exception


if __name__ == '__main__':
    # test_001_retry()
    # test_002_retry()
    # test_003_retry()
    # test_004_retry()
    test_005_retry()
