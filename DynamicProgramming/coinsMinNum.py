#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   coinsMinNum.py
@Time    :   2024/11/07 15:59:52
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution:
    def coinMinNum(self, coins, amount) -> int:
        dp=[[float('inf')]*(amount+1)]*(len(coins)+1)#这里初始化为什么是无穷大呢？


# 表示不可达状态：
# 初始时，我们还没有计算出凑成某个金额所需的硬币数量，因此可以认为所有金额（除了0）是不可达的。
# 使用无穷大（float('inf')）作为初始值能够有效地表示这一点。

# 便于比较：
# 当我们在动态规划过程中计算得到某个金额的最小硬币数时，我们需要与当前存储的最小值进行比较。如果初始值是一个很大的数（如无穷大），
# 那么任何实际计算得到的值都会更小，这样在更新dp数组时能够正确维护最低要求的硬币数。

# 边界条件：
# 当目标金额为0时，所需的硬币数显然是0，这个条件在后续的代码中会被特别处理。因此，除了金额0以外的所有金额在初始时都设为无穷大，
# 以便后续的计算能够正确反映出最优解
        for i in range(amount+1):
            if i % coins[0] == 0:
                dp[0][i] = i//coins[0] 
        for i in range(1,len(coins)):
            for j in range(1,amount+1):
                if j<coins[i]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-coins[i]]+1)
        return dp[-1][-1]
if __name__ == '__main__':  
    coins = [1]
    amount = 11
    print(Solution().coinMinNum(coins, amount)) 


