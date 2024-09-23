#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   swapPairs.py
@Time    :   2024/09/23 11:32:39
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next



class Solution():
    #递归法
    def swapPairs(self,head:ListNode)->ListNode:
        if head is None or head.next is None:
            return head
        pre=head
        cur=head.next
        cur.next=pre
        next=head.next.next
        pre.next=self.swapPairs(next)
        return cur
    #虚拟节点法
    def swapPairs(self,head:ListNode)->ListNode:
        dummy_head=ListNode(next=head)
        cur=dummy_head
        while cur.next and cur.next.next:
            temp=cur.next
            temp1=cur.next.next.next

            cur.next=cur.next.next
            cur.next.next=temp
            temp.next=temp1
            cur=cur.next.next #这里的位置要想清楚 为什么是cur.next.next,一个虚拟节点加两个三个真实节点，然后顺移动两位。    
        return dummy_head.next

        