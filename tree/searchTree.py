#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   searchTree.py
@Time    :   2024/10/12 21:55:26
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def searchTree(self,root,val):
        if not root or root.val==val:
            return root
        
        if root.val>val:
            return self.searchTree(root.left,val)
        if root.val<val:
            return self.searchTree(root.right,val)
        


    
    def searchTree(self,root,val):
        while root:
            if val<root.val:
                root=root.left
            elif val>root.val:
                root=root.right
            else:
                return root
        return None
        


        