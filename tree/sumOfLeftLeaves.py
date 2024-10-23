#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   sumOfLeftLeaves.py
@Time    :   2024/10/11 21:59:39
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def sumOfLeftLeaves(self,root):
        if not root:
            return 0
        if root.left is None and root.right is None:
            return 0
        

        left=self.sumOfLeftLeaves(root.left)
        if (root.left is not None) and (not root.left.left) and (not root.left.right):
            value=root.left.val

        right=self.sumOfLeftLeaves(root.right)
        return  value+left+right
    

    def sumOfLeftLeaves2(self,root):
        if not root:
            return 0
        if root.left is None and root.right is None:
            return 0
        stack=[root]
        result=0
        while stack:
            cur_node=stack.pop()
            if(cur_node.left is not None) and (not cur_node.left.left) and (not cur_node.left.right):
                result+=cur_node.left.val
            if cur_node.right:
                stack.append(cur_node.right)
            if cur_node.left:
                stack.append(cur_node.left)
        return result

