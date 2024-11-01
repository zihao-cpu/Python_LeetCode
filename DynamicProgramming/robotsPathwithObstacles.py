#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   robotsPathwithObstacles.py
@Time    :   2024/11/01 16:14:45
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def robotPathwithObstacles(self, grid):
        m=len(grid)
        n=len(grid[0])
        dp=[[0]*n for i in range(m)]
        for i in range(m):
            if grid[i][0]==1:
                break
            else:
                dp[i][0]=1
        for i in range(n):
            if grid[0][i]==1:
                break
            else:
                dp[0][i]=1
        for i in range(1,m):
            for j in range(1,n):
                if grid[i][j]==1:
                    continue
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
    
if __name__ == '__main__':
    grid=[[0,0,0],[0,1,0],[0,0,0]]
    print(Solution().robotPathwithObstacles(grid))   # Output: 2    