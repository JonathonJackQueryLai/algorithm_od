# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @project_name : DUOyi
# @Time : 2022/2/25
# @description :



def permute( nums) -> list:

    def dfs(first=0):

        if n == first:
            res.append(nums[:])

        for i in range(first, n):
            nums[i], nums[first] = nums[first], nums[i]

            dfs(first + 1)  # 下一个起点
            nums[first], nums[i] = nums[i], nums[first]

    n = nums.__len__()
    res = []
    dfs()
    return res

if __name__ == '__main__':
    print(permute())

