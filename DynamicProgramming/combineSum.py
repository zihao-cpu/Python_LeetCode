#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   combineSum.py
@Time    :   2024/11/06 20:25:41
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def combineSum(self, nums, target):
        dp=[0]*(target+1)
        dp[0]=1
        for j in range(1, target+1): #排列问题遍历背包先
            for i in range(len(nums)):                
                if j>=nums[i]:
                    dp[j]+=dp[j-nums[i]]    
        return dp[target]
    
    def combineSum2(self, nums, target):
        dp=[[0]*(target+1) for i in range(len(nums))]
        for i in range(len(nums)):
            dp[i][0]=1
        for j in range(1, target+1): #排列问题遍历背包先
            for i in range(len(nums)):                
                if j>=nums[i]:
                    dp[i][j]=dp[i-1][j]+dp[-1][j-nums[i]] #对于和为j 的组合，只有试过了所以的数才知道有几种排列  
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[-1][-1]
if __name__ == '__main__':
    nums=[2,3,6,7]
    target=7
    s=Solution()    
    print(s.combineSum(nums, target))
    print(s.combineSum2(nums, target))  