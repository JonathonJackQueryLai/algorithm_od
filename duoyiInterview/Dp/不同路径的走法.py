# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @project_name : DUOyi
# @Time : 2021/12/28
# @description : 

matrix = [[0 for i in range(3)] for i in range(3)]


def uniquePaths1(m: int, n: int) -> int:
    dp = [[0 for col in range(n)] for row in range(m)]
    # 定义边界
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1
    if m < 0 or n < 0:
        return -1
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]


if __name__ == '__main__':
    print(uniquePaths1(3, 7))
