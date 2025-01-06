#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   reverse.py
@Time    :   2024/09/26 14:38:27
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def reverse(self,str1: list[str])-> list[str]:
        left,right=0,len(str1)-1
        while left<right:
            str1[left],str1[right]=str1[right],str1[left]
            left+=1
            right-=1
        return str1



    def reverse(self,str1: list[str])->list[str]:
        stack=[]
        for char in str1:
            stack.append[char]
        for i in range(len(str1)):
            str1[i]=stack.pop()
        return str1
