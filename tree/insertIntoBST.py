#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   insertIntoBST.py
@Time    :   2024/10/16 10:57:06
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''


class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        
        self.value=val
        self.left=left
        self.right=right



class Solution():

    def __init__(self) -> None:
        self.parent=None
    def insertIntoBST(self,root,val):
        
        if root is None:
            return TreeNode(val)
        

        cur=root
        parent=root

        while cur:
            parent=cur
            if val<cur.left.value:
                cur=cur.left
            else:
                cur=cur.right
        if val<parent.value:
            parent.left=TreeNode(val)
        else:
            parent.right=TreeNode(val)
        return root
    
    def traversal(self, cur, val):
        if cur is None:
            node = TreeNode(val)
            if val > self.parent.value:
                self.parent.right = node
            else:
                self.parent.left = node
            return

        self.parent = cur   #保存父节点
        if cur.value > val:
            self.traversal(cur.left, val)
        if cur.value < val:
            self.traversal(cur.right, val)

        #整个函数不需要返回值

    def insertIntoBST2(self,root,val):
        self.parent = TreeNode(0)
        if root is None:
            return TreeNode(val)
        self.traversal(root, val) 
        return root  #在这里返回 
    


    
    def insertIntoBST3(self,root,val):
        if root is None:
            return TreeNode(val)
        
        if val>root.value:
            root.right=self.insertIntoBST(root.right,val)
        if val<root.value:
            root.left=self.insertIntoBST(root.left,val)


        return root  #在这里返回 root 在这里就是父节点的概念
    

    