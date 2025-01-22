# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @project_name : DUOyi
# @Time : 2022/2/13
# @description :

# 单例模式
class Single:
    __instance = None

    def __new__(cls, name):
        if not cls.__instance:
            # cls.__instance = object.__new__(cls)
            cls.__instance = super(Single,cls).__new__(cls)
        return cls.__instance


if __name__ == '__main__':
    ming = Single(18)
    xiao = Single(19)
    print(id(ming))
    print(id(xiao))
