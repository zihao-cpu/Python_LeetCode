#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   threeSum.py
@Time    :   2024/09/24 15:35:33
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
'''
哈希法 双指针
'''
class Solution():
    def threeSum(self,nums:list[int])->list[list[int]]:
        result=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]: #a 去重
                continue
            
            d={}
            for j in range(i+1,len(nums)):
                if j>i+2 and nums[j]==nums[j-1]==nums[j-2]: #b 去重
                    continue
                c=0-(nums[i]+nums[j])
                if c in d:
                    result.append([nums[i],nums[j],c])
                    d.pop(c)  #c 去重  
                else:
                    d[nums[j]]=j
        return result
    
    def threeSum(self,nums:list[int])->list[list[int]]:
        result=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]: #a 去重
                continue 
            left=i+1
            right=len(nums)-1

            while right>left:
                sum_=nums[i]+nums[left]+nums[right]
                if sum_<0:
                    left+=1
                elif sum_>0:
                    right-=1
                else:
                    result.append[nums[i],nums[left],nums[right]]
                    while right>left and nums[right]==nums[right-1]:
                        right-=1
                    while right>left and nums[left]==nums[left+1]:
                        left+=1
                    right-=1
                    left+=1
        return result
                





