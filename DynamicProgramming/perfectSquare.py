#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   perfectSquare.py
@Time    :   2024/11/08 20:10:14
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution:
    def PerfectSquare(self, num: int):
        max_num=int(pow(num,0.5))
        dp=[[float('inf')]*(num+1)]*(max_num+1)
        dp[0][0]=0#0的平方是0  0~max_num的平方和是0~max_num*max_num

        for j in range(1,num+1):  #遍历背包      这里是排列的问题 先便利背包 而且这完全背包
            for i in range(1,max_num+1):#遍历物品
                if j<pow(i,2):
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i-1][j-pow(i,2)]+1)
        return dp[-1][-1]
    


    def PerfectSquare2(self, num: int):
        max_num=int(pow(num,0.5))
        dp=[float('inf')]*(num+1)
        dp[0]=0#0的平方是0  0~max_num的平方和是0~max_num*max_num
        for j in range(1,num+1):    #遍历背包      这里是排列的问题 先便利背包 而且这完全背包   物品的范围是1~max_num
            for i in range(1,max_num+1):#遍历物品
                dp[j] = min(dp[j], dp[j - i * i] + 1)
        return dp[-1]   

if __name__ == '__main__':
    s=Solution()
    print(s.PerfectSquare(1))  
    print(s.PerfectSquare2(1)) 
    print(s.PerfectSquare(66)) 
    print(s.PerfectSquare2(66))  

