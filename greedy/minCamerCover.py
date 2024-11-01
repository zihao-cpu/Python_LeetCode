#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   minCamerCover.py
@Time    :   2024/11/01 15:13:54
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def minCameraCover(self, root ) -> int:
        result=[0]

        if  self.dfs(root,result)==0:
            result[0]+=1
            return result[0]
        def dfs(node,result):
            if not node:
                return 2
            left=dfs(node.left,result)
            right=dfs(node.right,result)
            if left==0 or right==0:
                result[0]+=1
                return 1
            if left==1 or right==1:
                return 2
            if left==2 or right==2:
                return 0
            