#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   unique.py
@Time    :   2025/01/07 15:45:20
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''

class Solution:
    def unique(self, nums) -> bool:
        record=dict()
        for num in nums:
            if num in record:   
                record[num]+=1
            else:
                record[num]=1
        values=list(record.values())
        return len(values)==len(set(values))