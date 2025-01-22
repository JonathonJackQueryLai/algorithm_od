# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @Time :2021/8/29-23:02
# @template :
class Node(object):
    def __init__(self):
        self.value = None
        self.next = None
        self.precursor = None


class MusicList(object):
    def __init__(self, li):
        pass

    def run(self):
        pass

    def push(self):
        pass

    def pop(self):
        pass

    def index(self):
        pass

def fun():
    n = float(2)
    res = 0
    h6 = float(0)
    for i in range(4):
        h6 = n / 2.0
        res += (n / 2.0)
        n = n/2
    res = 2 * res + 1
    print(res)
    print(h6 / 2)

if __name__ == '__main__':
    li = [i for i in range(4)]
    fun()
