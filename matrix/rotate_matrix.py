#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Jonathon
# @File    : rotate_matrix.py
# @Time    : 2025/2/10 15:52
# @motto   :  anything you say!


from typing import List

"""
题目:
https://leetcode.com/problems/rotate-image/?envType=problem-list-v2&envId=matrix


[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

逆时针旋转
[
  [7, 4, 1],
  [8, 5, 2],
  [9, 6, 3]
]

"""

"""
顺时针
"""
from typing import List


class Solution:
    def rotate_counterclockwise(self, matrix: List[List[int]]) -> None:
        """
        原地逆时针旋转矩阵 90 度
        """
        n = len(matrix)

        # 1. 转置矩阵（行列互换）
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 2. 反转每一列
        for j in range(n):
            for i in range(n // 2):
                matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return list(map(lambda x: x.reverse(), matrix))
