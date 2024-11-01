#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   minCostClimbStairs.py
@Time    :   2024/11/01 15:56:36
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
from typing import Any

class Solution():
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2, n+1):
            dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        return dp[n]

if __name__ == '__main__':
    s = Solution()
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(s.minCostClimbingStairs(cost))