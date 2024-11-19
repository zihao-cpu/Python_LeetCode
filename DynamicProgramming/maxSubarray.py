#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   maxSubarray.py
@Time    :   2024/11/19 19:01:54
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution:
    def maxSubArray(self, nums) -> int:
        dp=[0]*len(nums)
        dp[0]=nums[0]
        result=nums[0]
        for i in range(1,len(nums)):
            dp[i]=max(nums[i],dp[i-1]+nums[i])
            result=max(result,dp[i])
        return result

