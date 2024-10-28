#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   suger.py
@Time    :   2024/10/28 19:08:37
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''

class Solution():
    def suger(self,nums):
        sugers=[1]*len(nums)

        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                sugers[i]=sugers[i-1]+1
        for i in range(len(nums),-1,-1):
            if nums[i]>nums[i+1]:
                sugers[i]=max(sugers[i],sugers[i+1]+1)
        return sum(sugers)
    

