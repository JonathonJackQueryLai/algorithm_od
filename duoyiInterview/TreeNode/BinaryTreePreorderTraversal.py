# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @project_name : DUOyi
# @Time : 2022/1/11
# @description : 前序遍历


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 递归
def preorderTraversal(root: TreeNode) -> list:
    if not root:
        return ['1']
    return [root.val] + preorderTraversal(root.left) + preorderTraversal(root.right)


# 迭代
def preorderTraversal(root: TreeNode) -> list:
    if not root:
        return []
    return [root.val] + preorderTraversal(root.left) + preorderTraversal(root.right)


def inorderTraversal(root: TreeNode) -> list:
    if not root:
        return []
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)


def postorderTraversal(root: TreeNode) -> list:
    if not root:
        return []
    return postorderTraversal(root.left) + postorderTraversal(root.right) + [root.val]


# 判断是不是同一颗树 leetcode
def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    li1 = preorderTraversal(p)
    li2 = preorderTraversal(q)
    print(f'li1:{li1}')
    print(f'li2:{li2}')
    if li1.__len__() == li2.__len__():

        if li1 == li2:
            return True
        else:
            return False
    else:
        return False


# 第一百题 100. 相同的树
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q != None: return False
        if q == None and p != None: return False
        if p != None and q != None:
            if p.val != q.val: return False
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return True


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(1)
    root.left = TreeNode(None)
    root1 = TreeNode(1)
    root1.left = TreeNode(1)
    print(isSameTree(root, root1))
