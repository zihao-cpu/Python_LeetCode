#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   findLengthOfLCIS.py
@Time    :   2024/11/15 20:05:52
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        if not nums:
        
            return 0
        result = 1
        n = len(nums)
        if n == 1:
            return 1
        dp=[1]*n
        for i in range(n-1):
            if nums[i+1]>nums[i-1]:
                dp[i+1]=dp[i]+1
            result = max(result,dp[i+1])
        return result