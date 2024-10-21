#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   partition.py
@Time    :   2024/10/21 20:37:20
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def partition(self,s):
        result=[]

        path=[]

        self.backtracking(s,0,result,path)
        return result 
    

    

    def is_palindrome(s,left,right):
        while(left<right):
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True
    


    def backtracking(self,s,startIndex,path,result):
        if startIndex==s:
        
            result.append(path[:])
            return
        
        for i in range(startIndex,len(s)):

            if self.is_palindrome(s,startIndex,i):
                path.append(s[startIndex,i+1])
                self.backtracking(s,i+1,path,result)
                path.pop()
