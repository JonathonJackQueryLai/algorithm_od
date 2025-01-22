#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/31 22:44
# @Author  : Jonathon
# @File    : sring_49.py
# @Software: PyCharm
# @ Motto : 客又至，当如何

def groupAnagrams(strs: list) -> list:
    res = []

    if strs.__len__() == 1 or strs.__len__() == 0 or all(strs) == False:
        res.append(strs)
        return res
    elif strs:
        n = 0
        l = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        dic = {}

        for i in range(97, 123):
            dic[chr(i)] = l[n]
            n += 1
        l = []
        letters = {}
        dif = set()
        for s in strs:
            total = 1
            for i in s:
                total *= dic[i]
            letters[s] = total
            dif.add(total)
            l.append(letters)

        # for i in dif:
        #     temp = []
        #     for j in l:
        #         if int(j.values()) == i:
        #             temp.appenp(j.keys())
        #             l.remove(j)
        #     res.append(temp)
        left = 0
        dif = list(dif)
        l= l[0]
        l2 = l
        while left <dif.__len__():
            temp = []
            for d in l:


                if l[d] == dif[left]:
                    temp.append(d)

            res.append(temp)
            left += 1


        return res


if __name__ == '__main__':
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
