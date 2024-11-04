#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   findTargetSumWays.py
@Time    :   2024/11/04 14:29:02
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def findTargetSumWays(self, nums, S):
        #这是一道典型的动态规划问题，我们可以用回溯法来解决。
        #我们可以从第一个元素开始，对于每个元素，我们可以选择是否加到当前的和中，然后递归地求解剩下的元素和当前的和的组合。
        #如果当前元素不加，那么就递归地求解剩下的元素和当前的和的组合。如果当前元素加，那么就递归地求解剩下的元素和当前的和的组合，
        #并且当前元素的数量也要加一。
        #当我们递归到最后一个元素时，如果当前的和等于目标值，那么我们就找到了一个组合，我们就返回1，否则就返回0。
        return self.backtrack(nums, 0, S, 0, 0)
    def backtrack(self,nums,start, target, curr_sum, count):  
        if start == len(nums):
            return count + 1 if curr_sum == target else count
        count = self.backtrack(nums,start+1, target, curr_sum+nums[start], count)#加当前元素
        count = self.backtrack(nums,start+1, target, curr_sum-nums[start], count)#不加当前元素
        return count
        
     #也可以是另一种回溯的方法，这种方法更加简洁。
     #left-right=target
     #left+right=sum(nums)
     #right=sum(nums)-left
     #left=(sum(nums)+target)//2       
    def findTargetSumWays2(self, nums, S):
        total_sum = sum(nums)
        if total_sum < S or (total_sum+S)%2!= 0:
            return 0
        target = (total_sum+S)//2
        dp=[[0]*(target+1) for _ in range(len(nums))]
        
        numSize=0
        #初始化第一列
        for i in range(len(nums)):
            if nums[i]==0:
                numSize+=1
                dp[i][0]=pow(2,numSize)
        #初始化第一行
        if nums[0]<=target:
            dp[0][nums[0]]=1
        dp[0][0]=1
            
        for i in range(1,len(nums)):  #遍历每一个物品
            for j in range(target+1): #遍历每一个容量 d[i][j]表示前i个物品恰好装入（装满）一个容量为j的背包有多少种方法
                if j-nums[i-1]<0:    #如果当前元素大于目标值，则不加当前元素
                    dp[i][j]=dp[i-1][j]
                else: 
                    dp[i][j]=dp[i-1][j]+dp[i-1][j-nums[i-1]] #dp[2][2] = 容量为2的背包不放物品2有几种方法 + 容量为2的背包放物品2有几种方法
        # return dp[len(nums)][target]
        return dp[-1][-1]
if __name__ == '__main__':  
    nums = [1, 1, 1, 1, 1]
    S = 3   
    solution = Solution()
    print(solution.findTargetSumWays(nums, S)) # Output: 5  
    print(solution.findTargetSumWays2(nums, S)) # Output: 5


