#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   maxProfit.py
@Time    :   2024/10/25 14:23:29
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def maxProfile(self,nums):
        result=0
        for i in range(1,len(nums)):
            result+=max(nums[i]-nums[i-1],0) 
        return result