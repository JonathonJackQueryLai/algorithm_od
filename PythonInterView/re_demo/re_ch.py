# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @project_name : DUOyi
# @Time : 2022/2/13
# @description :

import re


def func():
    string = 'hello,温家宝1'
    part = re.compile(r'[\u4e00-\u9fa5]+')
    res = part.findall(string)
    print(res)


if __name__ == '__main__':
    func()
