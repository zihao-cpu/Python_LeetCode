#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   permute2.py
@Time    :   2024/10/23 17:02:54
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution:
    def permute(self, nums):
        result = []
        nums.sort()
        self.backtracking(nums, [], [False] * len(nums), result)
        return result

    
    def backtracking(self,nums, path, used, result):
        if len(path) == len(nums):
            result.append(path[:])
            return
        

        for i in range(len(nums)):
            if (i>0 and nums[i]==nums[i-1] and not used[i-1]) or used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            self.backtracking(nums, path, used, result)
            path.pop()
            used[i] = False



    def permuteUnique(self, nums):
        nums.sort()  # 排序
        result = []
        self.backtracking2(nums, [False] * len(nums), [], result)
        return result
    
    def backtracking2(self, nums, used, path, result):
        if len(path) == len(nums):
            result.append(path[:])
            return
        used_set = set()
        for i in range(len(nums)):
            if nums[i] in used_set:
                continue
            if not used[i]:#等于0
                used_set.add(nums[i])
                used[i] = True
                path.append(nums[i])
                self.backtracking(nums, used, path, result)
                path.pop()
                used[i] = False

new =Solution()
result=new.permute([1,1,2])
