#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   twoSum.py
@Time    :   2024/09/24 15:05:14
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def twoSum(self,nums:list[int],target:int)->list[int]:
        record=dict()
        for index,value in enumerate(nums):
            if target-value in record:
                return [record[target-value],index]
            record[value]=index  #把查看过的数据放入字典
        return []
    
    def twoSum(self,nums:list[int],target:int)->list[int]:
        record=set()
        for index,value in enumerate(nums):
            if target-value in record:
                return [nums.index[target-value],index]
            record.add(value)   #把查看过的数据放入集合