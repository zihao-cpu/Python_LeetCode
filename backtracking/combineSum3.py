#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   combineSum3.py
@Time    :   2024/10/19 11:48:12
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def combineSum3(self,n,k):

        result=[]
        self.backtracking(n,k,1,0,[],result)
        return result
    
    def backtracking(self,n,k,startIndex,currentSum,path,result):
        if len(path)==k:
            if currentSum==k:
                result.append(path[:])
            return
        
        for i in range(startIndex,n+1):
            currentSum+=i
            path.append(i)
            self.backtracking(n,k,i+1,currentSum,path,result)
            currentSum-=i
            path.pop()