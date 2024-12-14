#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   沉没孤岛.py
@Time    :   2024/12/14 12:15:41
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
directions = [(0,1),(0,-1),(1,0),(-1,0)] #四个方向
def dfs(grid,x,y):
    grid[x][y]=2 #标记为已访问
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if nx<0 or nx>=len(grid) or ny<0 or ny>=len(grid[0]):
            continue
        if grid[nx][ny]==2 or grid[nx][ny]==0:
            continue
        dfs(grid,nx,ny)


def bfs(grid,x,y):
    from collections import deque
    q=deque()
    q.append([x,y])
    while q:
        cur_x,cur_y=q.popleft()
        grid[cur_x][cur_y]=2 #标记为已访问
        for dx,dy in directions:
            nx,ny=cur_x+dx,cur_y+dy
            if nx<0 or nx>=len(grid) or ny<0 or ny>=len(grid[0]):
                continue
            if grid[nx][ny]==1:
                q.append([nx,ny])
                grid[nx][ny]=2 #标记为已访问

        
def main1():
    n,m=map(int,input().split())
    grid=[]
    for i in range(n):
        grid.append(list(map(int,input().split())))
    for i in range(n):
        if grid[i][m-1]==1: dfs(grid,i,m-1)
        if grid[i][0]==1:dfs(grid,i,0)

    for i in range(m):
        if grid[0][i]==1: dfs(grid,0,i)
        if grid[n-1][i]==1:dfs(grid,n-1,i)
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                grid[i][j] = 0
            if grid[i][j] == 2:
                grid[i][j] = 1  

def main2():
    n,m=map(int,input().split())
    grid=[]
    for i in range(n):
        grid.append(list(map(int,input().split())))
    for i in range(n):
        if grid[i][m-1]==1: bfs(grid,i,m-1)
        if grid[i][0]==1:bfs(grid,i,0)

    for i in range(m):
        if grid[0][i]==1: bfs(grid,0,i)
        if grid[n-1][i]==1:bfs(grid,n-1,i)
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                grid[i][j] = 0
            if grid[i][j] == 2:
                grid[i][j] = 1 
     