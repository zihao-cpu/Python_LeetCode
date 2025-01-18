#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   reorderList.py
@Time    :   2025/01/18 20:58:34
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
import collections
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        d=collections.deque()
        tmp=head
        while tmp.next:
            d.append(tmp.next)
            tmp=tmp.next
        tmp=head
        while d:
            tmp.next=d.pop()
            tmp=tmp.next
            if len(d):
                tmp.next=d.popleft()
                tmp=tmp.next
        tmp.next=None
    def reorderList2(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        slow=fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        right=slow.next#右边链表   
        slow.next=None#断开右边链表 

        right=self.reverseList(right)

        left=head#左边链表
        while right:
            curleft=left.next
            left.next=right
            left=curleft
            curright=right.next
            right.next=curleft
            right=curright

            

    def reverseList(self, head: ListNode) -> ListNode:
            if not head or not head.next:
                return head
            pre=None
            cur=head
            while cur:
                nxt=cur.next
                cur.next=pre
                pre=cur
                cur=nxt
            return pre


