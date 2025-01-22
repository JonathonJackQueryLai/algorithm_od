import random


def merge(array, start, mid, end):
    res = []
    left1 = start
    left2 = mid + 1
    while left1 <= mid and left2 <= end:
        if array[left1] <= array[left2]:
            res.append(array[left1])
            left1 += 1
        else:
            res.append(array[left2])
            left2 += 1
    if left1 <= mid:
        res.extend(array[left1:mid + 1])
    if left2 <= end:
        res.extend(array[left2:end + 1])
    for i in range(res.__len__()):
        array[start + i] = res[i]


def mergeSort(array, start, end):
    if start >= end:
        return
    mid = (start + end) // 2
    mergeSort(array, start, mid)
    mergeSort(array, mid + 1, end)
    merge(array, start, mid, end)


if __name__ == '__main__':
    l = [1, 5, 7, 2, 3, 6, 9, 4]
    start = 0
    end = l.__len__() - 1
    mergeSort(l, start, end)
    print(l)
