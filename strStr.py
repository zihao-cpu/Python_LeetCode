#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   strStr.py
@Time    :   2024/09/27 10:52:00
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
'''
KMP 算法
找到 前缀数组

'''


class Soulution():
    def getNext(self,next:list[int],s:str)->None:
        j=0
        next[0]=0
        for i in range(1,len(s)):

            while j>0 and s[i]!=s[j]:
                j=next[j-1]
            if s[i]==s[j]:
                j+=1
            next[i]=j
    def strStr(self,haystack:str,needle:str)->int:
        if len(needle)==0:
            return 0
        next=[0]*len(needle)
        self.getNext(next,needle)
        j=0
        for i in range(len(haystack)):
            while j>0 and haystack[i]!=needle[j]:
                j=needle[j-1]
            if haystack[i]==needle[j]:
                j+=1
            if j==len(needle):
                return i-len(needle)+1
        return -1