#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   nextGreaterElement.py
@Time    :   2024/11/27 16:30:48
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        result=[-1]*len(nums1)
        stcak=[0]
        for i in range(1,len(nums2)):
            if nums2[i]<=nums2[stcak[-1]]:
                stcak.append(i)
            else:
                while len(stcak)>1 and nums2[i]>nums2[stcak[-1]]:
                    if nums2[stcak[-1]] in nums1:
                        result[nums1.index(nums2[stcak[-1]])]=nums2[i]
                    stcak.pop()
                stcak.append(i)
        return result