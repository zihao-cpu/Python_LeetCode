#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   combineIP.py
@Time    :   2024/10/21 21:03:57
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''

# class Solution():
#     def combineIP(self,s):
#         result=[]

#         self.backtracking(s,0,3,[],result)
#         return result
        
#     def is_valid(self,s):
#         if len(s)==2 and s[0]=='0':
#             return False
#         if len(s)==3 and (int(s)>255 or s[0]=='0'):
#             return False
#         return True

#     def backtracking(self,s,startIndex,endIndex,path,result):
#         if len(path)==4 and endIndex==len(s)-1:
#             result.append('.'.join(path))
#             return
#         for i in range(startIndex,endIndex):
#             if self.is_valid(s[startIndex:i+startIndex+1]):
#                 path.append(s[startIndex:i+startIndex+1])
#                 self.backtracking(s,i+1,i+3,path,result)
#                 path.pop()
class Solution():
    def combineIP(self,s):
        result=[]
        self.backtracking(s,0,0,'',result)
        return result


    def backtracking(self,s,startIndex,pointNum,current,result):
        if pointNum==3:
            if self.is_valid(s,startIndex,len(s)-1):
                current+=s[startIndex:]
                result.append(current)
                return

        for i in range(startIndex,len(s)):
            if self.is_valid(s,startIndex,i):
                sub=s[startIndex:i+1]
                self.backtracking(s,i+1,pointNum+1,current+sub+'.',result)
            else:
                break

    def is_valid(self,s,start,end):
        if  start>end:
            return False
        if s[start]=='0' and  start!=end:
            return False   
        nums=0
        for i in range(start,end+1):
            if  not s[i].isdigit():
                return False
            nums=nums*10+int(s[i])
            if nums>255:
                return False
        return True




new=Solution()

result=new.combineIP("25525511135")


