#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   findAbscendSubsets.py
@Time    :   2024/10/23 15:50:07
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''


class Solution():
    def findAbscendSubsets(self,nums):
        result =[]
        path=[]
        self.backtracking(nums,0,[],result)
        return result



    def backtracking(self,nums,startIndex,path,result):
        
        used=set()

        if len(path)>1:
            result.append(path[:])#不放 这里会漏掉自己
            return  

        for i in range(startIndex,len(nums)):
            if (path and nums[i]<path[-1]) or nums[i] in used:
                continue

            used.add(nums[i])
            
            path.append(nums[i])
      
            self.backtracking(nums,i+1,path,result)

            path.pop()


new =Solution()
result=new.findAbscendSubsets([6,7,7])
