#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   nextGreaterElement2.py
@Time    :   2024/11/29 22:26:57
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution:
    def nextGreaterElements(self, nums):
        dp = [-1] * len(nums)
        stack = []
        for i in range(len(nums)*2):
            while(len(stack) != 0 and nums[i%len(nums)] > nums[stack[-1]]):    #取余
                    dp[stack[-1]] = nums[i%len(nums)]
                    stack.pop()
            stack.append(i%len(nums))
        return dp
    
