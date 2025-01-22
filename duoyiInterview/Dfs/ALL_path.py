# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @project_name : DUOyi
# @Time : 2022/2/23
# @description :

# 遍历图的所有的
# 类似于二叉树的深度遍历
def func(graph: list):
    ans = []
    stack = []

    def dfs(s):
        n = graph.__len__()

        if n - 1 == s:
            ans.append(stack[:])
            return
        for i in graph[s]:
            stack.append(i)
            dfs(i)
            #撤回操作
            stack.pop()

    stack.append(0)
    dfs(0)
    return ans


if __name__ == '__main__':
    print(func([[1, 2], [3], [3], []]))
