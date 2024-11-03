#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   lastStoneWeight.py
@Time    :   2024/11/03 17:58:14
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    #这道题的本质和分成两个子集和相同的子集一样，这题是尽可能区分成两堆，使得两堆的和最小
    #我们可以用动态规划来解决这个问题，dp[i][j] 表示前 i 个石头中，是否存在一种方法，可以将其分成两堆，使得两堆的和为 j。
    #如果 dp[i][j] 为 True，说明我们可以将数组分成两堆，使得两堆的和为 j，那么我们需要返回数组中所有元素的和减去 2*j。
    #如果 dp[i][j] 为 False，说明我们不能将数组分成两堆，使得两堆的和为 j。
    def lastStoneWeight(self, stones) -> int:
        taget_num=sum(stones)/2
        dp=[[False]*(taget_num+1) for _ in range(len(stones)+1)]
        for i in range(len(stones)+1): #初始化第一
            dp[i][0]=True


        for i in range(1,len(stones)+1):
            for j in range(1,taget_num+1):
                if j< stones[i-1]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-stones[i-1]]#如果我们能够通过选择或不选择第 i 个元素来构成和为 j 的子集，那么 dp[i][j] 就为 True；否则为 False
        for j in range(taget_num,-1,-1):
            if dp[len(stones)][j]:
                return sum(stones)-2*j #如果 dp[len(stones)][j] 为 True，说明我们可以将数组分成两堆，使得两堆的和为 j，那么我们需要返回数组中所有元素的和减去 2*j   
        return 0
