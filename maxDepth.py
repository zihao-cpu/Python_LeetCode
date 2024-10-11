#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   maxDepth.py
@Time    :   2024/10/11 16:49:26
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''

from typing import List
from collections import deque
# class Solution():
#     def levelorder(self,root)->List[List[int]]:
#         if not root:
#             return []
#         queue=deque([root])
#         result=[]
#         while queue:
#             level=[]
#             for _ in range(len(queue)):
#                 cur=queue.popleft()
#                 level.append(cur)
#                 if cur.left:
#                     queue.append(cur.left)
#                 if cur.right:
#                     queue.append(cur.right)
#             result.append(level)
#         return result

class Solution():
    def maxDepth(self,root):
        if not root:
            return 0
        queue=deque([root])
        depth=0
        while queue:
            depth+=1
            for _ in range(len(queue)):
                cur=queue.popleft()
              
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return depth
    

    def maxDepth(self,root):
        if not root:
            return 0
        left_max=self.maxDepth(root.left)
        right_max=self.maxDepth(root.right)
        return 1+max(left_max,right_max)

