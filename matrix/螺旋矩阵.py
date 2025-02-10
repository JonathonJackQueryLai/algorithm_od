#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Jonathon
# @File    : 螺旋矩阵.py
# @Time    : 2025/2/10 15:39
# @motto   :  anything you say!

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        top, bottom = 0, n - 1
        left, right = 0, m - 1
        res = []
        while left <= right and top <= bottom:
            # left -> right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            # top -> bottom
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            #  right -> left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    # print(bottom)
                    res.append(matrix[bottom][i])
                    print(matrix[top][i])
                bottom -= 1

            # bottom -> top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res
