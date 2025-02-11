# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @project_name : DUOyi
# @Time : 2021/12/26
# @description : 凑零钱

# 双函数是为了将num待下去给dp函数 ，因为只是用一个函数的话需要将list写在外面 可读性差，问题来了，dp什么时候需要双参数 什么时候需要一个参数呢？
def func(num, coins: list):
    meno = dict()  # 因为有对应的值，最少的硬币现在的数量的价值

    # 这里的dp含义是dp[n]:当前数值为n的时候 ，所需要最小的硬币数
    def dp(num):
        # 备忘录 n 已经在字典里面的话 ，就不用重复地去计算dp[n]
        if num in meno:
            return meno[num]
        # 通过画出来的递归树可以看到sub问题里面存在着 硬币数为负值或者是0的情况。
        if num == 0:
            return 0
        if num < 0:
            return -1

        # 设置为0的话,min 比较会出错
        res = float('INF')
        for coin in coins:
            # 子问题的含义是 答案 = 前一个子答案加多一个硬币
            sub = dp(num - coin)
            if sub == -1:
                return -1

            res = min(sub + 1, res)
        # 字典
        meno[num] = res
        return meno[num]

    return dp(num)


def coinChange(amount: int, coins: list) -> int:
    n = len(coins)
    dp = [[0 for _ in range(n + 1)] for i in range(amount + 1)]
    # 总数为0的时候
    # base
    if amount == 1:
        dp[0][0] = 1
        return 1
    if amount == 0:
        return 0
    for i in range(1, n):
        dp[0][i] = 0

        # dp[1][1] = 1
    for j in range(1, n):
        for i in range(1, amount):
            # 要不起
            if i < coins[j - 1]:
                dp[i][j] = dp[i][j - 1]
                continue
            dp[i][j] = min(dp[i][j - 1], dp[i - coins[j - 1]][j] + 1)
    return dp[amount][n]


if __name__ == '__main__':
    print(func(3, [2]))
    # print(coinChange(11, [1, 2, 5]))
