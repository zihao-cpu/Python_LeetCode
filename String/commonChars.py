#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   commonChars.py
@Time    :   2024/09/24 10:56:41
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def commonChars(self,strList:list[str])->list[str]:
        hash0=[0]*26  #数组实现哈希表
        result=[]
        for i,c in enumerate(strList[0]):
            hash0[ord(c)-ord('a')]+=1
        for i in range(1,len(strList)):
            hashtemp=[0]*26
            for j in strList[i]:
                hashtemp[ord(j)-ord('a')]+=1
            for k in range(0,26):
                hash0[k]=min(hash0[k],hashtemp[k])
        

        for i in range(0,26):
            while hash0[i]!=0:
                result.append(chr(i+ord('a')))
                hash0[i]-=1

        return result
    
    def commonChars(self,strList:list[str])->list[str]:
        from collections import Counter
        result=[]
        hash0=Counter(strList[0])
        for i in range(1,len(strList)):
            hash0=hash0&Counter(strList[i])
        for i in hash0:
            v=hash0[i]

            while v!=0:
                result.append(i)
                v-=1

        return result
