#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   rightSideView.py
@Time    :   2024/10/09 20:35:31
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
from typing import List
from collections import deque
class Solution():
    def rightSideView(self,root):
        if not root:
            return []
        queue=deque([root])
        result=[]
        while queue:
            levelSize=len(queue)
            for i in range(len(queue)):
                cur=queue.popleft()
                if i==levelSize-1: #遍历到该层的最后一个节点
                    result.append(cur.value) 
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return result