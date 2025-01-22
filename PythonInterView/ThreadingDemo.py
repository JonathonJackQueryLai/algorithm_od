# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @project_name : DUOyi
# @Time : 2022/2/13
# @description :

import threading


def merge(array, start, mid, end):
    res = []
    mid = (start + end) // 2
    p1 = start
    p2 = mid +1
    while start <= mid and p2 <= end:
        if array[p1] <= array[p2]:
            res.append(array[p1])
            p1 += 1
        else:
            res.append(array[p2])
            p2 += 1

    if p1 <= mid:
        res.extend(array[p1:mid])

    if p2 <= end:
        res.extend(array[p2:])
    return res


def mergeSort(arr, l, r):
    if l < r:
        m = (l + r) // 2

        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


if __name__ == '__main__':
    import random

    array = [random.randint(1, 1000) for i in range(5)]
    # 属于原地排队 直接
    mergeSort(array, 0, array.__len__() - 1)
    # sortf(array, 0, array.__len__() - 1)
    print(array)
