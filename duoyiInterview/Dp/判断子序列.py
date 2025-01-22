# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @project_name : DUOyi
# @Time : 2021/12/28
# @description :  判断子序列
'''
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

进阶：

如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？


'''


def isSubsequence1(s: str, t: str):
    s1 = 0
    t1 = 0
    len1 = len(s)
    len2 = len(t)

    while s1 < len1 and t1 < len2:
        if s[s1] == t[t1]:
            s1 += 1
            t1 += 1
        else:
            t1 += 1
    if s1 == len1:
        return True
    else:
        return False


'''

思路：

状态：dp[i][j]为s的从头开始到i的子字符串是否为t从头开始到j的子字符串的子序列

状态转移公式：

当char[i]==char[j]时，则字符i一定是j的子序列，如果0~i-1子字符串是0~j-1子字符串的子序列，则dp[i][j]=true，所以dp[i][j] = dp[i-1][j-1]；
当char[i]!=char[i]时，即判断当前0~i子字符串是否是0~j-1的子字符串的子序列，即dp[i][j] = dp[i][j - 1]。如ab，eabc，虽然s的最后一个字符和t中最后一个字符不相等，但是因为ab是eab的子序列，
所以ab也是eabc的子序列
初始化：空字符串一定是t的子字符串的子序列，所以dp[0][j]=true

结果：返回dp[sLen][tLen]

'''



def isSubsequence(word1: str, word2: str):
    m = len(word1)
    n = len(word2)
    dp = [[False for col in range(n + 1)] for row in range(m + 1)]
    for j in range(n + 1):
        dp[0][j] = True
    for i in range(m):
        for j in range(n):
            # 相等的话 继续找下一位，i, j
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i][j - 1]

if __name__ == '__main__':
    print(isSubsequence1("aaaaaaaaaa",
                         "bbaaaa"))
