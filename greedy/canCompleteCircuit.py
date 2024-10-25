#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   canCompleteCircuit.py
@Time    :   2024/10/25 20:19:19
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def canCompleteCircuit(self,gas,cost):
        cumCost=0
        total=0
        start=0
        for i in range(len(gas)):
            cumCost+=gas[i]-cost[i]
            total+=gas[i]-cost[i]
            if cumCost<0:
                start+=1
                cumCost=0

        if total<0:return -1
        return start