#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   deleteNode.py
@Time    :   2024/10/16 21:40:31
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():

    def deleteOnNode(self,target):
        if target is None:
            return target
        
        if target.right is None:
            return target.left
        
        cur=target.right
        while cur.left:
            cur=cur.left
        cur.left=target.left
        return target.right
    def deleteNode(self,root,target):
        if not root:
            return None
        cur=root
        parent=None

        while cur:
            parent=cur      #记录父节点
            if target<cur.left.value:
                cur=cur.left
            else:
                cur=cur.right
        if parent is None:
            
            return self.deleteOnNode(cur)
        if parent.left and parent.left.value == target:
            parent.left = self.deleteOneNode(cur)
        if parent.right and parent.right.value == target:
           parent.right = self.deleteOneNode(cur)
        return root
    



    def deleteNode(self,root,target):
        #这些都是终止条件
        if root is None:
            return root
        if root.value==target:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                cur=root.right
                while cur.left is None:
                    cur=cur.left

                cur.left=root.left
                return root.right
        ###
            
        if root.value<target:
            root.left=self.deleteNode(root.left,target)
        else:
            root.right=self.deleteNode(root.right,target)



