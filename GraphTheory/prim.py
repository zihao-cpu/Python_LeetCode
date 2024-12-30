#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   prim.py
@Time    :   2024/12/30 21:56:18
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
def prim(v,e,edges):
    import heapq
    import sys
    grid =[[10001]*(v+1) for _ in range(v+1)]
    for edge in edges:
        grid[edge[0]][edge[1]] = edge[2]
        grid[edge[1]][edge[0]] = edge[2]
    minDist=[10001]*(v+1)
    isInTree=[False]*(v+1)
    for i in range(1,v):
        cur=-1
        minVal=sys.maxsize

        # 选择距离最小的节点
        for j in range(1,v+1):
            if not isInTree[j] and minDist[j]<minVal:
                minVal=minDist[j]
                cur=j
        isInTree[cur]=True
        
        # 更新距离
        for j in range(1,v+1):
            if not isInTree[j] and grid[cur][j]<minDist[j]:
                minDist[j]=grid[cur][j]
        

