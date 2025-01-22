# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @Time :2020/8/6-21:41
# @template :
class Doc(object):
    def __init__(self):
        pass
    @staticmethod
    def run(self):
        dic = {'1': 1}
        li = [dic]
        li1 = li.copy()
        print(li1)

    def __repr__(self):
        return '23'


if __name__ == '__main__':
    my = Doc()
    print(my)
    # my.run()
    # Doc.run()