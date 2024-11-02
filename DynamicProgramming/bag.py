#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   bag.py
@Time    :   2024/11/02 11:55:15
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def bag(self,weights,values,capacity):
        dp=[[0]*(capacity+1) for _ in range(len(weights))]
        for i in range(capacity+1):
            dp[0][i]=values[0]
        for i in  range(len(weights)):
            for j in range(capacity+1):
                if j<weights[i]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=max(dp[i-1][j-weights[i]]+values[i],dp[i-1][j])
        return dp[-1][-1]
if __name__ == '__main__':    
    weights=[2,3,4,5]
    values=[1,5,3,7]    
    capacity=7
    s=Solution()
    print(s.bag(weights,values,capacity)) 