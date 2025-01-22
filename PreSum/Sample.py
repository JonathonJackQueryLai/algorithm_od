# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @project_name : DUOyi
# @Time : 2022/3/3
# @description :


class NumArray:

    def __init__(self, nums: list):
        n = nums.__len__()
        self.nums1 = [0 for i in range(n + 1)]
        # self.nums1[0] = nums[0]
        for i in range(1, n + 1):
            self.nums1[i] = self.nums1[i - 1] + nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        return self.nums1[right + 1] - self.nums1[left]


'''
# [0, -2, -2, 1, -4, -2, -3]
# -1
[0, -2, -2, 1, -4, -2, 0]
2

'''


def func():
    setu = '社团'
    return '色图' if '色图' == setu else '社团'


if __name__ == '__main__':
    myN = NumArray([-2, 0, 3, -5, 2, -1])
    # print(myN.sumRange(2, 5))
    li = ['bbb', 'ddbb']
    num = max(li, key=len)
    print(num)
