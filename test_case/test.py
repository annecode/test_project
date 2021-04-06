#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2021-03-05 17:35
# filename: test_project/test

# from functools import reduce
#
# def func1(n):
#     res = 1
#     for i in range(1, n + 1):
#         res = i * res
#     return res
#
# def func2():
#     sum = 0
#     for j in range(1, 4):
#         sum = func1(j) + sum
#     print(sum)
#
# def func3():
#     res = reduce(lambda a, b: a + b, range(1, 5))
#     print(res)
#
# def binary_find(arr, target):
#     l, r = 0, len(arr) - 1
#     while l <= r:
#         mid = (l + r) // 2
#         if arr[mid] < target:
#             l = mid + 1
#         elif arr[mid] > target:
#             r = mid - 1
#         else:
#             return mid
#     return -1
arr = [1, 3, 4, 6, 7]
target = 4
l, r = 0, len(arr) - 1
while l <= r:
    mid = (l + r) // 2
    if arr[mid] < target:
        l = mid + 1
    elif arr[mid] > target:
        r = mid - 1
    else:
        print(mid)
        break

# if __name__ == '__main__':
#     arr = [1, 3, 4, 6, 7]
#     # func2()
#     # func3()
#     res = binary_find(arr, 4)
#     print(res)