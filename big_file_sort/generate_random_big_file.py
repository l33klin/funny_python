#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Time    : 17/09/2018 9:28 PM
@Author  : Jian
@Contact : jian.li@shopee.com
@Site    : 
@File    : generate_random_big_file.py
"""
import os
import random

_MAX_SEED = 100000000000

_1KB = 1024
_1MB = _1KB * 1024
_1GB = _1MB * 1024


def append_ten_thousand(file_name):

    with open(file_name, 'a') as f:
        for _ in range(10000):
            f.write(str(random.randint(0, _MAX_SEED)) + '\n')


def generate_file(file_name, size=100):

    if not os.path.exists(file_name):
        with open(file_name, 'w') as f:
            pass

    while True:
        if os.path.getsize(file_name) > size:
            break
        else:
            append_ten_thousand(file_name)


if __name__ == '__main__':
    generate_file("100MB_test.data", size=_1MB * 100)
