# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @project_name : DUOyi
# @Time : 2022/1/18
# @description : 


class Solution:
    def rob(self, nums: list) -> int:
        num_len = nums.__len__()
        if num_len == 1:
            return nums[0]
        return max(self.robber(nums, 0, num_len - 2), self.robber(nums, 1, num_len - 1))

    def robber(self, li, start, end):
        dp1 = 0
        dp2 = 0
        dp = 0
        for i in range(end, start - 1, -1):
            dp = max(dp1, dp2 + li[i])
            dp2, dp1 = dp1, dp

        return dp


def quicksort1(array, start, end):
    pivot = array[start]
    left = start
    right = end
    while left < right:

        while left < right and array[right] > pivot:
            right -= 1

        while left < right and array[left] <= pivot:
            left += 1
        array[right], array[left] = array[left], array[right]
    array[start], array[left] = array[left], array[start]
    return left

def quicksort(array, start, end):
    pivot = array[start]
    left = start
    right = end
    while left < right:

        while left < right and array[right] > pivot:
            right -= 1
        array[right], array[left] = array[left], array[right]
        while left < right and array[left] <= pivot:
            left += 1
        array[right], array[left] = array[left], array[right]

    # pivot, array[left] = array[left], pivot
    # pivot, array[left] = array[left], pivot
    # array[start] = array[left]
    array[left] = pivot

    return left
def func(array, start, end):
    # start = 0
    # end = array.__len__() - 1
    if start >= end:
        return

    pivot = quicksort(array, start, end)
    func(array, start, pivot - 1)
    func(array, pivot + 1, end)


if __name__ == '__main__':
    li = [1, 3, 5, 4, 2, 7]
    func(li, 0, 5)
    print(li)
