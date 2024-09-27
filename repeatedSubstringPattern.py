#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   repeatedSubstringPattern.py
@Time    :   2024/09/27 13:56:24
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def repeatedSubstringPattern(self,s:str)->bool:
        if len(s)==0:
            return False
        next=[0]*len(s)
        self.getNext(next,s)
        if next[-1] !=0 and len(s)%(len(s)-next[-1])==0:
            return True
        return False
    
    def getNext(self,next:list[int],s:str)->None:
        j=0
        next[0]=0
        for i in range(1,len(s)):

            while j>0 and s[i]!=s[j]:
                j=next[j-1]
            if s[i]==s[j]:
                j+=1
            next[i]=j