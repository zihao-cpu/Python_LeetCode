#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   maxProfilt3.py
@Time    :   2024/11/13 15:37:12
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution:
    #给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易
    #dp数组里面放的是什么
    #五个状态：
    #什么斗都不干 0
    #第一次持有股票 1：1）第i-1天就持有股票并且第i天不卖出，那么就保持现状，所得现金就是昨天持有股票的所得现金：dp[i][1]=dp[i-1][1]
                   #2）第i-1天就不持有股票第i天买入，所得现金就是昨天持有股票的所得现金减去今天买入股票的价格 即：dp[i][1]=dp[i-1][0]- prices[i]
    #第一次不持有股票 2
    #第二次持有股票 3
    #第二次不持有股票 4

    def maxProfit3(self, prices) -> int:
        if len(prices) == 0:
            return 0
        dp = [[0] * 5 for _ in range(len(prices))]
        dp[0][1] = -prices[0]
        dp[0][3] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = dp[i-1][0]
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
            dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i])
        return dp[-1][4]      