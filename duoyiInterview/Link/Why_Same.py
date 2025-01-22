#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/5 21:31
# @Author  : Jonathon
# @File    : Why_Same.py
# @Software: PyCharm
# @ Motto : 客又至，当如何
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = l1
    l1.next = ListNode(2)
    while l2:
        print(l2.val)
        l2 = l2.next
