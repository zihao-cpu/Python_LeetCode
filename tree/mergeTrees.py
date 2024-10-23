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

    # 确定递归函数的参数和返回值
    def mergeTree(self,root1,root2):

        #终止条件 因为是传入了两个树，那么就有两个树遍历的节点t1 和 t2，如果t1 == NULL 了，两个树合并就应该是 t2 了（如果t2也为NULL也无所谓，合并之后就是NULL）。
        if not root1:
            return root2
        if not root2:
            return root1
        

        # 确定单层递归的逻辑
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