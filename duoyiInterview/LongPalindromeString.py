# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @Time :2021/10/7-18:15
# @template :
def longestPalindrome(s: str) -> str:
    length = len(s)
    right = 0
    left = length - 1
    index, index1 = 0, 0
    while right < length:
        while left >= 0:
            if s[right] == s[left]:

                if right == left or (left - right == 1):
                    return s[right - index:left + index + 1]
                right += 1
                left -= 1
                index += 1
            else:
                if s[right] != s[left]:
                    if right == left:
                        break
                    index, index1 = 0, 0
                    l = length - left
                    if l < right+1:
                        left -= 1

                    else:
                        right += 1

if __name__ == '__main__':
    print(longestPalindrome(s="bba1234"))
