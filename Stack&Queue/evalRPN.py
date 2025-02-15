#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   evalRPN.py
@Time    :   2024/09/29 18:26:32
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
from typing import List
from operator import add, sub, mul
def div(x,y):
    return int(x / y) if x * y > 0 else -(abs(x) // abs(y))
class Solution():
    op_map={'+':add,'-':sub,'*':mul,'/':div}
    def evalRPN(self,tokens:List[str]):
        
        stack=[]
        for i in tokens:
            if i not in {'+', '-', '*', '/'}:
                stack.append(int(i))
            else:
                op2=stack.pop()
                op1=stack.pop()
                stack.append(self.op_map[i](op1,op2))
        return stack.pop()
