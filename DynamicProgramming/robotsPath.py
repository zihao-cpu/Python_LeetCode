#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   robotsPath.py
@Time    :   2024/11/01 16:05:37
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def roobotsPath(self, m, n):
        dp=[[0]*n for _ in range(m)]
        for i in range(m):
            dp[i][0]=1
        for j in range(n):
            dp[0][j]=1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]