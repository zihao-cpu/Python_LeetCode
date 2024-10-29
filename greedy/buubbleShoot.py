#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   buubbleShoot.py
@Time    :   2024/10/28 21:41:36
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def bubbleShoot(self,bubbles):
        bubbles.sort(key=lambda x:[x[0],x[1]])
        max_right=bubbles[0][1]
        result=1
        for i in range(1,len(bubbles)):
            if bubbles[i][0]>=bubbles[i-1][1]:
                result+=1
            else:
                bubbles[i][1]=min(bubbles[i][1],bubbles[i-1][1])
        return result
    
new=Solution()
new.bubbleShoot( [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]])

