#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   permute.py
@Time    :   2024/10/23 16:32:26
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''

class Solution:
    def permute(self, nums):
        result = []
        self.backtracking(nums, [], [False] * len(nums), result)
        return result

    def backtracking(self, nums, path, used, result):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            self.backtracking(nums, path, used, result)
            path.pop()
            used[i] = False

            



new =Solution()
result=new.permute([1,1,2])