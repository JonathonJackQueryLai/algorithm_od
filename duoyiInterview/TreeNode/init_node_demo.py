#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/23 21:05
# @Author  : Jonathon
# @File    : init_node_demo.py
# @Software: PyCharm
# @ Motto : 客又至，当如何
class Node:
    def __init__(self, value=None, next_=None):
        self.value = value
        self.next_ = next_


# n = int(input())
# string = input()
# li = string.split(' ')


def init_node(li):
    head = Node()
    temp = head

    while li:
        temp.next_ = Node(li.pop(0))
        temp = temp.next_
    return head.next_


if __name__ == '__main__':
    head = init_node([i for i in range(5)])
    while head:
        print(head.value)
        head = head.next_
