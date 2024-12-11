#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   islandArea2.py
@Time    :   2024/12/11 16:59:22
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''



directions = [(0,1),(0,-1),(1,0),(-1,0)] #四个方向

#广度搜索
def bfs(x,y):
    from collections import deque
    q=deque()
    q.append([x,y])
    global count
    grid[x][y] = 0
    count+=1
    while q:
        cur_x,cur_y=q.popleft()
        for dx,dy in directions:
            nx,ny=cur_x+dx,cur_y+dy
            if nx<0 or nx>=len(grid) or ny<0 or ny>=len(grid[0]):
                continue
            if grid[nx][ny]==1:
                q.append([nx,ny])
                grid[nx][ny]=0
                count+=1
            


n, m=map(int,input().split())
grid=[]
for i in range(n):
    grid.append(list(map(int,input().split())))

for i in range(n):
    if grid[i][m-1]==1: bfs(i,m-1)
    if grid[i][0]==1:bfs(i,0)

for i in range(m):
    if grid[0][i]==1: bfs(0,i)
    if grid[n-1][i]==1:bfs(n-1,i)

count=0
for i in range(m):
    for j in range(n):
        if grid[i][j]==1:
            bfs(i,j)
print(count)