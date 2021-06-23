#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-12-03 13:59
# filename: test_project/public_method

import logging
import time
import random
import string
import datetime
import json
import re
from collections.abc import MutableMapping

FORMAT = '%(asctime)s--%(levelname)s: %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

class Mapping(MutableMapping):
    def __init__(self, *args, **kwargs):
        self.__dict__.update(*args, **kwargs)

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, key):
        return self.__dict__[key]

    def __delitem__(self, key):
        del self.__dict__[key]

    def __iter__(self):
        return iter(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return '{}, Mapping({})'.format(super(Mapping, self).__repr__(),
                                        self.__dict__)


m = Mapping()

# 装饰器
def log_print(func):
    def wrapper(*params):
        logging.info('-----------------------%s方法开始执行-----------------------' % func.__name__)
        before = time.time()
        result = func(*params)
        logging.info(f'{func.__name__}响应结果：\n{result}')
        after = time.time()
        logging.info(f'{func.__name__}接口耗时%.3f' % (after - before))
    return wrapper

def get_do(input_key):
    output_value = m.get(input_key)
    return output_value

def your_func():
    pass

# 动态传参自定义函数
def map_func(func_name, *args, **kwargs):
    map = {'random_string': get_timestamp,
           'your_func': your_func
           }
    return map[func_name](*args, **kwargs)


# 动态传参
def dynamic_parameter(params):
    params_str = json.dumps(params, ensure_ascii=False)
    if '{{' in params_str:
        key_list = re.findall("{{([^}}]+)", params_str)
        for key in key_list:
            value = get_do(key)
            params_str = params_str.replace('{{' + key + '}}', value)

    if '{%' in params_str:
        func_list = re.findall("{%([^%}]+)", params_str)
        for func in func_list:
            func_name = func.split(' ')[1]

            var_list = func.split(' ')[2: -1]
            value = map_func(func_name, *var_list)
            params_str = params_str.replace('{%' + func + '%}', value)

    return json.loads(params_str)


def random_letter_number(length=10, combination_type=0):
    """
    默认生成10位的混合数字密码
    :param length:返回字符串长度
    :param combination_type:组合方式 0为数字大写字母 1为纯数字 2为纯大写字母 3为大小写数字混合
    :return:随机字符串
    """
    length = int(length)
    com_type = int(combination_type)
    letter_list = []
    number_list = []
    if com_type == 0:
        len_of_letter = random.randint(1, length)
        len_of_number = length - len_of_letter
        for i in range(len_of_letter):
            letter_list.append(random.choice(string.ascii_uppercase))
        for i in range(len_of_number):
            number_list.append(random.choice(string.digits))
        combination_list = letter_list + number_list
        random.shuffle(combination_list)  # 将列表的元素随机排序
        return "".join(combination_list)
    elif com_type == 1:
        for i in range(length):
            number_list.append(random.choice(string.digits))
        return "".join(number_list)
    elif com_type == 2:
        for i in range(length):
            letter_list.append(random.choice(string.ascii_uppercase))
        return "".join(letter_list)
    elif com_type == 3:
        len_of_letter = random.randint(1, length)
        len_of_number = length - len_of_letter
        for i in range(len_of_letter):
            letter_list.append(random.choice(string.ascii_letters))
        for i in range(len_of_number):
            number_list.append(random.choice(string.digits))
        combination_list = letter_list + number_list
        random.shuffle(combination_list)
        return "".join(combination_list)


# 返回2020-07-05 00:00:00，格式化
def time_mktime(flag=None):
    current_time = datetime.datetime.now()
    print(current_time)
    start_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    end_time = (current_time + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
    print(end_time)
    if flag:
        return end_time
    else:
        return start_time

# 生成时间戳，毫秒级
def get_timestamp(length=19):
    timestr_ms = str(round(time.time(), 10**9))[:int(length)]
    return timestr_ms

def get_value_from_json(in_json, target_key, results=None):
    """
    从嵌套字典中获取目标key的值
    :param in_json: 字典
    :param target_key: 目标key
    :param results: 目标key的值
    :return: 目标key的所有值
    """
    if results is None:
        results = []
    if isinstance(in_json, dict):
        for key, value in in_json.items():
            if key == target_key:
                results.append(value)
            else:
                get_value_from_json(value, target_key, results=results)
    elif isinstance(in_json, (list, tuple)):
        for data in in_json:
            get_value_from_json(data, target_key, results=results)
    return results


def get_key(in_json, target_list):
    """
    批量查找目标key对应的值
    :param in_json: 字典
    :param target_list: 目标key列表
    :return: 目标key列表对应的所有值
    """
    result = {}
    for key in target_list:
        result[key] = get_value_from_json(in_json, key)[0]
    return result


if __name__ == '__main__':
    data = {"info": "2 grade",
            "grades": {"xm": [{"chinese": 60}, {"math": 80}, {"english": 100}],
                       "xh": [{"chinese": 90}, {"math": 70}, {"english": 50}],
                       "xl": [{"chinese": '{{hello}}'}, {"math": 80}, {"english": 80}],
                       },
            "newGrades": {"info": "new data",
                          "newChinese": 77
                          }
            }
    # target = "xl"
    # result = get_value_from_json(data, target)
    # print(result)
    # fields = ["xm", "english", "newChinese"]
    # res = get_key(data, fields)
    # print(res)
    # # 使用参数让json数据格式化输出
    # res_final = json.dumps(res, sort_keys=True, indent=4, separators=(',', ':'))
    # print(res_final)
    get_do()
    a = dynamic_parameter(data)
    print(a)
