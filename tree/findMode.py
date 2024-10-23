#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   findMode.py
@Time    :   2024/10/15 17:30:04
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''

class Solution():
    def searchTree(self,root,freq_map)->dict:
        if not root:
            return
        freq_map[root.val]+=1
        self.searchTree(root.left,freq_map)
        self.searchTree(root.right,freq_map)
        return freq_map

    def findMode(self,root):
        result=[]
        if not root:
            return result

        map_={}
        map_result=self.searchTree(root,map_)


        maxValue=max(map_result.values())
        
        for key,freq in map_result.items():
            if freq==maxValue:
                result.append(key)

        return result





