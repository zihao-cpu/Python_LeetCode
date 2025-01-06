#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   smallerNumbersThanCurrent.py
@Time    :   2025/01/06 20:44:34
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        hash=dict()
        res=nums.copy()
        res.sort()

        for i,num in enumerate(res):
            if num not in hash:
                hash[num]=i
        for i,num in enumerate(nums):
            res[i]=hash[num]  
        return res
