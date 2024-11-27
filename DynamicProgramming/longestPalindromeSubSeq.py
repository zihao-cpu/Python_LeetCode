#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   longestPalindromeSubSeq.py
@Time    :   2024/11/27 14:40:18
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class  Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp=[[0]*(len(s)+1) for _ in range(len(s)+1)]
        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                if s[i]==s[j]:
                    dp[i][j]=dp[i+1][j-1]+2
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j-1])
        return dp[0][len(s)-1]
      