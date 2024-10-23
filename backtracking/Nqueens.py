#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Nqueens.py
@Time    :   2024/10/23 20:40:59
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def Nqueens(self,n):
        result=[]
        chessboard=['.'*n for _ in range(n)]

        self.backtracking(n, 0, chessboard, result)

        return [[''.join(row) for row in solution] for solution in result]


    def backtracking(self, n, row,chessboard,result):
        if row==n:
            result.append(chessboard[:])
            return
        for col in range(n):
            if self.is_valid(row,col,chessboard):
                chessboard[row]=chessboard[row][:col]+'Q'+chessboard[row][col+1:]

                self.backtracking(n,row+1,chessboard,result)
                #回溯
                chessboard[row]=chessboard[row][:col]+'.'+chessboard[row][col+1:]

    def is_valid(self,row,col,chessboard):
        for i in range(row):
            if chessboard[i][col]=='Q':
                return False
        

        i,j=row-1,col-1

        while i>=0 and j>=0:
            if chessboard[i][j]=='Q':
                return False
            i-=1
            j-=1

        i,j=row-1,col+1

        while i>=0 and j<len(chessboard):
            if chessboard[i][j]=='Q':
                return False
            i-=1
            j+=1

        return True
    
new= Solution()

new.Nqueens(4)