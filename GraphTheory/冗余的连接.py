#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   冗余的连接.py
@Time    :   2024/12/26 16:56:30
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class  UnionFind:
    def __init__(self,size):
        self.parent=list(range(size+1))
    def find(self,u):
        if self.parent[u]!=u:
            self.parent[u]=self.find(self.parent[u])
        return self.parent[u]

    def union(self,u,v):
        root_u=self.find(u)
        root_v=self.find(v)
        if root_u!=root_v:
            self.parent[root_u]=root_v 

    def is_same(self,u,v):
        return self.find(u)==self.find(v)
    

def main():
    n=int(input())
    uf=UnionFind(n)
    for _ in range(n):
        s,t=map(int,input().split())
        if uf.is_same(s,t):
            print(s,t)
            return
        else:
            uf.union(s,t)


