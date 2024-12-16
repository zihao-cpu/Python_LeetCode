#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   水流问题.py
@Time    :   2024/12/16 15:25:34
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
directions = [(0,1),(0,-1),(1,0),(-1,0)] #四个方向
first=set()
second=set()

def dfs(grid,visit,x,y,side):
    if visit[x][y]:
        return
    visit[x][y]=True
    side.add((x,y))
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if (0<=nx<len(grid) and 0<=ny<len(grid[0]) and int(grid[nx][ny])>= int(grid[x][y])):
            dfs(grid,visit,nx,ny,side)
def main1():
    n,m=map(int,input().split())
    grid=[]
    for i in range(n):
        grid.append(list(map(int,input().split())))
    visit = [[False] * m for _ in range(n)]
    for i in range(m):
        dfs(grid,visit,0,i,first)
    for i in range(n):
        dfs(grid,visit,i,0,first)
    for i in range(m):
        dfs(grid,visit,n-1,i,second)
    for i in range(n):
        dfs(grid,visit,i,m-1,second)
        
result=first & second    