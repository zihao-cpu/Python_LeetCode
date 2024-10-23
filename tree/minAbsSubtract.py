#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   minAbsSubtract.py
@Time    :   2024/10/15 16:32:16
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def __init__(self):
        self.result = float('inf')
        self.pre = None
    def minAbsSubtract(self,root):
        
        
        stack=[]
        
        cur=root #引用一个指针
        pre=None
        result=float('inf')
        while cur or stack:
            if cur:     #访问到最下面的左子树
                stack.append(cur)
                cur=cur.left
            else:
                cur=stack.pop()    #弹出一个 指针右移
                if pre is not None:
                    result=min(result,cur.val-pre.val)

                pre=cur
                cur=cur.right
        
        return
    


    def dfs(self,node):

        if node is None:
            return
        
        self.dfs(node.left)
        if self.pre is not None:
            self.result=min(self.result,node.val-self.pre.val)
        self.pre=node
        self.dfs(node.right)
        return self.result

    def minAbsSubtract2(self,root):
        return self.dfs(root)