#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   averageOfLevels.py
@Time    :   2024/10/09 20:41:03
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
from collections import deque
class Sulution():
    def averageOfLevels(self,root):
        if not root:
            return []
        queue=deque([root])
        result=[]
        while queue:
            level_sum=0
            level_size=len(queue)
            for _ in range(len(queue)):
                cur=queue.popleft()
                level_sum+=cur.value

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(level_sum/level_size)
        return result