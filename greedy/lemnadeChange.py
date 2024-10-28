#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   lemnadeChange.py
@Time    :   2024/10/28 20:34:30
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''

class Solution():
    def lemondeChange(self,bills):

        five=0
        tenn=10
        twenty=0
        for bill in bills:
            if bill==5:
                five+=1
            if bill==10:

                if five<=0:
                    return False
                five-=1
                ten+=1
            if bill==20:
                if five>0 and ten>0:
                    five-=1
                    ten-=1
                elif five>=3:
                    five-=3
                else:
                    return False
        return True