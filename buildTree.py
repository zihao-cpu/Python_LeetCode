#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   buildTree.py
@Time    :   2024/10/12 20:25:23
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
    def bulidTree(self,inorder,postporder):
        if not postporder:
            return None
        root_val =postporder[-1]
        root=TreeNode(root_val)


        separator_idx=inorder.index(root_val) #找到分割点

        inorder_left=inorder[:separator_idx]
        inorder_right=inorder[separator_idx+1:]

        postporder_left=postporder[:len(inorder_left)]
        postporder_right=postporder[len(inorder_left):len(postporder)-1]

        root.left=self.bulidTree(inorder_left,postporder)
        root.right=self.bulidTree(inorder_right,postporder_right)
        return root