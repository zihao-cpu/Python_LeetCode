#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   dfs.py
@Time    :   2024/12/05 14:28:41
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution:


    def dfs(self,graph,start,n,path,result):
        if start==n:#此时找到了一条路径
            result.append(path)
            return
        for  i in range(1,n+1):
            if graph[start][i]==1:
                path.append(i)
                self.dfs(graph,i,n,path,result)
                path.pop()#回溯
    def main1(self):
        #定义一个图 矩阵方法
        n, m = map(int, input().split())
        graph= [[0]*(n+1) for _ in range(n+1)]
        for _ in range(m):
            s,t = map(int, input().split()) 
            graph[s][t] = 1
        result=[]
        return self.dfs(graph,1,n,[1],result)
    

    def dfs2(self,graph,start,n,path,result):
        if start==n:#此时找到了一条路径
            result.append(path)
            return
        for  i in graph[start]:
            
            path.append(i)
            self.dfs2(graph,i,n,path,result)
            path.pop()#回溯


    def main2(self):
        #定义一个图 邻接表方法
        from collections import defaultdict
        n, m = map(int, input().split())
        grapth = defaultdict(list)
        for _ in range(m):
            s,t=map(int,input().split())
            grapth[s].append(t)
            





if __name__ == '__main__':
    s = Solution()

    print(s.main1())
