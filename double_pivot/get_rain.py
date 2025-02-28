#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Jonathon
# @File    : get_rain.py
# @Time    : 2025/2/19 10:58
# @motto   :  anything you say!
# 输入柱子的高度
nums = input().split()
nums = list(map(lambda x: int(x), nums))

# 初始化左右指针
l, r = 0, len(nums) - 1

# 初始化左右最大高度
left_max, right_max = nums[l], nums[r]

# 初始化接水量
res = 0

# 双指针遍历
while l < r:
    if left_max < right_max:
        l += 1
        # 更新左边最大高度
        left_max = max(left_max, nums[l])
        # 计算接水量
        res += max(0, left_max - nums[l])
    else:
        r -= 1
        # 更新右边最大高度
        right_max = max(right_max, nums[r])
        # 计算接水量
        res += max(0, right_max - nums[r])

print(res)
