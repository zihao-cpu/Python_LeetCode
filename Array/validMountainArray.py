#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   validMountainArray.py
@Time    :   2025/01/07 15:37:05
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''

class Solution:
    def validMountainArray(self, arr)-> bool:
        left=0
        right=len(arr)-1
        while left<len(arr)-1 and arr[left]<arr[left+1]:
            left+=1
        while right>0 and arr[right]>arr[right-1]:  
            right-=1
        return left==right and left!=0 and right!=len(arr)-1  #在中间相遇
        
            
