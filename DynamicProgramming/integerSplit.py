#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   integerSplit.py
@Time    :   2024/11/01 21:52:08
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution:
    def integerSplit(self, num: int) -> int:

         # 假设对正整数 i 拆分出的第一个正整数是 j（1 <= j < i），则有以下两种方案：
        # 1) 将 i 拆分成 j 和 i−j 的和，且 i−j 不再拆分成多个正整数，此时的乘积是 j * (i-j)
        # 2) 将 i 拆分成 j 和 i−j 的和，且 i−j 继续拆分成多个正整数，此时的乘积是 j * dp[i-j]
        dp = [0] * (num+1)
        dp[2] =1 
        for i in range(3,num+1):
            for j in range(1,i):
                dp[i]=max(dp[i-j]*j,(i-j)*j,dp[i])
        return dp[num]
if __name__ == '__main__':
    num = 10
    print(Solution().integerSplit(num)) # Output: 36
