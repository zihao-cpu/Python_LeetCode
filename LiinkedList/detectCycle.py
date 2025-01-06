#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   detectCycle.py
@Time    :   2024/09/23 21:32:36
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
'''
1.快 慢指针的方法

fast 每次移动两步
慢指针 每次移动一步 
相遇的时候 fast走过的步数等于slow步数的两倍


2.集合的方法
不断去遍历 节点 把遍历的节点加入到集合中，然后 去判断当前节点是否是在集合中

'''
class Solution():
    def detectCycle(self,head:ListNode)->ListNode:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow ==fast:
                slow = head
                while slow != fast:
                    slow=slow.next
                    fast=fast.next
                return slow
        return None
    def detectCycle(self,head:ListNode)->ListNode:
        visited=set()
        while head:
            if head in visited:
                return head
            visited.add(head)
            head=head.next
        return None
