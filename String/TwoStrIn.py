# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @project_name : DUOyi
# @Time : 2022/1/22
# @description : 链接： https://leetcode-cn.com/problems/implement-strstr/ 28. 实现 strStr() (类似于Python里面的find())


def strStr(haystack: str, needle: str) -> int:
    if haystack == '' and needle == '':
        return 0
    if haystack == '' and needle != '':
        return -1
    if haystack == needle:
        return 0
    n1 = haystack.__len__()
    n2 = needle.__len__()
    left = 0
    right = n2
    # 以左右指针作为窗口一起移动去扫描needle字符串是否存在
    while right <= n1:
        if haystack[left:right] == needle:
            return left
        else:
            left += 1
            right += 1
    return -1


if __name__ == '__main__':
    print(strStr('abc', "c"))
