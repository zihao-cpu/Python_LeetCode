#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   merge.py
@Time    :   2024/10/30 19:59:51
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def merge(self,nums):
        nums.sort(key=lambda x:[x[0]])
        result=[]
        result.append(nums[0])
        for i in range(1,len(nums)):
            if result[-1][1]>=nums[i][0]:
                result[-1][1]=max(result[-1][1],nums[i][1])
            else:
                result.append(nums[i])