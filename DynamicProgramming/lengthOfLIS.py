#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   lengthOfLIS.py
@Time    :   2024/11/15 19:42:14
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''

#最长递增子序列的长度
#dp[i]代表的是i之前包括i的以nums[i]结尾的最长递增子序列的长度
#状态转移方程为：dp[i] = max(dp[j] + 1) for j in range(i) if nums[j] < nums[i]
#即，如果nums[j] < nums[i]，则nums[j]可以接在nums[i]的后面形成一个更长的递增子序列，
#因此dp[i] = max(dp[j] + 1)

class Solution:
    def lengthOfLIS(self, nums) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        for i in range(1,n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
