#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/15 21:08
# @Author  : Jonathon
# @File    : avl_tree.py
# @Software: PyCharm
# @ Motto : 客又至，当如何
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        node = Node(key)
        if self.root is None:
            self.root = node
        else:
            current = self.root
            while current is not None:
                if key < current.key:
                    if current.left is None:
                        current.left = node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = node
                        break
                    else:
                        current = current.right
        self.update_height(node)
        self.rebalance(node)

    def update_height(self, node):
        if node.left is None and node.right is None:
            node.height = 1
        elif node.left is None:
            node.height = node.right.height + 1
        elif node.right is None:
            node.height = node.left.height + 1
        else:
            node.height = max(node.left.height, node.right.height) + 1

    def rebalance(self, node):
        while node is not None:
            self.update_height(node)
            balance = self.get_balance(node)
            if balance > 1 and self.get_balance(node.left) >= 0:
                self.right_rotate(node)
            elif balance < -1 and self.get_balance(node.right) <= 0:
                self.left_rotate(node)
            elif balance > 1 and self.get_balance(node.left) < 0:
                self.left_rotate(node.left)
                self.right_rotate(node)
            elif balance < -1 and self.get_balance(node.right) > 0:
                self.right_rotate(node.right)
                self.left_rotate(node)
            node = node.parent

    def get_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def left_rotate(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left is not None:
            right_child.left.parent = node
        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def right_rotate(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right is not None:
            left_child.right.parent = node
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child
