# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @project_name : DUOyi
# @Time : 2022/1/19
# @description : 


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def func(head: Node):
    curr = head
    pre = None
    while curr:
        next = curr.next
        curr.next = pre
        pre, curr = curr, next

    return pre


def func1(head: Node) -> Node:
    '''
    递归写法
    :param head: 头部
    :return:
    '''



if __name__ == '__main__':
    pass
