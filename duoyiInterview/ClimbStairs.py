# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @project_name : DUOyi
# @Time : 2021/12/24
# @description : 爬楼梯

def climbStairs(n: int) -> int:
    if n == 1 or n == 2 or n == 3:
        return n
    else:
        return climbStairs(n - 1) + climbStairs(n - 2)


def climbStairs1(n: int) -> int:
    if n <= 3:
        return n
    dp = [0 for i in range(n)]
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n - 1]

def climbStairs2(n: int) -> int:
    dp = [0 for i in range(n + 1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp


if __name__ == '__main__':
    print(climbStairs1(4))
