#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   reverseList.py
@Time    :   2024/09/19 13:57:46
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class ListNode():
    def __init__(self,val,next) -> None:
        self.val=val
        self.next=next
class Solution():
    #双指针法
    def reverseList(self,head:ListNode)->ListNode:
        pre=None
        cur=head
        while cur:
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp
        return pre
    #递归法
    def reverseList(self,head:ListNode)->ListNode:
        return self.reverse(head,None)
    def reverse(self,cur:ListNode,pre:ListNode)->ListNode:
        if cur==None:#终止条件
            return pre    
        temp=cur.next
        cur.next=pre
        return self.reverse(temp,cur)
