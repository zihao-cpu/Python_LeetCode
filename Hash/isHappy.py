#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   isHappy.py
@Time    :   2024/09/24 14:37:59
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def isHappy(self,num:int)->bool:
        record=set()
        while True:
            num=self.get_sum(num)
            if num==1:
                return True
            if num in record:
                return False
            else:
                record.add(num)
    def get_sum(self,num:int)->int:
        new_num=0
        while n:
            n,r=divmod(num,10)
            new_num=new_num+r**2
        return new_num
    

    def isHappy(self,num:int)->int:
        record=set()
        while num!=1:
            num=sum(int(i)**2 for i in str(num))
            if num in record:
                return False
            record.add(num)
        return True

