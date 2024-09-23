#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   getIntersectionNode.py
@Time    :   2024/09/23 19:41:19
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

'''
采用双指针的方法，但是不是快慢指针
'''
class Solution():
    def getIntersectionNode(self,headA:ListNode,headB:ListNode)->ListNode:
        #获取长度
        curA=headA
        curB=headB
        lenA=lenB=0
        while curA:
            lenA +=1
            curA=curA.next
        while curB:
            lenB+=1
            curB=curB.next

        curA=headA
        curB=headB
        if lenA<lenB:    #A本来是短的现在变长
            temp=curA
            curA=curB
            curB=temp

            temp=lenA
            lenA=lenB
            lenB=temp
        for _ in range(lenA-lenB):
            curA=curA.next    #在这里对齐
        while curB:
            if curA==curB:
                return curA
            else:
                curA=curA.next
                curB=curB.next
        return None