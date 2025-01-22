# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @project_name : DUOyi
# @Time : 2022/2/13
# @description :


def func():
    dic = {'a': 1, 'b': 2, 'c': 1}
    # 通过get来获取值
    print(dic.get('a'))

    # print(max(dic,dic.get))
    # li = []

    print(max(dic.keys(), key=dic.get))
    # for i in dic.keys():


if __name__ == '__main__':
    func()
