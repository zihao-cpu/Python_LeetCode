#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   rob3.py
@Time    :   2024/11/10 22:18:30
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        self.memory={}
    def rob3(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.val
        
        #偷父节点的时候
        result1=root.val
        if root.left:
            result1+=self.rob3(root.left.left)+self.rob3(root.left.right)
        if root.right:
            result1+=self.rob3(root.right.left)+self.rob3(root.right.right)
        #不偷父节点的时候
        result2=self.rob3(root.left)+self.rob3(root.right)
        return max(result1,result2)
    
    def rob3_1(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.val
        if root in self.memory:
            return self.memory[root]    
        #偷父节点的时候
        result1=root.val
        if root.left:
            result1+=self.rob3_1(root.left.left)+self.rob3_1(root.left.right)
        if root.right:
            result1+=self.rob3_1(root.right.left)+self.rob3_1(root.right.right)
        #不偷父节点的时候
        result2=self.rob3_1(root.left)+self.rob3_1(root.right)
        self.memory[root]=max(result1,result2)
        return max(result1,result2)
    

    #
    def dfs(self, root):
        if not root:
            return [0,0]
        left = self.dfs(root.left)#【不偷，偷】
        right = self.dfs(root.right)
        #偷当前节点的时候 不能偷左右子节点
        rob_root = root.val + left[0] + right[0]
        #不偷父节点的时候
        not_rob_root = max(left) + max(right)
        return [rob_root, not_rob_root]
    def rob3_3(self, root: TreeNode) -> int:
        return max(self.dfs(root))
    
    


if __name__ == '__main__':
    root = TreeNode(3, TreeNode(2, TreeNode(3), TreeNode(3)), TreeNode(3, None, TreeNode(1)))
    print(Solution().rob3(root)) # Output: 7
    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(3)), TreeNode(5, None, TreeNode(1)))
    print(Solution().rob3(root)) # Output: 9
    
        