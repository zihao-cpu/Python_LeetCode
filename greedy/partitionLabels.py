#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   partitionLabels.py
@Time    :   2024/10/29 17:36:44
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def partitionLabels(self,s):
        last_occurrennce={}   #统计每个字符最后出现的位置
        for i,ch in enumerate(s):
            last_occurrennce[ch]=i
        result=[]
        end,start=0,0
        for i,ch in enumerate(s):
            end=max(last_occurrennce[ch],end)#获取目前为止最远字符位置
            if i==end:
                result.append(end-start+1)
                start=i+1
        return result

