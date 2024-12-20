#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   字符串接龙.py
@Time    :   2024/12/20 21:21:29
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
def judge(s1,s2):
    count =0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            count+=1
    return count==1


def main():
    n=int(input())
    beginstr,endstr=map(str,input().split())
    if beginstr==endstr:
        print(0)
        exit()
    strlist=[]
    for i in range(n):
        strlist.append(input())
    visited=[False]*n
    queue=[[beginstr,1]]
    while queue:
        str,step=queue.pop(0)
        if judge(str,endstr):
            print(step)
            exit()
        for i in range(n):
            if visited[i]==False and judge(strlist[i],str):
                visited[i]=True
                queue.append([strlist[i],step+1])
