#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   rob2.py
@Time    :   2024/11/10 21:32:55
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution:
    def rob2(self, nums) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        #偷1
        dp=[0]*(len(nums)-1)
        dp[0]=nums[0]
        dp[1]=nums[0]
        for j in range(2,len(nums)-1):
            dp[j]=max(dp[j-1],dp[j-2]+nums[j])  #选择当前的房屋和不选择当前房屋的最大值.
 
        #不偷1
        result1=dp[-1]
        dp=[0]*(len(nums)-1)
        dp[0]=nums[1]
        dp[1]=max(nums[1],nums[2])
        for j in range(2,len(nums)-1):
            dp[j]=max(dp[j-1],dp[j-2]+nums[j+1])  #选择当前的房屋和不选择当前房屋的最大值.
        result2=dp[-1]
        
        print(result1,result2)  
        return max(result1,result2)
if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,5,1]
    print(s.rob2(nums))
    nums = [2,7,9,3,1]
    print(s.rob2(nums))
    nums = [1,2,3,4,5,6,7,8,9,10]
    print(s.rob2(nums))

