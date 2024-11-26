#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   minDistance2.py
@Time    :   2024/11/26 18:52:13
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''

class Solution:
    def minDistance2(self, word1: str, word2: str) -> int:
        dp=[[0]*(len(word1)+1) for _ in range(len(word2)+1)]
        for i in range(len(word2)+1):
            dp[i][0]=i
        for j in range(len(word1)+1):
            dp[0][j]=j
        for i in range(1,len(word2)+1):
            for j in range(1,len(word1)+1):
                if word2[i-1]==word1[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1 #增和删一样 就是替换
        return dp[-1][-1]
    