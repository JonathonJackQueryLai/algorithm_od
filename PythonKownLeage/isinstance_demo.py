# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @project_name : DUOyi
# @Time : 2022/3/11
# @description :

class A(object):
    pass


class B(A):
    pass


if __name__ == '__main__':
    a = A()
    b = B()
    print(isinstance(a, A))
    print(isinstance(b, A))
    print(type(B), type(A), isinstance(B, A))
    print(isinstance(B, object))
    print(isinstance(A, object))
    print(isinstance(list, list))
