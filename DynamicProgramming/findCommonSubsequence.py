#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   findCommonSubsequence.py
@Time    :   2024/11/18 13:17:51
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
def findCommonSubsequence(s1: str, s2: str) -> str:
    dp=[[0]*len(s1)+1 for _ in range(len(s2)+1)]
    for i in range(1,len(s2)+1):
        for j in range(1,len(s1)+1):
            if s2[i-1]==s1[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    res=""
    i,j=len(s2),len(s1)
    while i>0 and j>0:
        if s2[i-1]==s1[j-1]:
            res=    s2[i-1]+res 
            i-=1    
            j-=1
        elif dp[i-1][j]>dp[i][j-1]:
            i-=1
        else:
            j-=1
    return res
if __name__ == '__main__':
    s1="ABCDGH"
    s2="AEDFHR"
    print(findCommonSubsequence(s1,s2)) # ADH