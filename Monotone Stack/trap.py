#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   trap.py
@Time    :   2024/12/01 19:27:06
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution:
    def trap(self, height) -> int:
        leftheight = [0] * len(height)
        rightheight = [0] * len(height)
        leftheight[0]=height[0]
        for i in range(1,len(height)):
            leftheight[i]=max(leftheight[i-1],height[i])
        rightheight[-1]=height[-1]
        for i in range(len(height)-2,-1,-1):
            rightheight[i]=max(rightheight[i+1],height[i])
        ans=0
        for i in range(len(height)):
            ans+=min(leftheight[i],rightheight[i])-height[i]
        return ans