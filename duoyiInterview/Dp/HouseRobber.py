# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @project_name : DUOyi
# @Time : 2021/12/27
# @description : 打家劫舍

# Input: [2,7,9,3,1]


def func(houses: list):
    meno = {}

    # 通过画出来的递归树可以看到sub问题里面存在着 硬币数为负值或者是0的情况
    length = len(houses)
    dp = [0] * (length + 1)
    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])
    for i in range(2, length):
        dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])

    return dp[length - 1]


# leetcode
def rob(nums: list) -> int:
    # 房间对应的金额

    m = len(nums)
    if m == 1:
        return nums[0]
    # dp[i]的含义时当为最大前几家的金额和最大
    dp = [0 for _ in range(m)]
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, m):

        sub = dp[i - 1]
        if sub < 0:
            return -1
        dp[i] = max(sub, dp[i - 2] + nums[i])
        # memo[i] = res
    return dp[m - 1]


def bubble_sort(arr: list):
    length = len(arr)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == '__main__':
    # print(func([2, 7, 9, 3, 1]))
    # print(rob([2, 7, 9, 3, 1]))
    print(bubble_sort([2, 7, 9, 3, 1]))
