#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   theLeftValue.py
@Time    :   2024/10/11 22:23:05
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''


# def levelorder(self,root)->List[List[int]]:
#     if not root:
#         return []
#     queue=deque([root])
#     result=[]
#     while queue:
#         level=[]
#         for _ in range(len(queue)):
#             cur=queue.popleft()
#             level.append(cur)
#             if cur.left:
#                 queue.append(cur.left)
#             if cur.right:
#                 queue.append(cur.right)
#         result.append(level)
#     return result
from typing import List
from collections import deque
class Solution:
    def theLeftValue(self,root):
        if not root:
            return []
        queue=deque([root])
        
        while queue:
            level=[]
            for _ in range(len(queue)):
                cur=queue.popleft()
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return level[0]