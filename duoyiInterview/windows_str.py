# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @project_name : DUOyi
# @Time : 2022/2/14
# @description :
# https://leetcode-cn.com/problems/permutation-in-string/submissions/
'''
给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。

换句话说，s1 的排列之一是 s2 的 子串 。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-in-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


def checkInclusion(s1: str, s2: str) -> bool:
    left = 0
    n = s2.__len__()
    m = s1.__len__()
    s3 = s1
    right = m
    while right <= n:

        temp = s2[left:right]
        for i in temp:

            if i not in s1:
                break
            else:
                p = s1.index(i)
                s1 = s1[:p] + s1[p+1:]
        if not s1:
            return True
        s1 = s3
        left += 1
        right += 1

    return False





if __name__ == '__main__':
    print(checkInclusion("ab","ab"))
