#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   maxProfit2.py
@Time    :   2024/11/12 15:45:33
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution:

            #动态规划
    #如果第i天持有股票即dp[i][0]，1）第i-1天就持有股票并且第i天不卖出，那么就保持现状，所得现金就是昨天持有股票的所得现金 即：dp[i - 1][0]
    #2）第i-1天就持有股票并且第i天买入，所得现金就是昨天持有股票的所得现金减去今天买入股票的价格 即：- prices[i]

    #如果第i天不持有股票即dp[i][1],1）那么就保持现状，所得现金就是昨天不持有股票的所得现金 即：dp[i - 1][1]
    #2）第i天卖出股票，所得现金就是按照今天股票价格卖出后所得现金即：prices[i] + dp[i - 1][0]
    def maxProfit2(self, prices) -> int:
        dp=[[0,0]*len(prices)]
        dp[0][0]=-prices[0]
        dp[0][1]=0
        for i in range(1,len(prices)):
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]-prices[i])  #唯一差别 是多次买卖 
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]+prices[i])
        return dp[-1][1]