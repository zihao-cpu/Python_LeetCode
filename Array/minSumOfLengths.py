
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   minSumOfLengths.py
@Time    :   2025/04/29 14:51:38
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''

class Solution:
    def minSumOfLengths(self, arr, k):
        n = len(arr)  # 数组的长度
        # 创建一个前缀和数组 s，s[i] 表示 arr[0] 到 arr[i-1] 的和
        s = [0] * (n + 1)
        for i in range(n):
            s[i + 1] = s[i] + arr[i]
        
        # 初始化结果为正无穷大，表示暂时没有找到符合条件的解
        res = float('inf')
        
        # 用一个数组 min_len 来记录从位置 0 到当前位置的最小子数组长度 始终记录最小的
        min_len = [float('inf')] * (n + 1)
        
        # 用一个字典 cnt 来记录每个前缀和出现的位置
        cnt = {}
        
        for i in range(n + 1):
            # 计算当前前缀和减去目标值 k，得到一个值 x
            x = s[i] - k
            # 如果 x 存在于字典 cnt 中，说明我们找到了一个和为 k 的子数组
            if x in cnt:
                # 计算符合条件的子数组的长度
                len_subarray = i - cnt[x]
                # 更新结果：最小长度就是当前子数组的长度 + 前一个符合条件的子数组的最小长度
                # print(min_len)
                # print(len_subarray,cnt[x],min_len[cnt[x]])
                res = min(res, len_subarray + min_len[cnt[x]])
                # print(res)
            
            # 更新 min_len 数组，min_len[i] 表示从位置 0 到 i 的最小子数组长度
            if i > 0:
                # 如果之前已经找到过符合条件的子数组，更新 min_len[i]
                if 'len_subarray' in locals():
                    min_len[i] = min(min_len[i - 1], len_subarray)
                else:
                    min_len[i] = min_len[i - 1]
            
            # 将当前前缀和 s[i] 的值和其对应的索引存入字典 cnt
            cnt[s[i]] = i
        
        # 返回结果，如果没有找到符合条件的子数组，返回 -1
        return res if res != float('inf') else -1
if __name__ == '__main__':
    arr = [7,3,4,7]
    k = 7
    Solution().minSumOfLengths(arr, k)