# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @Time :2020/6/18-14:46
# @template : 二叉堆
import random
import head

# 上升
def upJust(arr: list):
    childIndex = len(arr) - 1  # 从最后开始
    parentIndex = (childIndex - 1) // 2  # 完全二叉树 左孩子先开始,最容易忘记
    temp = arr[childIndex]
    # > 0至少孩子不能是顶点吧
    while childIndex > 0 and temp < arr[parentIndex]:  # 找一个 小于父节点的 上去
        arr[childIndex] = arr[parentIndex]
        childIndex = parentIndex
        parentIndex = int((parentIndex - 1) / 2)
    arr[childIndex] = temp
    arr1 = arr


# 下沉
def downJust(arr, parentIndex, length):
    temp = arr[parentIndex]  # 跟左右孩子比较
    childrenIndex = 2 * parentIndex + 1  # 左孩子
    while childrenIndex < length:  # 不能超过
        # 还有右孩子的话，且右孩子小于左孩子的值，则定位到右孩子
        if childrenIndex + 1 < length and arr[childrenIndex + 1] < arr[childrenIndex]:
            childrenIndex += 1
        # 下沉找一个更大的交换
        if temp <= arr[parentIndex]:
            break
        arr[parentIndex] = arr[childrenIndex]
        parentIndex = childrenIndex
        childrenIndex = 2 * childrenIndex + 1

    arr[parentIndex] = temp


def downJust(arr, parentIndex, length):
    temp = arr[parentIndex]
    childrenIndex = parentIndex * 2 + 1  # 左孩子
    while childrenIndex < length:
        if childrenIndex + 1 < length and arr[childrenIndex + 1] > arr[childrenIndex]:
            childrenIndex += 1
        if temp < arr[parentIndex]:
            break
        arr[parentIndex] = arr[childrenIndex]
        parentIndex = childrenIndex
        childrenIndex = 2 * childrenIndex + 1
    arr[parentIndex] = temp


# 取出父节点进行每一次的下沉
def build(arr: list):
    # 从下面的父亲节点到根节点
    for i in range((len(arr) - 2) // 2, -1, -1):
        downJust(arr, i, len(arr) - 1)
    print(arr)
    # 最后一个跟 第一个元素交换
    for i in range(arr.__len__() // 2, -1, -1):
        temp = arr[i]
        arr[i] = arr[0]
        arr[0] = temp
        downJust(arr, 0, i)


if __name__ == '__main__':
    arr = [random.randint(0, 10) for i in range(10)]
    print("上调调整前：", arr)
    upJust(arr)
    print("上调整后", arr)

    arr1 = [random.randint(0, 10) for i in range(10)]
    print("下沉调整前：", arr1)
    build(arr1)
    print("调整后：", arr1)