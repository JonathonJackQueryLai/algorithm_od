# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @Time :2021/10/7-17:00
# @template :


def isPalindrome(x: int) -> bool:
    '''
    第一种解法
    :param self:
    :param x:
    :return:
    '''
    # x1 = str(x)[::-1]
    # if x1 == str(x):
    #     return True
    # else:
    #     return False
    '''
    第二种解法
    '''
    # x1 = x  # 做一个备份
    # if x < 0:
    #     return False
    # if x == 0:
    #     return True
    # # 121
    # sum = []
    # while x != 0:
    #     sum.append(x % 10)
    #     x = x // 10
    # temp = 0
    # l = len(sum)
    # for i in sum:
    #     l -= 1
    #     temp += i * pow(10, l)
    # print(temp)
    # if temp == x1:
    #     return True
    # else:
    #     return False

    """
    第三种方法在第二种上进行空间与时间的优化
    在中间停止判断
    """

    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    x1 = 0
    while x > x1:
        x1 = x1 * 10 + x % 10
        x = x // 10
    return x == x1 or x1 == x // 10




    if __name__ == '__main__':
        print(isPalindrome(121))
