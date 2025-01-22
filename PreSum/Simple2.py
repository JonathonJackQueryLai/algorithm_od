# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @project_name : DUOyi
# @Time : 2022/3/7
# @description :

class NumArray:
    def __init__(self, nums):
        self.sums = [0]
        _sums = self.sums

        for num in nums:
            _sums.append(_sums[-1] + num)
        print(self.sums)
    def sumRange(self, i: int, j: int) -> int:
        _sums = self.sums
        return _sums[j + 1] - _sums[i]


if __name__ == '__main__':
    myN = NumArray([-2, 0, 3, -5, 2, -1])
    print(myN.sumRange(2, 5))
