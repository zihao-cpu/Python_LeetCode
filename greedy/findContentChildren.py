#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   findContentChildren.py
@Time    :   2024/10/24 15:53:48
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def findContentChildern(self,s,g):
        s.sort()
        g.sort()
        index =0 
        for i in range(len(s)):
            if index<len(g) and s[i]>=g[index]:
                index+=1
        return index

        