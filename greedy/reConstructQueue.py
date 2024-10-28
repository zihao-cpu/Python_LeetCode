#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   reConstructQueue.py
@Time    :   2024/10/28 20:57:47
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def reConstructQueue(self,people):
        people.sort(key=lambda x:[-x[0],x[1]])
        que=[]
        for i in people:
            que.insert(i[1],i)
        return que