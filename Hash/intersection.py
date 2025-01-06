#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   intersection.py
@Time    :   2024/09/24 11:24:06
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def intersection(self,nums1: list[int], nums2: list[int]) -> list[int]:
        from collections import Counter
        result=[]
        hash1=Counter(nums1)
        hash2=Counter(nums2)
        hash1_2=hash1 & hash2
        for j in hash1_2:
            if hash1_2[j]!=0:
                result.append(j)
        return result
    def intersection(self,nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1)&set(nums2))