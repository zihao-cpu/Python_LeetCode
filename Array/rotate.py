#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   rotate.py
@Time    :   2025/01/12 19:54:25
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k %= n
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
        end -= 1
    #先反转整个数组
    reverse(0, n-1)

    #再反转前k个元素
    reverse(0, k-1)

    #再反转后n-k个元素
    reverse(k, n-1)


#空间复杂度O(n)
def roteate_2(nums, k):
    n = len(nums)
    copy=nums.copy()
    for i in range(n):
        nums[(i+k)%n]=copy[i]
    return nums
