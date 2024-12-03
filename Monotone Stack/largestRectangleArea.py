#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   largestRectangleArea.py
@Time    :   2024/12/03 19:18:09
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
def largestExtraRectangle(heights):
    size=len(heights)

    min_left_index=[0]*size
    min_right_index=[0]*size

    result=0
    #记录每一个柱子的左侧第一个矮一级的柱子的位置
    min_left_index[0]=-1
    for i in range(1,size):
        temp = i-1
        while temp >=0 and heights[temp]>=heights[i]:
            temp=min_left_index[temp]
        min_left_index[i]=temp
    #记录每一个柱子的右侧第一个矮一级的柱子的位置
    min_right_index[size-1]=size
    for i in range(size-2,-1,-1):
        temp=i+1
        while temp<size and heights[temp]>=heights[i]:
            temp=min_right_index[temp]
        min_right_index[i]=temp
    #计算面积
    for i in range(size):
        result=max(result,heights[i]*(min_right_index[i]-min_left_index[i]-1))
        return result
    