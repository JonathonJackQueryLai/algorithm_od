# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @project_name : DUOyi
# @Time : 2022/1/1
# @description : 最长公共前缀


def func(strs=["a11", "a12", "a13"]):
    m = len(strs[0])
    n = len(strs[1])
    l = len(strs[2])
    min_len = min(m, n, l)
    a = 1
    b = 1
    c = 1

    if strs[0][0] != strs[1][0] or strs[0][0] != strs[2][0] or strs[0][0] != strs[2][0]:
        return '输入不存在公共前缀。'
    else:
        flag = strs[0][0] == strs[1][0] == strs[2][0]
        if flag:
            temp = strs[0][0]
            while a < m and b < n and c < l:
                if strs[0][a] == strs[1][b] == strs[2][c]:
                    temp += strs[0][a]
                a += 1
                b += 1
                c += 1

        return temp


if __name__ == '__main__':
    print(func())
