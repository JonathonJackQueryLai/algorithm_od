# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @project_name : DUOyi
# @Time : 2022/3/12
# @description :

import numpy as np

# 初始化
def func():
    a = np.zeros((3, 2), dtype=np.float32)
    # 结构
    print(a.shape)
    # 像Python递增列表一样的操作
    b = np.arange(3, 7)
    print(b, b.shape)
    # 在指定的区间内返回均匀间隔的数字
    c = np.linspace(0, 10, 10)
    print(f'c类型 ：{type(c)},C ：{c}')
    # 返回一个二维的0到1的随机值
    d = np.random.random((2, 4))
    print(d)
    # 转化数据类型 ，一定要赋值给另一个变量
    e = d.astype(int)
    print(e)

# 计算
def oper_func():
    # 相同尺寸的数组可以进行相加
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    c = a + b
    # 相除
    # print(b // a)
    # 相乘
    # print(np.dot(a, b))

    # 交叉相乘 一维数组相乘为一个数值，而维度不对应，按最低的维度给出结果
    d = np.array([[1, 2]])
    e = np.array([[1, 2], [0, 1]])
    print(d @ e)
    # 求 平方根
    print(np.sqrt(a))
    # sin 值
    print(np.sin(a))
    # cos
    print(np.cos(a))
    # 对数
    print(np.log(a))
    # 指数
    print(np.power(a, 2))

    # 最大或者是最小值,平均值，总和,标准方差，方差
    print(np.min(a), np.max(a), np.mean(a), np.sum(a), np.median(a), a.std(), a.var())
    # 返回最大或者是最小值的索引
    print(np.argmin(a), np.argmax(a))

    # axis 为 0 等于将第一个维度相加 ，axis为 1 等于将第二个维度相加
    print(e.sum(axis=0))  # 行相加
    print(e.sum(axis=1))  # 列相加

# 索引
def fun1():
    # filter过滤
    a = np.array([i for i in range(1, 10)])
    # 跟Python的习惯不一样
    print(a[(a < 9) & (a % 2 == 0)])
    # 跟Python的索引一样
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    # print(arr[0, 1])
    # print(arr[1, 2])
    # 分片
    arr1 = np.array([[1, 2, 3], [4, 5, 6]])
    print(arr1[0, ::-1])
    print(arr1[1, :])

if __name__ == '__main__':
    func()
    oper_func()
    fun1()
