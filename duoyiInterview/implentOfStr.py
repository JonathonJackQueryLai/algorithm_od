# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @Time :2021/10/7-12:23
# @template :
def strStr(haystack: str, needle: str) -> int:
    if haystack == '' and needle == '':
        return 0
    if needle == '':
        return 0
    target = needle[0]
    if target in haystack:
        return haystack.index(target)
    else:
        return -1


if __name__ == '__main__':
    print(strStr(haystack='aaa', needle='aaaa'))
