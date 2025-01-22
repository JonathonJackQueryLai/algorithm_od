#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/1/22 20:10
# @Author  : Jonathon
# @File    : subarray_sum.py
# @Software: PyCharm
# @ Motto : 客又至，当如何

def minSubArrayLen(target: int, nums: list) -> int:
    if sum(nums) < target:
        return 0
    left = 0
    window = []
    min_len = 0
    l = len(nums)
    for r in range(l):
        window.append(nums[r])
        while sum(window) >= target:
            temp = r - left + 1

            min_len = min(min_len, temp) if min_len else temp

            window.remove(nums[left])
            left += 1
    return min_len


if __name__ == '__main__':
    nums = [2, 3, 1, 2, 4, 3]
    print(minSubArrayLen(7, nums))
