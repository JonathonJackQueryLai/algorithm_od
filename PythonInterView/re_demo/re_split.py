# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @project_name : DUOyi
# @Time : 2022/2/13
# @description :


def func():
    '''
    正则表达式切片
    :return:
    '''
    string = 'wenjiabao:hello 翻翻的钟'
    import re
    part = re.split(r':| ',string)
    print(part)



if __name__ == '__main__':
    func()
