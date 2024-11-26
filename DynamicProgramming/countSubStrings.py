#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   countSubStrings.py
@Time    :   2024/11/26 19:33:15
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        dp=[[False]*len(s) for _ in range(len(s))]

        result=0
        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                if s[i]==s[j]:
                    if j-i<=1:
                        result+=1
                        dp[i][j]=True
                    elif dp[i+1][j-1]:
                        result+=1
                        dp[i][j]=True
        return result
                