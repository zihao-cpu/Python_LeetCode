#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   rotate.py
@Time    :   2025/01/18 17:26:04
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution:
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[-k:] + nums[:-k]
        return nums
    
    def reverse(self, nums, start, end) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    def rotate2(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        self.reverse(nums, 0, n-1) #先整体翻转
        self.reverse(nums, 0, k-1)#再翻转前k个元素
        self.reverse(nums, k, n-1)#再翻转后n-k个元素

if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    k = 3
    Solution().rotate(nums, k)  
