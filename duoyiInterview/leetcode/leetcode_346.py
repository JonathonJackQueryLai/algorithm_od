#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/21 11:23
# @Author  : Jonathon
# @File    : leetcode_346.py
# @Software: PyCharm
# @ Motto : 客又至，当如何
class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for c in s:
            if stack and stack[-1] == 'A' and c == 'B':
                stack.pop()
            elif c == 'D' and stack and stack[-1] == 'C':
                stack.pop()
            else:
                stack.append(c)
        return len(stack)


def makeSmallestPalindrome(s: str) -> str:
    n = len(s)
    l, r = 0, n - 1
    l_li = []
    r_li = []
    while l <= r:
        if l == r:
            l_li.append(s[l])
            break
        if s[l] == s[r]:
            l_li.append(s[l])
            r_li.append(s[r])
            l += 1
            r -= 1
            continue
        else:
            if ord(s[r]) < ord(s[l]):
                l_li.append(s[r])
                r_li.append(s[r])
            else:
                l_li.append(s[l])
                r_li.append(s[l])
            l += 1
            r -= 1
    l_li.extend(r_li[::-1])
    res = ''.join(l_li)
    return res


if __name__ == '__main__':
    print(makeSmallestPalindrome('abcd'))
