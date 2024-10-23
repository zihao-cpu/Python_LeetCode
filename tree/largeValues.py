#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   largeValues.py
@Time    :   2024/10/09 20:49:40
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
from collections import deque
class Solution():
    def largeValues(self,root):
        if not root:
            return []
        queue=deque([root])
        result=[]
        while queue:
            level=[]
            max_value=float('-inf')
            for _ in range(len(queue)):
                cur=queue.popleft()
                max_value=max(max_value,cur.value)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(max_value)
        return result       