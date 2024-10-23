#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Traversal.py
@Time    :   2024/09/30 14:43:08
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''


class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        
        self.value=val
        self.left=left
        self.right=right
        return
class Solution():
    def preorder(self,root:TreeNode):
        res=[]
        def dfs(node):
            if node is None:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res
    def midorder(self,root:TreeNode):
        res=[]
        def dfs(node):
            if node is None:
                return
            
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res
    def postorder(self,root:TreeNode):
        res=[]
        def dfs(node):
            if node is None:
                return
            
            dfs(node.left)
            
            dfs(node.right)
            res.append(node.val)
        dfs(root)
        return res