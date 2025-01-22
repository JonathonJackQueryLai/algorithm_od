# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @Time :2020/6/16-21:56
# @template :

# 右移操作是用符号位补位的 正数补0，负数补1
def getMaxNum(a: int, b: int):
    return a - ((a - b) >> 31 & (a - b))


def getMinNum(a: int, b: int):
    return a + ((b - a) >> 31 & (b - a))


if __name__ == '__main__':
    print(getMaxNum(10, 20))
    print(getMinNum(10, 20))
