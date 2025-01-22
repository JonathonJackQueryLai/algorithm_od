# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @project_name : DUOyi
# @Time : 2021/12/30
# @description : 


def removeDuplicates(nums):
    n = len(nums)
    if n <= 2:
        return n
    right = 2
    left = 0
    count = 0
    while right < n:
        if nums[left] == nums[right]:
            right += 1
        else:

            left += 1
            nums[left] = nums[right]
            right += 1
            count += 1
    return left + 1


class Solution:
    def removeDuplicates(self, nums: list) -> int:
        n = len(nums)
        if n < 2:
            return n
        right = 1
        left = 0
        while right < n:
            if nums[left] == nums[right]:
                right += 1
            else:
                left += 1
                nums[left] = nums[right]
                right += 1
                count += 1
        return left + 1


if __name__ == '__main__':
    print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
