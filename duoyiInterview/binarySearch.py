# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @Time :2020/6/23-18:54
# @template :
class Doc(object):
    def __init__(self):
        pass

    def binarySearch(self):
        pass


def binarySearch(array: list, target):
    end = len(array) - 1
    start = 0

    while start <= end:
        mid = start + (end - start) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1

    return False


if __name__ == '__main__':
    # a = [i for i in range(0, 100)]
    li = sorted([3, 18, 5, 17, 38, 44, 65, 95, 14, 16])
    print(li)
    # print(binarySearch(a, 50))
    print(binarySearch(li, 95))
    print(binarySearch(li, 3))
