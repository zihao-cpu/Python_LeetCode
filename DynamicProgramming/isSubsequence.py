#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   isSubsequence.py
@Time    :   2024/11/20 21:26:25
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution:
    def isSubsequence(self,s,t):
        dp=[[0]*(len(t)+1) for _ in range(len(s)+1)]
        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:   
                    dp[i][j]=dp[i-1][j]
        return dp[len(s)][len(t)]==len(s)   
    