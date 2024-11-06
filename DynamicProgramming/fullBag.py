#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   fullBag.py
@Time    :   2024/11/05 19:43:31
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    #完全背包问题
    #二维的dp 
    def fullbag(self,weights,values,capacity):
        dp=[[0]*(capacity+1) for _ in range(len(weights))]
        for i in range(capacity+1):
            dp[0][i]=values[0]
        for i in  range(1,len(weights)):
            for j in range(capacity+1):
                # if j<weights[i]:
                #     dp[i][j]=dp[i-1][j]
                # else:
                #     dp[i][j]=max(dp[i-1][j-weights[i]]+values[i],dp[i-1][j])
                dp[i][j]=dp[i-1][j]
                for k in range(j//weights[i]+1):
                    if j>=k*weights[i]:
                        dp[i][j]=max(dp[i][j],dp[i-1][j-k*weights[i]]+k*values[i])
        return dp[len(weights) - 1][capacity]
    
    def fullbag2(self,weights,values,capacity):
        dp=[0]*(capacity+1)
        for i in range(len(weights)):
            for j in range(weights[i],capacity+1):#正序的遍历
                dp[j]=max(dp[j],dp[j-weights[i]]+values[i])
        return dp[capacity]
   

 
if __name__ == '__main__':    
    weights=[2,3,4,5]
    values=[1,5,3,7]    
    capacity=7
    s=Solution()
    print(s.bag(weights,values,capacity)) 