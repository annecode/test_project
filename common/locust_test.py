#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne-home
# datetime: 2021-01-30 15:38
# filename: test_project/locust_test

from locust import TaskSet, HttpUser, task, between


def about(req):
    req.client.get("/about")
