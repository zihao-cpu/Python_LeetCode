#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   removeFromEnd.py
@Time    :   2024/09/23 19:13:25
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class Solution():

    #采用双指针的方法 快指针 先移动 n+1 ；快、慢指针一起移动 直到快指针为none
    def removeFromEnd(self,head:ListNode,n:int)->ListNode:
        dummy_head=ListNode(0,head)
        slow=fast=dummy_head
        for i in range(n+1):
            fast=fast.next
        while fast:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        
        return dummy_head.next