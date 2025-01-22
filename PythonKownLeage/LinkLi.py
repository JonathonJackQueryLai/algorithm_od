# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @Time :2020/8/7-23:32
# @template :
class item(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class SLinkList(object):
    '''
    静态链表，就是用数组来模拟链表，那么数组的下标就当做是节点的地址，
    这个概念是静态链表的核心
    '''

    def __init__(self, size=100):
        '''
        初始化主要是用于初始化链表的大小，而非创建链表
        '''
        self.link = [item(None) for i in range(size + 1)]  # 申请size大小的节点空间[0,1,2,...,size]，其中下标0的节点作为头结点
        self.link[0].next = None  # 表示空表
        self.link[0].space = 1  # 指向第一个节点，因为初始化时第一个节点为空闲节点

        i = 1
        while i < size:
            self.link[i].next = i + 1  # 利用空闲节点连成一个新的表，并且头结点的space始终指向下一个空闲的节点
            i += 1

        self.link[i].next = None  # 空闲表尾指向None

        self.length = 0  # 链表长度
        self.rear = 0  # 表尾指针


if __name__ == '__main__':
    pass
