#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/22 13:56
# @Author  : Jonathon
# @File    : double_link.py
# @Software: PyCharm
# @ Motto : 客又至，当如何

# 可以使用Python实现双向链表，下面是一个简单的实现
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next


if __name__ == '__main__':
    my_link = DoublyLinkedList()
    for i in range(-10,0):
        my_link.prepend(i)
    for i in range(7):

        my_link.append(i)
    my_link.print_list()

