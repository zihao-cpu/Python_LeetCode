#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   hasPathSum.py
@Time    :   2024/10/11 22:39:31
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
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
    return result


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




def hasSumpath(root,sum):
    if not root:
        return False   
    node_stack,path_stack=[root],[root.val]
    while node_stack:
        cur_node=node_stack.pop()
        cur_sum=path_stack.pop()
        if (cur_node.left is None) and (cur_node.right is None) and cur_sum==sum:#not （cur_node.left or cur_node.leftcur_node.right）
            return True
        if cur_node.right:
            node_stack.append(cur_node.right)
            path_stack.append(cur_sum+cur_node.right.val)
        if cur_node.left:
            node_stack.append(cur_node.left)
            path_stack.append(cur_sum+cur_node.left.val)
    return False


def traversal( cur, path, result,value):
    path.append(cur.val)  # 中
    if not cur.left and not cur.right and value==0:  # 到达叶子节点
        sPath = '->'.join(map(str, path))
        result.append(sPath)
        return True
    if cur.left:  # 左
        traversal(cur.left, path,result,value-cur.left.val)
        path.pop()  # 回溯
    if cur.right:  # 右
        traversal(cur.right, path,result,value-cur.right.val)
        path.pop()  # 回溯
    return False
def hasSumpath2(root,sum):
    result = []
    path = []
    if not root:
        return False
    traversal(root,path,result,sum-root.val)
    return result
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

Node1=TreeNode(val=5)
Node2=TreeNode(val=4)
Node3=TreeNode(val=8)
Node4=TreeNode(val=11)
Node5=TreeNode(val=13)
Node6=TreeNode(val=4)
Node7=TreeNode(val=7)
Node8=TreeNode(val=2)
Node9=TreeNode(val=5)
Node10=TreeNode(val=1)

Node1.left=Node2
Node1.right=Node3

Node2.left=Node4

Node3.left=Node5
Node3.right=Node6

Node4.left=Node7
Node4.right=Node8

Node6.left=Node9
Node6.right=Node10