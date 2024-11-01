#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   fib.py
@Time    :   2024/11/01 15:30:44
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def fib(self, n: int) -> int:

        # 计算斐波那契数列第 n 项的函数
        if n == 0:
            return 0
        dp=[0]*(n+1) # 定义一个数组，用于存储斐波那契数列
        dp[0]=0# 第一个数为0
        dp[1]=1# 第二个数为1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]# 计算第 i 个数
        return dp[n]