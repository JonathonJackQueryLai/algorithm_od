# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @Time :2020/6/16-21:56
# @template : 快速排序

def quickSort(arr, start, end):
    if start >= end:
        return
    povit_index = sort3(arr, start, end)
    quickSort(arr, start, povit_index - 1)
    quickSort(arr, povit_index + 1, end)

# java C++ C#的写法
def sort1(arr, start, end):
    # 直接使用start的话，第一个index的位置就发生了变化，需要保留第一个位置
    left = start
    right = end
    pivot = arr[start]
    # 两个指针一起协作 所以使用到三个while
    while left < right:
        while left < right and arr[right] > pivot:
            right -= 1
        while left < right and arr[left] <= pivot:
            left += 1
        # 因为左边的都小于基准值 右边都大于基准值就行
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
    # 指针交换
    temp = arr[left]
    arr[left] = arr[start]
    arr[start] = temp
    return left


def sort3(array, start, end):
    left = start
    right = end
    base = array[start]
    while left < right:
        # 也是有顺序的
        while left < right and array[right] > base:
            right -= 1

        while left < right and array[left] <= base:
            left += 1
        # 简化交换，但是注意与以往不同的是指针指向的内存没有发生改变
        array[left], array[right] = array[right], array[left]
    # 为什么是arr[start]而不能用base，因为array[left] 就是base值，这样做会使得重复

    array[left], array[start] = array[start], array[left]
    return left


#  这种是可读性比较差的方法 结果：passed
def sortf(array, start, end):
    if start >= end:
        return
    # 挖坑法
    left = start
    right = end
    base = array[start]
    while left < right:
        while left < right and array[right] > base:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= base:
            left += 1
        array[right] = array[left]

    array[right] = base
    sortf(array, start, left - 1)
    sortf(array, left + 1, end)


# 挖坑法 结果 passed
def sort4(array, start, end):
    left = start
    right = end
    base = array[start]
    while left < right:

        # 跟顺序有关
        while left < right and array[right] > base:
            right -= 1
        array[left] = array[right]

        while left < right and array[left] <= base:
            left += 1
        array[right] = array[left]
    # 下面这样一步叫做挖个坑让标准值跳到里面去，所以不能使用array[start]
    array[left] = base
    return left


if __name__ == '__main__':
    import random

    array = [random.randint(1, 1000) for i in range(5)]
    # 属于原地排队 直接
    quickSort(array, 0, array.__len__() - 1)
    # sortf(array, 0, array.__len__() - 1)
    print(array)
