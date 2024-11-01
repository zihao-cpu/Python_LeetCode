#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   climbStairs.py
@Time    :   2024/11/01 15:40:04
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
from typing import Any


class Solution():
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]  
        return dp[n]
    

    def climbStairs_v2(self, n: int) -> int:
        dp=[0]*(n+1)
        
        dp[0]=1
        for i in range(1,n+1):
            for j in range(1,i+1):
                if i-j>=0:
                    dp[i]+=dp[i-j]
        return dp[n]
