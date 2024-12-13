#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-12-10 13:35
# filename: test_project/test

import os
file = {}


class TestFile:

    def addFilePara(self, key, value_url):
        file[key] = open(r"{}".format(value_url), 'rb')
        return self


if __name__ == '__main__':
    f = TestFile()
    r = f.addFilePara("pic", os.path.basename(__file__))
    print(r)  # 返回对象地址
    print(file)
    print(file["pic"])
    print(TestFile.__class__)
    print(TestFile.__class__.__bases__)
