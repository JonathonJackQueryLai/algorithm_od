# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @project_name : DUOyi
# @Time : 2022/2/13
# @description :

from json import load, loads, dumps, dump
from json import load


# 将Python 字典转化为json字符串
def dumps_func(dic: dict):
    print(dumps(dic))


# 将Python对象序列为上下文管理器对象
def dump_func(dic: dict):
    dump(dic, open('demo.txt', "w"))
    with open('demo.txt', "r") as  ff:
        print(ff.read())


# 将Python对象序列为json字符串
def load_func(string: str):
    print(dump())


# 将json字符串反序列为 Python对象
def loads_func(string: str):
    print(type(string), loads(string))


# 将文件对象反序列为 Python对象
def load_func():
    with open("demo.txt", mode='r') as f:
        res = load(f)
        print(type(res), res)


if __name__ == '__main__':
    dic = {1: 2}
    string = """
    {
        "4": 5,
        "6": 7
    }
    """
    dump_func({'4': 5, '6': 7})

    dumps_func({'4': 5, '6': 7})
    loads_func(string)
    load_func()
