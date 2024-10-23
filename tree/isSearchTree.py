#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   isSearchTree.py
@Time    :   2024/10/15 15:54:07
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class Soolution():
    def __init__(self):
        self.maxVal = float('-inf')  # 因为后台测试数据中有int最小值
    def isSearchTree(self,root):
        if not root:
            return True
        
        # if root.val>root.left.val and root.right.val>root.val:
        #     return True
        left=self.isSearchTree(root.left)


        if self.maxVal<root.val:
            self.maxVal=root.val
        else:
            return False

        right=self.isSearchTree(root.right)

        
        return left and right
    

    #中序遍历
    def isSearchTree2(self,root):   
        if not root:
            return
        
        stack=[]
        
        cur=root #引用一个指针
        pre=None


        while cur or stack:
            if cur:     #访问到最下面的左子树
                stack.append(cur)
                cur=cur.left
            else:
                cur=stack.pop()    #弹出一个 指针右移
                if pre is not None and cur.val<pre.val:
                    return False

                pre=cur
                cur=cur.right

        return True
    


    def isSearchTree2(self,root):  

       #搜素二叉树是有序的
        def midorder(self,root):
            res=[]
            def dfs(node):
                if node is None:
                    return
                
                dfs(node.left)
                res.append(node.val)
                dfs(node.right)
            dfs(root)
            return res 
        
        res=midorder(root)


        if not root:
            return
        
        for i in range(1,len(res)):
            if res[i]<=res[i-1]:
                return False

        return True