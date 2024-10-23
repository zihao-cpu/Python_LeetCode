#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Traversalnew.py
@Time    :   2024/10/09 09:39:50
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
from typing import List
class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        
        self.value=val
        self.left=left
        self.right=right
        return
class Solution:
    def preorder(self,root:TreeNode):
        if not root:
            return []
        
        stack=[root]
        result=[]
        while stack:
            node=stack.pop()                      #弹一个 放入两个（右左）子节点
            result.append(node.value)

            if node.right: 
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result


    def innerorder(self,root:TreeNode):
        if not root:
            return []
        
        stack=[]
        result=[]
        cur=root #引用一个指针
        while cur or stack:
            if cur:     #访问到最下面的左子树
                stack.append(cur)
                cur=cur.left
            else:
                cur=stack.pop()    #弹出一个 指针右移
                result.append(cur.value)
                cur=cur.right

        return result
    
    def posterorder(self,root:TreeNode):
        if not root:
            return []
        
        stack=[root]
        result=[]
        while stack:
            node=stack.pop()                      #弹一个 放入两个（右左）子节点
            result.append(node.value)
            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)
        return result[::-1]
    