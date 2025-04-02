#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   numOfSubarrays.py
@Time    :   2025/04/02 10:23:15
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
# 给你一个整数数组 arr 和两个整数 k 和 threshold 。请你返回长度为 k 且平均值大于等于 threshold 的子数组数目。
class Solution:
    def numOfSubarrays(self, arr, k: int, threshold: int) -> int:
        n = len(arr)
        left = 0
        right = k - 1
        count = 0
        while right < n:
            if sum(arr[left:right+1]) / k >= threshold:
                count += 1
            left += 1
            right += 1
        return count
    

    def numOfSubarrays2(self, arr, k: int, threshold: int) -> int:
        sum=0
        ans=0
        target=k*threshold
        for i in range(len(arr)):
            sum+=arr[i]
            if i>=k-1:
                if sum>=target:
                    ans+=1
                sum-=arr[i-k+1]
        return ans
    
# 思路：
# 1. 遍历数组，每次滑动窗口大小为 k ，计算窗口内元素的和，如果和大于等于 k*threshold ，则计数器加 1 。
# 2. 优化：
#    由于窗口大小为 k ，因此可以将窗口内元素的和保存到变量 sum 中，每次滑动窗口时，只需要更新 sum 即可。
#    由于窗口大小为 k ，因此可以将窗口左边界 left 保存到变量中，每次滑动窗口时，只需要更新 left 即可。
#    由于窗口大小为 k ，因此可以将窗口右边界 right 保存到变量中，每次滑动窗口时，只需要更新 right 即可。
if __name__ == '__main__':
    arr = [2, 2, 2, 2, 5, 5, 5, 8]
    k = 3
    threshold = 4
    print(Solution().numOfSubarrays(arr, k, threshold)) # 3
    print(Solution().numOfSubarrays2(arr, k, threshold)) # 3    
