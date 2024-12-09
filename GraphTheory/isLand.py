#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   isLand.py
@Time    :   2024/12/06 20:24:48
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution:
    #深度搜索
    def __init__(self):
        self.directions = [(0,1),(0,-1),(1,0),(-1,0)] #四个方向
    def dfs(self,grid,visited,x,y):
        for dx,dy in self.directions:
            nx,ny=x+dx,y+dy
            if nx<0 or nx>=len(grid) or ny<0 or ny>=len(grid[0]):
                continue
            if grid[nx][ny]==1 and not visited[nx][ny]:
                visited[nx][ny]=True
                self.dfs(grid,visited,nx,ny)
    #广度搜索
    def bfs(self,grid,visited,x,y):
        from collections import deque
        q=deque()
        q.append([x,y])
        while q:
            cur_x,cur_y=q.popleft()
            for dx,dy in self.directions:
                nx,ny=cur_x+dx,cur_y+dy
                if nx<0 or nx>=len(grid) or ny<0 or ny>=len(grid[0]):
                    continue
                if grid[nx][ny]==1 and not visited[nx][ny]:
                    visited[nx][ny]=True
                    q.append([nx,ny])

    def main(self):
        n,m=map(int,input().split())
        grid=[]
        for i in range(n):
            grid.append(list(map(int,input().split())))
        visited=[[False for j in range(m)] for i in range(n)]
        res1=0
        res2=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and not visited[i][j]:
                    res1+=1
                    visited[i][j]=True
                    self.dfs(grid,visited,i,j)

                    res2+=1
                    self.bfs(grid,visited,i,j)
