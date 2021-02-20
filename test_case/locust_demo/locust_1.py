#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2021-02-04 14:04
# filename: test_project/locust_1

from locust import HttpUser, TaskSet, between

def login(req):
    req.client.post()