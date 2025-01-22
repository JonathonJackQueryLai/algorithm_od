#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/30 0:00
# @Author  : Jonathon
# @File    : 123.py
# @Software: PyCharm
# @ Motto : 客又至，当如何
import copy


def back(num, track):
    if num.__len__() == track.__len__():
        t = copy.deepcopy(track)
        res.append(t)
        return
    # for i in range(num.__len__()):
    #     if num[i] in track:
    #         continue
    #     track.append(num[i])
    #     back(num, track)
    #     track.pop()
    for i in num:
        if i in track:
            continue
        track.append(i)
        back(num, track)
        track.pop()


if __name__ == '__main__':
    res = []
    track = []
    num = ['a', 'b', 'c']
    back(num, track)
    print(res)
