#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   canConstruct.py
@Time    :   2024/09/25 14:24:21
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def canConstruct(sefl,ransom:str,magazine:str)->bool:
        heatmap=dict()
        for i in magazine:
            heatmap[i]=heatmap.get(i,0)+1
        for i in ransom:
            value=heatmap.get(i)
            if not value:
                return False
            else:
                heatmap[i]-=1
        return
