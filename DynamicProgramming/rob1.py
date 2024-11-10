#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   rob1.py
@Time    :   2024/11/10 19:30:02
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def rob1(self, nums):
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for j in range(2,len(nums)):
            dp[j]=max(dp[j-1],dp[j-2]+nums[j])  #选择当前的房屋和不选择当前房屋的最大值。
        return dp[-1]
if __name__ == '__main__': 
    nums=[2,3,2]
    s=Solution()
    print(s.rob1(nums)) 