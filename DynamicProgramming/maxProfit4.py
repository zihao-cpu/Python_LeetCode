#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   maxProfit4.py
@Time    :   2024/11/13 21:38:57
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution:

    #买股票最多交易k次
    def maxProfit4(self, prices,k) -> int:
        if not prices:
            return 0
        dp = [[0] * (2*k+1) for _ in range(len(prices))]
        for i in range(1,2*k,2):
            dp[0][i] = -prices[0]
        for i in range(1,len(prices)):
            for j in range(0,2*k-1,2):
                dp[i][j+1] = max(dp[i-1][j+1],dp[i-1][j]-prices[i])
                dp[i][j+2] = max(dp[i-1][j+2],dp[i-1][j+1]+prices[i])
        return dp[-1][2*k]