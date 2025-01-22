# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @project_name : DUOyi
# @Time : 2022/2/16
# @description :


def searchRange(nums: list, target: int) -> list:
    if not nums:
        return [-1, -1]

    # 大学内容了 没什么题解好说的
    start = 0
    length = nums.__len__()
    end = length - 1
    mid = (start + end) // 2
    temp = nums[mid]
    while start <= end:
        if target == temp:
            break
        elif target > temp:
            start = mid + 1
        elif target < temp:
            end = mid - 1
        mid = (start + end) // 2
        temp = nums[mid]
    if nums[mid] != target:
        return [-1, -1]
    elif nums[mid] == target and length == 1:
        return [mid, mid]
    start = 0
    end = length - 1
    num = nums.count(target)
    step = num - 1
    left = mid - step
    right = mid + step
    if left < start:
        left = start
    if right > end:
        right = end
    for i in range(left, mid + 1):
        if nums[i] == target:
            left = i
            break
    for i in range(mid, right + 1):
        if nums[i] != target:
            right = i - 1
            break
    return [left, right]


if __name__ == '__main__':
    print(searchRange([5, 7, 7, 8, 8, 10], 8))
    print(searchRange([2, 2], 2))
    print(searchRange([1], 1))
