#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   searchInsert.PY
@Time    :   2025/01/13 21:29:05
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
def searchInsert(nums, target):
    left=0
    right=len(nums)-1 #定义target在左闭右闭的区间里，[left, right]
    while left<=right: #注意这里是<= 为什么是这样呢？当left==right，区间[left, right]依然有效
        # 因为left和right的定义是闭区间，所以当left==right时，区间[left, right]依然有效
        middle=left+(right-left)//2   
        
        if nums[middle]==target:
            return middle
        if nums[middle]>target:
            right=middle-1
        else:
            left=middle+1


        # 分别处理如下四种情况
        # 目标值在数组所有元素之前  [0, -1]  right会等于-1
        # 目标值等于数组中某一个元素  return middle;
        # 目标值插入数组中的位置 [left, right]，return  right + 1
        # 目标值在数组所有元素之后的情况 [left, right]， 因为是右闭区间，所以 return right + 1
    return right+1 #是因为闭区间