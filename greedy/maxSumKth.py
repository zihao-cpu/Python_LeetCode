#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   maxSumKth.py
@Time    :   2024/10/25 18:58:14
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''

class Solution():
    def maxSumKth(self,nums,k):
        #O(Nlogn)
        if k==0:return sum(nums)
        while k>0:
            nums_diff=[-i-i for i in nums]
            max_diff=max(nums_diff)
            
            nums[nums_diff.index(max_diff)]=-nums[nums_diff.index(max_diff)]
            k-=1 
        return sum(nums)
    


    def maxSumKth(self,nums,k):
        #O(N)?
        nums.sort(key=lambda x:abs(x), reverse=True)
        for i in range(len(nums)):
            if nums[i]<0 and k>0:
                nums[i]*=-1
                k-=1
        if k%2==1:
            nums[-1]*=-1
        return sum(nums)
