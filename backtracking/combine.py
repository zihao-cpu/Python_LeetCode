#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   combine.py
@Time    :   2024/10/19 11:38:17
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def combine(self,n,k):

        result=[]
        self.backtracking(n,k,1,[],result)
        return result
    
    def backtracking(self,n,k,startIndex,path,result):
        if len(path)==k:
            result.append(path[:])
            return
        
        for i in range(startIndex,n+1):
            path.append(i)
            self.backtracking(n,k,i+1,path,result)
            path.pop()

