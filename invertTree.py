#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   invertTree.py
@Time    :   2024/10/10 16:02:40
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def inverseTree(self,root):
        if not root:
            return None
        root.left,root.right=root.right,root.left
        self.inverseTree(root.left)
        self.inverseTree(root.right)
        return root
    

    def inverseTree(self,root):
        if not root:
            return None
        stack=[root]
        while stack:
            node=stack.pop()                      #弹一个 放入两个（右左）子节点
            root.left,root.right=root.right,root.left
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return root