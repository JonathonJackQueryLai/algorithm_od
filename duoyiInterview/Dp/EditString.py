# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @project_name : DUOyi
# @Time : 2021/12/29
# @description : 编辑距离
"""
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

"""


# 可读性更强
def mindistance(word1, word2):
    m = len(word1)
    n = len(word2)
    # 二维数组 为什么要 + 1； 为什么要使用二维数组
    # +1 是为了在递推的过程中不爆栈
    # dp[i][j] 表示word1[i]变成word2[j]的时候使用的最小的步数的数量
    dp = [[0 for col in range(n + 1)] for row in range(m + 1)]
    # 当word1有i个数需要delete i 个数变成word2中的 j = 0
    for i in range(m + 1):
        dp[i][0] = i
    # 同上 同理
    for j in range(n + 1):
        dp[0][j] = j
    # 老框架了 就是一个递推
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # 当数位上的字符相等的时候，就躺赢什么都不用做 直接等于之前的那个dp就行
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # 这里是 插入，删除，替换的操作
                '''
                dp[i - 1][j] 删除，因为dp[i][j]多余了一个word[i]
                dp[i][j-1] 插入 见上同理可得 ,需要插入一个数才能变成word[j],因此 j++
                dp[i-1][j-1]  替换需要将word1[i] 变成 word2[j] 才能实现dp[i][j]， i,j 需要同时前进一位       
                '''
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    return dp[m][n]


def mindistance1(word1, word2):
    m = len(word1)
    n = len(word2)
    dp = [[0 for col in range(n + 1)] for row in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = min(dp[i - 1][j - 1] + (0 if word1[i - 1] == word2[j - 1] else 1), dp[i][j - 1] + 1,
                           dp[i - 1][j] + 1)
    return dp[m][n]




if __name__ == '__main__':
    # print(mindistance('ucyfsmg', 'zuixhuhyjgksyhqkjqxwylkoubykjxtcvkyqjpzgltbemmbmqibxxqpkgbvwbmjotixanvciibubglizmumcrjavakiygyuv'))