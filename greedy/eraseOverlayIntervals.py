#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   eraseOverlayIntervals.py
@Time    :   2024/10/29 17:05:29
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def eraseOverlayIntervals(self,nums):
        nums.sort(key=lambda x:[x[0]])
        max_right=nums[0][1]
        result=1
        for i in range(1,len(nums)):
            if nums[i][0]>=nums[i-1][1]:
                result+=1
            else:
                nums[i][1]=min(nums[i][1],nums[i-1][1])
        return len(nums)-result      