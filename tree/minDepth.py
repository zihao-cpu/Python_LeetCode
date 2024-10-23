#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   minDepth.py
@Time    :   2024/10/11 17:06:00
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
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution():
    def minDepth(self,root):
        if not root:
            return 0
        queue=deque([root])
        depth=0
        while queue:
            depth+=1
            for _ in range(len(queue)):
                cur=queue.popleft()
                if not cur.left and cur.right:
                    return depth
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return depth
    
    #递归
    def minDepth(self,root):
        if not root:
            return 0
        left_min=self.minDepth(root.left)
        right_min=self.minDepth(root.right)
        if root.left is None and root.right is not None:
            return 1+right_min
        if root.left is not None and root.right is None:
            return 1+left_min

        return 1+min(left_min,right_min)
    

Node1=TreeNode(val=3)
Node2=TreeNode(val=9)
Node3=TreeNode(val=20)
Node4=TreeNode(val=15)
Node5=TreeNode(val=7)
Node1.left=Node2
Node1.right=Node3
Node3.left=Node4
Node3.right=Node5


