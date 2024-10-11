#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   binaryTreePaths.py
@Time    :   2024/10/11 20:10:30
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

def traversal( cur, path, result):
    path.append(cur.val)  # 中
    if not cur.left and not cur.right:  # 到达叶子节点
        sPath = '->'.join(map(str, path))
        result.append(sPath)
        return
    if cur.left:  # 左
        traversal(cur.left, path, result)
        path.pop()  # 回溯
    if cur.right:  # 右
        traversal(cur.right, path, result)
        path.pop()  # 回溯
def binaryTreePaths( root):
    result = []
    path = []
    if not root:
        return result
    traversal(root, path, result)


def binaryTreePaths2( root):  #前序遍历
    node_stack,path_stack,result=[root],[str(root.val)],[]
    while node_stack:
        cur_node=node_stack.pop()
        cur_path=path_stack.pop()
        if (cur_node.left is None) and (cur_node.right is None):#not （cur_node.left or cur_node.leftcur_node.right）
            result.append(cur_path)
        if cur_node.right:
            node_stack.append(cur_node.right)
            path_stack.append(cur_path+'->'+str(cur_node.right.val))
        if cur_node.left:
            node_stack.append(cur_node.left)
            path_stack.append(cur_path+'->'+str(cur_node.left.val))
    return result  
binaryTreePaths(Node1)




class Solution:
    def traversal(self, cur, path, result):
        path.append(cur.val)  # 中  #借栈
        if not cur.left and not cur.right:  # 到达叶子节点
            sPath = '->'.join(map(str, path))
            result.append(sPath)
            return
        if cur.left:  # 左
            self.traversal(cur.left, path, result)
            path.pop()  # 回溯
        if cur.right:  # 右
            self.traversal(cur.right, path, result)
            path.pop()  # 回溯

    def binaryTreePaths(self, root):
        result = []
        path = []
        if not root:
            return result
        self.traversal(root, path, result)
        return result
    

    def binaryTreePaths2(self, root):
        node_stack,path_stack,result=[root],[str(root.value)],[]
        while node_stack:
            cur_node=node_stack.pop()
            cur_path=path_stack.pop()
            if (cur_node.left is None) and (cur_node.right is None):#not （cur_node.left or cur_node.leftcur_node.right）
                result.append(cur_path)
            if cur_node.right:
                node_stack.append(cur_node.right)
                path_stack.append(cur_path+'->'+str(cur_node.right.value))
            if cur_node.left:
                node_stack.append(cur_node.left)
                path_stack.append(cur_path+'->'+str(cur_node.left.value))
        return result           
        
        
        
        
        
        return