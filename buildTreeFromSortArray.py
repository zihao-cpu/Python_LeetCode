#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   buildTreeFromSortArray.py
@Time    :   2024/10/17 19:47:05
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
    

    def bulidMaxTree(self,vals):
        if not vals:
            return None
        
        root_val=max(vals)
        root=TreeNode(root_val)
        separator_idx=vals.index(root_val)


        leftVals=vals[:separator_idx]
        rightVals=vals[separator_idx+1:]


        root.left=self.bulidMaxTree(leftVals)
        root.right=self.bulidMaxTree(rightVals)

        return root
    


    def buildTreeFromSortArray(self,vals):
        if not vals:
            return None
        
        mid =len(vals)//2

        root=TreeNode(vals[mid])

        root.left=self.buildTreeFromSortArray(vals[:mid])
        root.right=self.buildTreeFromSortArray(vals[mid+1:])

        return root
    

    