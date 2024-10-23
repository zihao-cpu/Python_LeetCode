#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   trimBST.py
@Time    :   2024/10/17 19:24:25
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Solution():
#迭代法很好理解 
    def trimBST(self,root,l,r):

        if root is None:
            return None
        

        #先处理父节点  使得父节点在[l,r]范围内
        while root and (root.left<l or root.right>r):
            if root.left.value<l:
                root=root.right
            else:
                root=root.left
        #处理左边 
        cur = root
        while cur:
            while cur.left and cur.left.value<l:      #此时是不用处理大于r 的部分 为啥？这是因为这是搜索二叉树  此时cur 的 左子树肯定是 ：~L~cur.value,这个范围内
                cur.left=cur.left.right

            cur=cur.left


        cur = root
        while cur:
            while cur.right and cur.right.value>r:
                cur.right=cur.right.left

            cur=cur.right
        
        return root