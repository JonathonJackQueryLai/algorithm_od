# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @Time :2021/10/7-14:30
# @template :
def twoSum(nums: list, target: int) -> list:
    # hashmap = {}
    # for index, num in enumerate(nums):
    #     another_num = target - num
    #     if another_num in hashmap:
    #         return [hashmap[another_num], index]
    #     hashmap[num] = index
    # return None


    d = {}
    for i in range(nums.__len__()):
        temp = target - nums[i]
        if temp in d:
            return [i, d[temp]]
        d[nums[i]] = i
    # hashD = {}
    # for index, num in enumerate(nums):
    #     temp = target - num
    #     if temp in hashD:
    #         return [hashD[temp], index]
    #     else:
    #         hashD[num] = index
    # return None


# for idx, val in enumerate(nums):
#             if target - val not in records:
#                 records[val] = idx
#             else:
#                 return [records[target - val], idx]

if __name__ == '__main__':
    print(twoSum([1, 3, 2, 4, 5], 6))
