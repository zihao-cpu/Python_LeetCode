#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   mergeTrees.py
@Time    :   2024/10/12 21:11:29
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
from collections import deque
class Solution():
    def mergeTree(self,root1,root2):
        if not root1:
            return root2
        if not root2:
            return root1
        
        root1.val=root1.val+root2.val

        root1.left=self.mergeTree(root1.left,root2.left)

        root1.right=self.mergeTree(root1.right,root2.right)

        return root1
    



    def mergeTree(self,root1,root2):
        if not root1:
            return root2
        if not root2:
            return root1
        
        queue=deque()
        queue=deque([root1])
        queue=deque([root2])

        while queue:
            node1=queue.popleft()
            node2=queue.popleft()

            if node1.left and node2.left:
                queue.append(node1.left)
                queue.append(node2.lfet)


            if node1.right and node2.right:
                queue.append(node1.right)
                queue.append(node2.right)

            node1.val+=node2.val


            if not node1.left and node2.left:
                node1.left=node2.left

            if not node1.right and node2.right:
                node1.right=node2.right           
        return root1