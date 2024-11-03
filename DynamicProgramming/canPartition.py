#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   canPartition.py
@Time    :   2024/11/03 16:57:48
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    #这是一个01背包问题，即是否可以将数组中的元素分成两组，使得两组的和相等。
    #我们可以用动态规划来解决这个问题。
    #设dp[i][j]表示前i个元素能否分成j组，则有如下递推式：
    #dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
    #即，如果不分组，则dp[i][j]取决于dp[i-1][j]；如果分组，则dp[i][j]取决于dp[i-1][j-nums[i-1]]。
    def canPartition(self, nums):
        taget_num=sum(nums)//2
        if taget_num*2!=sum(nums): #如果数组元素和为奇数，则无法分成两组
            return False
        dp=[[False]*(taget_num+1) for _ in range(len(nums)+1)]
        for i in range(len(nums)+1): #初始化第一
            dp[i][0]=True


        for i in range(1,len(nums)+1):
            for j in range(1,taget_num+1):
                if j< nums[i-1]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-nums[i-1]]#如果我们能够通过选择或不选择第 i 个元素来构成和为 j 的子集，那么 dp[i][j] 就为 True；否则为 False
        return dp[len(nums)][taget_num]
if __name__ == '__main__':
    nums=[1,5,11,5]
    print(Solution().canPartition(nums))        