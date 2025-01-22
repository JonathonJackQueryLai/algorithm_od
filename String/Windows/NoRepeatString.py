# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @project_name : DUOyi
# @Time : 2022/3/8
# @description :


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se = set(s)
        dic = {}
        for i in se:
            dic[i] = 0

        left = 0
        right = 0
        n = len(s)
        res = 0
        while right < n:
            c = s[right]
            right += 1
            dic[c] += 1
            while dic[c] > 1:
                d = s[left]
                left += 1
                dic[d] -= 1

            res = max(res, right - left)
        return res


if __name__ == '__main__':
    myFunc = Solution()
    print(myFunc.lengthOfLongestSubstring("abcde"))
