#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   moveZeros.py
@Time    :   2025/01/11 14:00:53
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
def moveZeros(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    slow=0
    for fast in range(len(nums)):

        if nums[fast]!=0:
            nums[slow]=nums[fast]
            slow+=1

            
    for i in range(slow,len(nums)):
        nums[i]=0