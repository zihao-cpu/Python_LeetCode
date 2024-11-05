#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   findMaxSubset.py
@Time    :   2024/11/05 17:26:25
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution:
    #二维动态规划 其实是第一个维度遍历物品，第二个维度遍历背包，此时是两个背包
    def findMaxSubset(self, strs,m,n) -> int:
        dp=[[[0]*(n+1) for _ in range(m+1)] for _ in range(len(strs))]
        nums_of_zeros=[0]*len(strs)
        nums_of_ones=[0]*len(strs)
        for i in range(len(strs)):
            str=strs[i]
            nums_of_zeros[i]=str.count('0')
            nums_of_ones[i]=str.count('1')
        if nums_of_zeros[0]<=m and nums_of_ones[0]<=n:  #初始化
            for i in range(nums_of_zeros[0],m+1):
                for j in range(nums_of_ones[0],n+1):
                    dp[0][i][j]=1#初始化
        for i in range(1,len(strs)):
            cur_zeros=nums_of_zeros[i]
            cur_ones=nums_of_ones[i]
            for j in range(0,m+1):
                for k in range(0,n+1):
                    if j<cur_zeros or k<cur_ones:
                        dp[i][j][k]=dp[i-1][j][k]
                    else:
                        dp[i][j][k]=max(dp[i-1][j][k],dp[i-1][j-cur_zeros][k-cur_ones]+1)
        return dp[len(strs) - 1][m][n]    #返回最大子集大小

    #改写成一维动态规划
    def findMaxSubset2(self, strs,m,n) -> int:
        dp=[[0]*(n+1) for _ in range(m+1)] 
        for str in strs:
            cur_zeros=str.count('0')
            cur_ones=str.count('1')
            for j in range(m,cur_zeros-1,-1):#详细看一维度倒序遍历
                for k in range(n,cur_ones-1,-1):
                    dp[j][k]=max(dp[j][k],dp[j-cur_zeros][k-cur_ones]+1) #这个加一就相当于物品的value
        return dp[m][n]    #返回最大子集大小


class Solution:
    def findMaxForm(self, strs, m: int, n: int) -> int:
        num_of_str = len(strs)

        # 创建三维动态规划数组
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(num_of_str)]

        # 记录每个字符串的 0 和 1 的数量
        num_of_zeros = []
        num_of_ones = []
        for str in strs:
            count_of_zero = str.count('0')
            count_of_one = str.count('1')
            num_of_zeros.append(count_of_zero)
            num_of_ones.append(count_of_one)
        
        # 初始化第一层 dp[0][j][k]
        if num_of_zeros[0] <= m and num_of_ones[0] <= n:
            for j in range(num_of_zeros[0], m + 1):
                for k in range(num_of_ones[0], n + 1):
                    dp[0][j][k] = 1
        
        # 填充 dp 数组
        for i in range(1, num_of_str):
            count_of_zeros = num_of_zeros[i]
            count_of_ones = num_of_ones[i] 
            for j in range(m + 1):
                for k in range(n + 1):
                    if j < count_of_zeros or k < count_of_ones:
                        dp[i][j][k] = dp[i - 1][j][k]
                    else:
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - count_of_zeros][k - count_of_ones] + 1)
        
        # 返回结果
        return dp[num_of_str - 1][m][n]
if __name__ == '__main__':
    strs=["1010","1110","1101","1010","1011","0111","0011","1111"]
    m=5  #m为0-5
    n=3  #n为1-3
    s=Solution()
    print(s.findMaxForm(strs,m,n))    