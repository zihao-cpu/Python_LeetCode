#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   reverse2.py
@Time    :   2024/09/26 15:05:19
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
'''

每次移动2*k


'''
class Solutoin():
    def reverse2(self,str1,k:int):
        def reverse(text):
            left,right=0,len(text)-1
            while left<right:
                text[left],text[right]=text[right],text[left]
                left+=1
                right-=1
            return text
        res=list(str1)
        for cur in range(0,len(res),2*k):
            res[cur,cur+k]=reverse(res[cur,cur+k])
        return ''.join(res)