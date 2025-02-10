#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Jonathon
# @File    : longest_Substring_Without_Repeating_Characters.py
# @Time    : 2025/1/24 14:37
# @motto   :  anything you say!
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         # 初始化滑动窗口的左右边界和最长子串长度
#         left, right, max_length = 0, 0, 0
#
#         # 用于记录字符及其最后出现的位置
#         char_index = {}
#
#         while right < len(s):
#             # 如果当前字符已经在滑动窗口中出现过
#             if s[right] in char_index and char_index[s[right]] >= left:
#                 # 更新左边界为上次出现的位置的下一个位置
#                 left = char_index[s[right]] + 1
#
#             # 更新当前字符最后出现的位置
#             char_index[s[right]] = right
#
#             # 更新最长子串长度
#             max_length = max(max_length, right - left + 1)
#
#             # 移动右边界
#             right += 1
#
#         return max_length


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        l1 = len(set(list(s)))
        if s == " ":
            return 1
        if l1 == l:
            return l
        target, window = {}, {}
        # for i in set(list(s)):
        #     target[i] = target.get(i, 0) + 1
        left = 0
        res = 0
        for right in range(l):
            c = s[right]
            window[c] = window.get(c, 0) + 1
            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] -= 1
            res = max(res, right - left + 1)
        return res


if __name__ == '__main__':
    s = "pwwkew"
    # s = "abcabcbb"
    # s = "a"
    so = Solution()
    print(so.lengthOfLongestSubstring(s))
