#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   isSymmetric.py
@Time    :   2024/10/11 14:36:19
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''

class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        
        self.value=val
        self.left=left
        self.right=right
import collections
class Solution():
    #递归
    def compare(self,left,right):
        if left ==None and right !=None:return False
        elif left!=None and right==None:return False
        elif left == None and right==None:return True
        elif left.value!=right.value:return False
        outside=self.compare(left.left,right.right)
        inside=self.compare(left.right,right.left)
        isSame=outside&inside
        return isSame

    def isSymmetric(self,root):
        if not None:
            return True
        
        return self.compare(root.left,root.right)
    
    
    #迭代
    def isSymmetric(self,root):
        if not None:
            return True
        
        queue=collections.deque()
        queue.append(root.left)
        queue.append(root.right)
        while queue:
            left=queue.popleft()
            right=queue.popleft()
            if not left and not right:     
                continue

            if not left or not right or left.value !=right.value:
                return False
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        return True



    #层次遍历
# from typing import List
# from collections import deque
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
    

    def isSymmetric(self,root):
        if not root:
            return True
        queue=collections.deque([root.left,root.right])
        while queue:
            if len(queue)%2!=0:
                return False
            level=[]
            for _ in range(len(queue)):
                cur=queue.popleft
                if cur:
                    level.append(cur.value)
                    queue.append(cur.left)
                    queue.append(cur.right)
                else:
                    level.append(None)
            if level!=level[::-1]:return False

        return True
    





