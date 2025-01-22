# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @project_name : DUOyi
# @Time : 2022/1/22
# @description : 


from functools import reduce


def myPow1(x: float, n: int) -> float:
    res = 1
    if n > 0:
        for i in range(n):
            res *= x
    if n == 0:
        return 1
    if n < 0:
        n = int(-n)
        for i in range(n):
            res = x * x
        res = 1.0 / res
        tear = str(res).split('.')[1]
        if tear.__len__() > 5:
            # res = float(str(res)[:7])

            res = round(res, 5)

    return res


# 官方
def myPow( x: float, n: int) -> float:
    def quickMul(N):
        if N == 0:
            return 1.0
        y = quickMul(N // 2)
        return y * y if N % 2 == 0 else y * y * x

    return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)

if __name__ == '__main__':
    # print(myPow(34.00515, -3))
    print(myPow(34.00515, -3))
