#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   solveSudoku.py
@Time    :   2024/10/23 21:38:23
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
    def solveSudoku(self,board):

        self.backtrackinng(board)
        
        return
    
    
    def backtrackinng(self,board):
        
        for row in range(9):
            for col in range(9):
                if board[row][col]!='.':
                    continue
                for k in range(9):
                    if self.is_valid(row,col,k,board):
                        board[row][col]=str(k)
                        if self.backtrackinng(board):return True
                        board[row][col]='.'
                # 若数字1-9都不能成功填入空格，返回False无解
                return False
        return True
    

    def is_valid(row,col,k,board):
        for i in range(9):
            if board[i][col]==str(k):
                return False
            
        for i in range(9):
            if board[row][i]==str(k):
                return False
            

        start_row=(row//3)*3
        start_col=(col//3)*3
        for i in range(start_row,start_row+3):
            for j in range(start_col,start_col+3):
                if board[i][j]==str(k):
                    return False
        
        return True