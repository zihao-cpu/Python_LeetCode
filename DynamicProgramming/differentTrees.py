#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   differentTrees.py
@Time    :   2024/11/01 22:16:35
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    """定义一个解决方案类用于计算不同的二叉树数量."""
     
    def differentTrees(self, n: int) -> int:
        """计算能够构造的不同二叉树的数量.
         
        参数:
        n : int : 节点的数量
         
        返回:
        int : 不同二叉树的数量
        """
        dp=[0]*(n+1)
        dp[0]=1
        for i in range(1,n+1):
            for j in range(1,i+1):
                dp[i]+=dp[i-j]*dp[j-1]
 
        return dp[n]
if __name__ == '__main__':
    s = Solution()
    print(s.differentTrees(3)) # 5
    print(s.differentTrees(1)) # 1  