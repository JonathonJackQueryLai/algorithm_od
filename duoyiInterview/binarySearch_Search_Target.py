# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @project_name : DUOyi
# @Time : 2022/1/8
# @description : 


def func(nums: list, target: int):
    start = 0
    end = len(nums) - 1
    mid = (start + end) // 2
    temp = nums[mid]
    flag = 0
    while 1:
        if target == temp:
            return mid

        if target < temp:
            end = mid - 1
            flag = True
        else:
            start = mid + 1
            flag = False
        if start <= end:
            mid = (start + end) // 2
            temp = nums[mid]
        else:
            break

    if flag:
        return mid
    else:
        # if mid == 0:
        #     return mid + 2

        return mid + 1


def searchInsert(nums: list, target: int) -> int:
    num_len = len(nums)
    right = num_len - 1
    left = 0
    mid = (right + left) // 2
    flag = True
    while left <= right:
        if target == nums[mid]:
            return mid
        else:
            if target > nums[mid]:
                flag = True
                left = mid + 1
                mid = (right + left) // 2

            elif target < nums[mid]:
                flag = False
                right = mid - 1
                mid = (right + left) // 2
                # target = nums[mid]
    if target > nums[mid]:
        return mid + 1
    else:
        if mid <= 0:

            return mid + 1
        else:
            return mid


if __name__ == '__main__':
    # print(func([1, 3, 5, 6],2))
    print(searchInsert([1, 3,5], 4))
