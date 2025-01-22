# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @project_name : DUOyi
# @Time : 2022/1/16
# @description : 

def func(target):
    if maxDoubles == 0:
        return target - 1
    if target == 0:
        return -1

    dp = [[0 for i in range(target)] for j in range(maxDoubles)]
    dp[0][0] = 1
    for i in range(1, maxDoubles):
        for j in range(1, target):

            if dp[i][j] == target:
                return i + j
            else:
                dp[i][j] = max(dp[i - 1][j] + 1, dp[i][j - 1] * 2)


if __name__ == '__main__':
    pass
