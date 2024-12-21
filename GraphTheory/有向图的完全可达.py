#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   有向图的完全可达.py
@Time    :   2024/12/21 20:16:54
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''

import collections
path=set()


def bfs(root,graph):
    global path
    que=collections.deque(root)
    while que:
        cur=que.popleft()
        path.append(cur)
        for nei in graph[cur]:
            que.append(nei)
        graph[cur]=[]
    return


def main():
    n, m=map(int,input().split())
    graph=collections.defaultdict(list)
    for _ in range(m):
        src,dest= map(int,input().strip().split())
        graph[src].append(dest)
    bfs(1,graph)
    if path=={i for i in range(1,n+1)}:
        return 1
    return -1



def dfs(graph,key,visited):
    for nei in graph[key]:
        if not visited[nei]:
            visited[nei]=True
            dfs(graph,key,visited)

def main1():
    n, m=map(int,input().split())
    graph=collections.defaultdict(list)
    for _ in range(m):
        src,dest= map(int,input().strip().split())
        graph[src].append(dest)
    visited=[False]*(n+1)
    visited[1]=True
    dfs(graph,1,visited)
    for i in range(1,n+1):
        if not visited[i]:
            print(-1)
            return
    print(1)