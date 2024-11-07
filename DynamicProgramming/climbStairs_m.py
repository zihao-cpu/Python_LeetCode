#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   climbStairs_m.py
@Time    :   2024/11/07 15:29:17
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution:
    #m 是每次至多爬的台阶数 是一个完全背包的问题
    def climbStairs_m(self, n: int,m) -> int:
        dp=[0]*(n+1)
        dp[0]=1
        for i in range(1,n+1):
            for j in range(1,m+1):  # 这里的j表示每次爬的台阶数 所以j的范围是1~m    
                if i-j>=0:
                    dp[i]+=dp[i-j]
        return dp[n]