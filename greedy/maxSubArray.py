#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   maxSubArray.py
@Time    :   2024/10/24 16:51:11
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def maxSubArray(self,nums):
        result=float('-inf')

        count=0
        for i in range(len(nums)):
            count+=nums[i]

            if count>result:
                result=count
            if count<=0:
                count=0
        return count