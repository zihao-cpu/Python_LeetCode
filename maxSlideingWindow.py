#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   maxSlideingWindow.py
@Time    :   2024/09/29 21:11:26
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
from collections import deque
class MyQueen():
    def __init__(self):
        self.queue=deque()
    def pop(self,value):
        if value==self.queue[0]:
            self.queue.popleft()
    def push(self,value):#不断去比较加入的数字和队列的左侧
        while value>self.queue[-1] and self.queue:
            self.queue.pop()
        self.queue.append(value)
    def front(self):
        return self.queue[0]
    
class Solution():
    def maxSlidingWindow(self,nums,k):
        que=MyQueen()
        result=[]
        for i in range(k):
            que.push(nums[i])
            result.append(que.front())

        for i in range(k,len(nums)):
            que.pop(nums[i-k])
            que.push(nums[i])
            result.append(que.front())
        return result

