#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   minDistance.py
@Time    :   2024/11/25 22:44:12
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''

# 当word1[i - 1] 与 word2[j - 1]相同的时候
# 当word1[i - 1] 与 word2[j - 1]不相同的时候
# 当word1[i - 1] 与 word2[j - 1]相同的时候，dp[i][j] = dp[i - 1][j - 1];

# 当word1[i - 1] 与 word2[j - 1]不相同的时候，有三种情况：

# 情况一：删word1[i - 1]，最少操作次数为dp[i - 1][j] + 1

# 情况二：删word2[j - 1]，最少操作次数为dp[i][j - 1] + 1

# 情况三：同时删word1[i - 1]和word2[j - 1]，操作的最少次数为dp[i - 1][j - 1] + 2
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp=[[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(len(word1)+1):
            dp[i][0]=i
        for j in range(len(word2)+1):
            dp[0][j]=j
        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j-1]+2,dp[i-1][j]+1,dp[i][j-1]+1)
        return dp[-1][-1]