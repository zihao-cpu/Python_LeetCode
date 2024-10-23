#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   isBalanced.py
@Time    :   2024/10/11 18:29:56
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


Node1=TreeNode(val=3)
Node2=TreeNode(val=9)
Node3=TreeNode(val=20)
Node4=TreeNode(val=15)
Node5=TreeNode(val=7)
Node1.left=Node2
Node1.right=Node3
Node3.left=Node4
Node3.right=Node5


Node6=TreeNode(val=1)
Node7=TreeNode(val=2)
Node8=TreeNode(val=2)
Node9=TreeNode(val=3)
Node10=TreeNode(val=3)
Node11=TreeNode(val=4)
Node12=TreeNode(val=4)
Node6.left=Node7
Node6.right=Node8
Node7.left=Node9
Node7.right=Node10
Node9.left=Node11
Node9.right=Node12


class Solution():
    
    def maxDepth(self,root):
        from collections import deque
        if not root:
            return 0
        queue=deque([root])
        depth=0
        while queue:
            depth+=1
            for _ in range(len(queue)):
                cur=queue.popleft()
              
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return depth
    
    def isBalanced(self,root):
        
        if not root:
            return True
        st=[root]  
        while st:

            node=st.pop()
            if abs(self.maxDepth(node.left)-self.maxDepth(node.right))>1:
                return False
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)

        return True

    def getHigh(self,root):
        if not root:
            return 0
        if(left_high:=self.getHigh(root.left))==-1:
            return -1
        if(righ_high:=self.getHigh(root.right))==-1:
            return -1
        if abs(left_high-righ_high)>1:
            return -1
        
        return 1+max(left_high,righ_high)
    
    def isBalanced2(self,root):
        if self.getHigh(root)!=-1:
            return True
        else:
            return False



    


    

