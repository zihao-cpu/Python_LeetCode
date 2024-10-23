#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   lowestCommonAncestor.py
@Time    :   2024/10/15 18:44:31
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def lowestCommonAncestor(self,root,q,p):
        if root == q or root==p or root is None:
        
            return root
        
        left =self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)

        if left is not None and right is not None:
            return root
        

        if left is not None and right is None:
            return left
        

        if left is None and right is not None:
            return right
        
        else:
            
            return None



