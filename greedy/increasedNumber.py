#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   increasedNumber.py
@Time    :   2024/10/30 21:48:40
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def increasedNumber(self,num):
        num_str=list(str(num))

        for i in range(len(num_str)-1,0,-1):
            if int(num_str[i])>int(num_str[i-1]):
                num_str[i-1]=str(int(num_str[i-1])-1)
                for j in range(i,len(num_str)):
                    num_str[i-1]='9'

        return int(''.join(num_str))