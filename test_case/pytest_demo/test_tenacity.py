#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2021-01-08 18:10
# filename: test_project/test_tenacity

from tenacity import retry, wait_fixed, stop_after_attempt, stop_after_delay
import time


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
    print("等待重试，最大尝试3次，超过后停止...")
    raise Exception


@retry(stop=stop_after_delay(4))
def test_004_retry():
    print("等待重试，最大延迟4s，超过停止...")
    time.sleep(5)
    raise Exception


# &--两者都满足，|--任意种满足
@retry(stop=(stop_after_delay(2) & stop_after_attempt(3)))
def test_005_retry():
    print("等待重试，重试最多5次，每次重试延迟小于10s...")
    time.sleep(4)
    raise Exception


if __name__ == '__main__':
    # test_001_retry()
    # test_002_retry()
    # test_003_retry()
    # test_004_retry()
    test_005_retry()
