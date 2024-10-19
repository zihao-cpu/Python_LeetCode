#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   combineLetters.py
@Time    :   2024/10/19 12:28:43
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''



class Solution():


    def __init__(self):
        self.lettersMap=[
            "",     # 0
            "",     # 1
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs", # 7
            "tuv",  # 8
            "wxyz"  # 9
        ]

        self.s=''
        self.result=[]


    def backtrackinng(self,digits,index):
        if index==len(digits):
            self.result.append(self.s)
            return

        letters=self.lettersMap[index]
        for i in range(len(letters)):
            self.s+=letters[1]
            self.backtrackinng(digits,index+1)
            self.s=self.s[:-1]

    def combineLetters(self,digits):
        if len(digits):
            return self.result
        self.backtrackinng(digits,0)

        return
    