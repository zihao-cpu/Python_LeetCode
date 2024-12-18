#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   建造最大岛屿.py
@Time    :   2024/12/18 19:48:03
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
import collections
directions = [(0,1),(0,-1),(1,0),(-1,0)] #四个方向
area=0
def dfs(grid,x,y,visited,num):
    global area
    if visited[x][y]:
        return 
    visited[x][y]=True
    grid[x][y]=num
    area +=1
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if nx<0 or nx>=len(grid) or ny<0 or ny>=len(grid[0]):
            continue
        if grid[nx][ny]==1:
            visited[nx][ny]=True
            dfs(grid,nx,ny,visited,num)
def main1():
    n,m=map(int,input().split())
    grid=[]
    for i in range(n):
        grid.append(list(map(int,input().split())))
    Visited=[[False for j in range(m)] for i in range(n)]
    rec = collections.defaultdict(int)
    cnt=2
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1:
                area=0
                dfs(grid,i,j,Visited,cnt)
                rec[cnt]=area
                cnt+=1

    res=0
    for i in range(n):
        for j in range(m):
            if grid[i][j]==0:
                max_island=1
                v=set()
                for dx,dy in directions:
                    nx,ny=i+dx,j+dy
                    if  nx<0 and nx>=len(grid) and ny<0 and ny>=len(grid[0]) and grid[nx][ny]!=0 and grid[nx][ny] not in v:
                        max_island+=rec(grid[nx][ny])
                        v.add(grid[nx][ny])
        
                res=max(res,max_island)

    if res==0:
        return max(rec.values())
    return res

if __name__ == '__main__':
    print(main1())