#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/4 10:41
# @Author  : Jonathon
# @File    : leetcode_348.py
# @Software: PyCharm
# @ Motto : 客又至，当如何

def minimizedStringLength(s: str) -> int:
    s = set(s).__len__()
    return s


def semiOrderedPermutation(nums: list) -> int:
    l = nums.__len__()
    l_i = nums.index(1)
    res = 0
    for i in range(l_i, 0, -1):
        nums[i], nums[i - 1] = nums[i - 1], nums[i]
        res += 1
    r_i = nums.index(l)
    for i in range(r_i, l - 1):
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
        res += 1
    return res


def matrixs(n: int, queries: list) -> int:
    arr = [[0 for j in range(n)] for i in range(n)]
    for nums in queries:
        if nums[0] == 0:
            arr[nums[1]] = [nums[2]] * n
        elif nums[0] == 1:
            for i in range(n):
                arr[i][nums[1]] = nums[2]

    total_sum = sum(sum(arr, []))

    return total_sum


class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        # l1,l2分别储存行列值
        l1 = [0 for _ in range(n)]
        l2 = [0 for _ in range(n)]
        res, s1, s2 = 0, 0, 0
        for i in range(len(queries) - 1, -1, -1):
            #判断是否已经储存值，和应该放入l1还是l2
            if queries[i][0] == 0 and l1[queries[i][1]] == 0:
                l1[queries[i][1]] = queries[i][2]
                #计算当前res
                res += queries[i][2]*(n - s2)
                s1 += 1
            elif queries[i][0] == 1 and l2[queries[i][1]] == 0:
                l2[queries[i][1]] = queries[i][2]
                res += queries[i][2]*(n - s1)
                s2 += 1
        return res



def count1(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
    pass


if __name__ == '__main__':
    # print(minimizedStringLength('aaaddd'))
    # semiOrderedPermutation([1, 3, 4, 2, 5])

    # print(sum([i for i in range(1, 13)]))
    print(matrixs(n=3, queries=[[0, 0, 4], [0, 1, 2], [1, 0, 1], [0, 2, 3], [1, 2, 1]]))
