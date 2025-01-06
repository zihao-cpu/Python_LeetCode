#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   removeElements.py
@Time    :   2024/09/19 13:57:34
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''

class ListNode:
    def __init__(self,val=0,next=None) -> None:
        self.val=val
        self.next=next


#加入虚拟节点
class Solution():
    def removeElements(self,val,head):
        dummy_node=ListNode(next=head)
        current=dummy_node
        while current.next:
            if current.next.val==val:
                current=current.next.next
            else:
                current=current.next
        return dummy_node.next