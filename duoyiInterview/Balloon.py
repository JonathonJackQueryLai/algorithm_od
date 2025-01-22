# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @Time :2020/6/17-0:32
# @template :

def modify(data: dict):
    '''
    计算出一种可行的挂气球方式
    :param data:
    :return:
    '''
    try:
        bal_count = sum([i for i in data.values()])  # 气球总数
        # 气球颜色最多的数量
        max_count = sorted(data.items(), key=lambda v: v[1], reverse=True)[0][1]
        res = []
        if max_count > (bal_count + 1) // 2:
            print('无法做到相同颜色的气球不挂在一起')
            return ''
        for k, count in data.items():
            res.extend(k * count)

        ans = [None] * bal_count
        ans[::2], ans[1::2] = res[bal_count // 2:], res[:bal_count // 2]
        return "|".join(ans)
    except Exception as ex:
        print(ex)


def isInt(num: int):
    if isinstance(num, int):
        return int(num)
    else:
        return False


if __name__ == '__main__':
    while 1:
        try:
            redNum = int(input("请输入红球的数量：").strip())
            blueNum = int((input("请输入蓝球的数量：")).strip())
            whiteNum = int((input("请输入白球的数量：")).strip())
        except Exception as ex:
            print("输入无效，请输入数字！")
            continue
        inputData = {
            'r': redNum,
            'b': blueNum,
            'w': whiteNum,
        }
        res = modify(inputData)
        print(res)
