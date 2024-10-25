#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   winggleMaxLength.py
@Time    :   2024/10/24 16:29:50
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def winggleMaxlength(self,nums):
        if len(nums)<=1:return len(nums)

        curDiff=0
        preDiff=0
        result=0
        for i in range(len(nums)-1):
            curDiff=nums[i+1]-nums[i]
            if (preDiff>=0 and curDiff<0) or (preDiff<=0 and curDiff>0):
                result+=1
                preDiff=curDiff   #只有在摆动的时候更新
        return result