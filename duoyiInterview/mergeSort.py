# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @Time :2020/6/17-22:21
# @template :
def merge(arr, start, end):
    if start < end:
        mid = int((start + end) / 2)
        merge(arr, start, mid)
        merge(arr, mid + 1, end)
        mergeSort(arr, start, mid, end)


def mergeSort():
    resLi = []
    p1, p2 = 0, 0

    lefLi = [2, 4, 6]
    rightLi = [1, 3, 5]
    while (p1 < lefLi.__len__() and p2 < rightLi.__len__()):
        if lefLi[p1] >= rightLi[p2]:

            resLi.append(rightLi[p2])
            p2 += 1
        else:
            resLi.append(lefLi[p1])
            p1 += 1

    if p1 <= lefLi.__len__():
        resLi.extend(lefLi[p1:])
    if p2 <= rightLi.__len__():
        resLi.extend(rightLi[p2:])
    return resLi


def func2(string):
    import re

    n = len(string)
    # dic = {'abc':2, 'def':3, 'ghi':4, 'jkl':5, 'mno':6, 'pqrs':7, 'tuv':8 ,'wxyz':9}
    dic = {}
    letter = [chr(i) for i in range(97, 123)]
    # print(letter)
    for i in letter:
        dic[i] = None
    for i in letter:
        if i in 'wxyz':
            dic[i] = '9'

        elif i in 'tuv':
            dic[i] = '8'
        elif i in 'pqrs':
            dic[i] = '7'

        elif i in 'mno':
            dic[i] = '6'
        elif i in 'jkl':
            dic[i] = '5'
        elif i in 'ghi':
            dic[i] = '4'
        elif i in 'def':
            dic[i] = '3'
        elif i in 'abc':
            dic[i] = '2'
    # print(dic)

    part1 = re.compile(r'[a-z]')
    part2 = re.compile(r'[A-Z]')

    l = 0
    li = list(string)
    while l < n:
        c = li[l]

        if part1.findall(c):
            li[l] = dic[c]
        elif part2.findall(c):
            if c == 'Y':
                li[l] = 'a'
                continue
            temp = ord(c.lower())
            temp += 1
            li[l] = chr(temp)
        l += 1
    print(''.join(li))


if __name__ == '__main__':
    # arr = [4, 5, 1, 2, 3, 3, 7, 6, 8, 9]
    # print(mergeSort())
    # merge(0, arr.__len__())
    # print(arr)
    func2('7Lsu52')