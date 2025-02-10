#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Jonathon
# @File    : 239._Sliding_Window_Maximum.py
# @Time    : 2025/1/25 17:56
# @motto   :  anything you say!
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        left = 0
        l = len(nums)
        res = []
        first = 1
        temp = float('-inf')
        for right in range(l - k + 1):
            # ?
            if first:
                for i in range(right, right + k):
                    window.append(nums[i])
                first = 0
            else:
                window.append(nums[right + k - 1])
            temp = max(window)
            res.append(temp)
            window.popleft()
        return res


from collections import deque


class Solution1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        l = len(nums)
        res = []
        for right in range(l):
            if window and right - window[0] == k:
                # 插入索引是为了方便维护窗口的大小
                window.popleft()
            while window and nums[window[-1]] < nums[right]:
                window.pop()
            window.append(right)
            if right >= k - 1:
                res.append(nums[window[0]])
        return res


if __name__ == '__main__':
    s1 = Solution1()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(s1.maxSlidingWindow(nums, k))
