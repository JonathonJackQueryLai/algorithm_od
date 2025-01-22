# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @project_name : DUOyi
# @Time : 2021/12/30
# @description : 有效括号


def isValid(s: str):
    """
    :type s: str
    :rtype: bool
    """
    s_len = len(s)
    if s_len % 2 != 0:
        return False
    mid = (s_len - 1) // 2
    # right = mid + 1
    # left = mid

    pre = ['(', '{', '[']
    # sub = [')', '}', ']']
    dic = {'(': ')', '{': '}', '[': ']'}
    temp = []
    count = 0
    for left in range(s_len):
        if temp == []:
            if s[left] not in pre:
                return False
            temp.append(s[left])
            continue
        else:

            if s[left] in pre:
                temp.append(s[left])
            else:

                if dic[temp[-1]] == s[left]:
                    temp.pop()
                else:
                    return False

    if temp:
        return False
    return True


if __name__ == '__main__':
    print(isValid("(){}}{"))
    # print(isValid("([]}"))
