#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Jonathon
# @File    : longset_palindrome_stirng.py
# @Time    : 2025/2/28 13:53
# @motto   :  anything you say!
from typing import List


class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, max_len = 0, 1
        n = len(s)
        if n < 2:
            return s

        def expand(l, r):
            nonlocal start, max_len
            while l >= 0 and r < n and s[l] == s[r]: # 一开始 锚点的时候相同才开始进入while循环，这个循环是保持接下来的回文字母是相同的
                # max_len,start  = r-l +1,l if r-l +1 > max_len else max_len
                if r - l + 1 > max_len:
                    start = l
                    max_len = r - l + 1
                l -= 1
                r += 1

        for i in range(n):
            print(i)
            # 一定要每人走一步所以。。
            expand(i, i)
            expand(i, i + 1)

        return s[start: start + max_len]


if __name__ == '__main__':
    s = Solution()
    s.longestPalindrome("dcbabad")
