# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @project_name : DUOyi
# @Time : 2022/1/23
# @description : 循环列表


class Node:
    def __init__(self, val, pre=None, nex=None):
        self.val = val
        self.pre = pre
        self.nex = nex


if __name__ == '__main__':
    root = Node('1')
    root .nex = Node('2')
    root.nex.pre = root