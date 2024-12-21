#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   岛屿周长.py
@Time    :   2024/12/21 22:30:58
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
def main1():
    n,m=map(int,input().split())
    grid=[]
    for i in range(n):
        grid.append(list(map(int,input().split())))
    sum_island,cover=0,0
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1:
                sum_island+=1
                if i-1>=0 and grid[i-1][j]==1:
                    cover+=1
                if j-1>=0 and grid[i][j-1]==1:
                    cover+=1
#只算左侧和上侧的岛屿，为什么？循环 下去 会重复计算
    result=sum_island*4-cover*2