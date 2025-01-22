# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @project_name : DUOyi
# @Time : 2022/1/16
# @description : 


def divideString(s: str, k: int, fill: str):
    str_len = len(s)
    num = str_len // k
    mod = str_len % k
    res_li = []
    left = 0  # 指针
    if k > str_len:
        return [s + (k - str_len) * fill]
    else:
        while 1:
            temp = s[left:left + k]
            if left + k <= str_len - mod:

                res_li.append(temp)
                left += k

            else:
                break

        if mod == 0:
            pass
        else:
            res_li.append(s[-mod:] + (k-mod) * fill)

        return res_li


if __name__ == '__main__':
    print(divideString('bgycymgbblobvpdf', 67, 'u'))
