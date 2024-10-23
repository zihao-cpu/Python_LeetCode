#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   convertBST.py
@Time    :   2024/10/18 15:08:27
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Slution():
#右 中 左迭代的逻辑
    def __init__(self) -> None:
        self.pre=0
    def convetBST(self,root):
        if root is None:
            return
        self.convetBST(root.right)
        self.pre=root.value+self.pre
        root.value=self.pre
        self.convetBST(root.left)
        return root
    

    def convetBST(self,root):
        self.pre=0
        self.traversal(root)
        return root
    
    def traversal(self, cur):
        if cur is None:
            return        
        self.traversal(cur.right)
        cur.value += self.pre
        self.pre = cur.value
        self.traversal(cur.left)


    def convertBST(self, root):
        if not root: return root
        stack = []
        result = []
        cur = root
        pre = 0
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.right
            else: 
                cur = stack.pop()
                cur.val+= pre
                pre = cur.val
                cur =cur.left
        return root

