#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   isSearchTree.py
@Time    :   2024/10/15 15:54:07
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Soolution():
    def __init__(self):
        self.maxVal = float('-inf')  # 因为后台测试数据中有int最小值
    def isSearchTree(self,root):
        if not root:
            return True
        
        # if root.val>root.left.val and root.right.val>root.val:
        #     return True
        left=self.isSearchTree(root.left)


        if self.maxVal<root.val:
            self.maxVal=root.val
        else:
            return False

        right=self.isSearchTree(root.right)

        
        return left and right