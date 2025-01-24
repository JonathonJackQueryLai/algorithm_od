#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Jonathon
# @File    : bar_foo.py
# @Time    : 2025/1/24 11:00
# @motto   :  anything you say!

# 我的答案 在最后一个testcase里面 s的长度为10000，需要cheat才能过 不然超时 ，答案的长度为5001
class Solution:

    def findSubstring(self, s: str, words: list) -> list:
        right = 0
        target, windows = {}, {}
        # 作为标杆
        for i in words:
            target[i] = target.get(i, 0) + 1
        required = len(words)
        step = len(words[0])
        lst_len = required * step
        l1 = len(s)
        res = []
        if l1 < lst_len:
            return []
        while right < l1:
            cur = right
            # 连续
            for i in range(required):
                temp_str = s[cur:cur + step]
                print(temp_str)
                if temp_str not in target:
                    break
                else:
                    windows[temp_str] = windows.get(temp_str, 0) + 1
                cur += step
            if windows == target:
                res.append(right)
            windows, cur = {}, 0
            right += 1
        return [] if not res else res


#  论坛的答案
#
# class Solution:
#     def findSubstring(self, s: str, words: List[str]) -> List[int]:
#         wordcount = {}
#         for word in words:
#             wordcount[word] = 1 + wordcount.get(word, 0)
#         result = []
#         substringlength = len(words) * len(words[0])
#         for i in range(len(s) - substringlength + 1):
#             substr = s[i:i + substringlength]
#             substrcount = {}
#             for j in range(0, len(substr), len(words[0])):
#                 word = substr[j:j + len(words[0])]
#                 substrcount[word] = 1 + substrcount.get(word, 0)
#             if substrcount == wordcount:
#                 result.append(i)
#         return result





so = Solution()
print(so.findSubstring('lingmindraboofooowingdingbarrwingmonkeypoundcake', ["fooo", "barr", "wing", "ding", "wing"]))
# print(so.findSubstring('wordgoodgoodgoodbestword', ["word", "good", "best", "good"]))
