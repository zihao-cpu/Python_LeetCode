#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   minStep.py
@Time    :   2025/04/03 14:40:40
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution:
    def minSteps(s: str, t: str) -> int:
        n = len(s)
        mp = [0] * 128  # 创建一个长度为 128 的列表，用于存储字符的频次
        for i in range(n):
            mp[ord(s[i])] += 1  # 增加 s 中字符的频次
            mp[ord(t[i])] -= 1  # 减少 t 中字符的频次
        
        cnt = 0
        for num in mp:
            cnt += abs(num)  # 计算字符的绝对差值
        return cnt // 2  # 因为每个字符被计算了两次，除以 2 即为最小步骤数


    def minSteps2(s: str, t: str) -> int:
        # 创建一个字典来记录字符的频次
        mp = {}
        
        # 遍历字符串 s 和 t，分别增加和减少字符的频次
        for i in range(len(s)):
            mp[s[i]] = mp.get(s[i], 0) + 1  # 增加 s 中字符的频次
            mp[t[i]] = mp.get(t[i], 0) - 1  # 减少 t 中字符的频次
        
        # 计算不匹配的字符的数量
        cnt = 0
        for num in mp.values():
            cnt += abs(num)  # 计算字符频次差的绝对值
        return cnt // 2  # 除以 2 得到最小步骤数

if __name__ == '__main__':
    s = "leetcode"
    t = "practice"
    print(Solution.minSteps(s, t))
    print(Solution.minSteps2(s, t))