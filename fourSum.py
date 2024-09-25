#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   fourSum.py
@Time    :   2024/09/24 18:33:15
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def fourSum(self,nums:list[int],target:int)->list[list[int]]:
        result=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]>target:
                break

            if i>0 and nums[i]==nums[i-1]:
                continue

            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]>target:
                    break

                if j>i+1 and nums[j]==nums[j-1]:
                    continue

                
                left,right=j+1,len(nums)-1
                while  right>left:
                    s=nums[i]+nums[j]+nums[left]+nums[right]
                    if s==target:
                        result.append([nums[i],nums[j],nums[left],nums[right]])
                        while left<right and nums[left]==nums[left+1]:
                            left+=1
                        while left<right and nums[right]==nums[right-1]:
                            right-=1
                        left+=1
                        right-=1
                    elif s< target:
                        left+=1
                    else:
                        right-=1
        return result
                    
                
