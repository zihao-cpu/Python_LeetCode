#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   connect.py
@Time    :   2024/10/09 21:10:36
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


from typing import List
from collections import deque
class Solution():
    def connect(self,root):
        if not root:
            return []
        queue=deque([root])
        result=[]
        while queue:
            level=[]
            prev_node=None
            for _ in range(len(queue)):
                cur=queue.popleft()
                if prev_node:     #如果该节点存在前一个节点，则将该节点变成前一个节点的next 否则自己变成别人的前一个节点
                    prev_node.next=cur
                prev_node=cur
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return root