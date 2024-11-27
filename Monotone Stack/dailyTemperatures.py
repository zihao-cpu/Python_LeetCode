#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   dailyTemperatures.py
@Time    :   2024/11/27 15:05:53
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution:
    def dailyScores(self, temperatures):
        answer=[0]*len(temperatures)
        stack=[0]
        for i in range(1,len(temperatures)):
            if temperatures<=temperatures[stack[-1]]:
                stack.append(i)
            else:
                while len(stack)>0 and temperatures[stack[-1]]<temperatures[i]:
                    stack.pop()
                    answer[stack[-1]]=i-stack[-1]
                stack.append(i)
        return answer   