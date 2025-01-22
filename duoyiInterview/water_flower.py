#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/28 16:41
# @Author  : Jonathon
# @File    : water_flower.py
# @Software: PyCharm
# @ Motto : 客又至，当如何
def func():
    for num in range(100, 1001):
        a, b, c = 0, 0, 0,
        a = num // 100
        b = (num - a * 100) // 10
        c = (num - a * 100 - b * 10)
        if pow(a, 3) + pow(b, 3) + pow(c, 3) == num:
            print(num, end=' ')


if __name__ == '__main__':
    func()
