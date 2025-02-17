# 递归算法三要素

1.**确定递归函数的参数和返回值：** 确定哪些参数是递归的过程中需要处理的，那么就在递归函数里加上这个参数， 并且还要明确每次递归的返回值是什么进而确定递归函数的返回类型

2.确定终止条件：写完了递归算法, 运行的时候，经常会遇到栈溢出的错误，就是没写终止条件或者终止条件写的不对，操作系统也是用一个栈的结构来保存每一层递归的信息，如果递归没有终止，操作系统的内存栈必然就会溢出。

3.**确定单层递归的逻辑：** 确定每一层递归需要处理的信息。在这里也就会重复调用自己来实现递归的过程

确定递归函数：dfs(node)

终止条件：if node is none:return

单层递归：中左右，左中右，左右中

![img](https://camo.githubusercontent.com/542d6395ba384d9175721ee9dc3322ad08aa6b7f39bea79bbdf6853f0549f9dd/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303230303830363139313130393839362e706e67)

## 递归的写法

```python
# 前序遍历-递归-LC144_二叉树的前序遍历
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        def dfs(node):
            if node is None:
                return
            
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res
    
```

```python
# 中序遍历-递归-LC94_二叉树的中序遍历
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        def dfs(node):
            if node is None:
                return
            
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res
```

```python
# 后序遍历-递归-LC145_二叉树的后序遍历
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        def dfs(node):
            if node is None:
                return
            
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)

        dfs(root)
        return res
```

# 迭代遍历的写法

**递归的实现就是：每一次递归调用都会把函数的局部变量、参数值和返回地址等压入调用栈中**，然后递归返回的时候，从栈顶弹出上一次递归的各项参数，所以这就是递归为什么可以返回上一层位置的原因。

## 前序遍历

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/e7bb83754cbe32f3c1d24bbe4c602f51.gif#pic_center)

```python
# 前序遍历-迭代-LC144_二叉树的前序遍历
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 根结点为空则返回空列表
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            # 中结点先处理
            result.append(node.val)
            # 右孩子先入栈
            if node.right:
                stack.append(node.right)
            # 左孩子后入栈
            if node.left:
                stack.append(node.left)
        return result
      
      
```



## 中序遍历

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/827562b8c485d136406f8f72e9c13d45.gif#pic_center)

```python
# 中序遍历-迭代-LC94_二叉树的中序遍历
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = []  # 不能提前将root结点加入stack中
        result = []
        cur = root
        while cur or stack:
            # 先迭代访问最底层的左子树结点
            if cur:     
                stack.append(cur)
                cur = cur.left		
            # 到达最左结点后处理栈顶结点    
            else:		
                cur = stack.pop()
                result.append(cur.val)
                # 取栈顶元素右结点
                cur = cur.right	
        return result
```



## 后序遍历

![前序到后序](https://camo.githubusercontent.com/de2fb6015ef4ff0cacb079f38ac9d326c3bb1803de416cb037db481d8352bd13/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303230303830383230303333383932342e706e67)

```python
# 后序遍历-迭代-LC145_二叉树的后序遍历
class Solution:
   def postorderTraversal(self, root: TreeNode) -> List[int]:
       if not root:
           return []
       stack = [root]
       result = []
       while stack:
           node = stack.pop()
           # 中结点先处理
           result.append(node.val)
           # 左孩子先入栈
           if node.left:
               stack.append(node.left)
           # 右孩子后入栈
           if node.right:
               stack.append(node.right)
       # 将最终的数组翻转
       return result[::-1]
```

## 层序遍历

![102二叉树的层序遍历](https://camo.githubusercontent.com/e1bb369928f38f317b162d9139d538569690174c59e962b48b853225c4444a7c/68747470733a2f2f636f64652d7468696e6b696e672e63646e2e626365626f732e636f6d2f676966732f3130322545342542412538432545352538462538392545362541302539312545372539412538342545352542312538322545352542412538462545392538312538442545352538452538362e676966)

```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque([root])
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):#很重要
                cur = queue.popleft()
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(level)
        return result
```

# 翻转二叉树

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0226.%E7%BF%BB%E8%BD%AC%E4%BA%8C%E5%8F%89%E6%A0%91.md

![226.翻转二叉树1](https://camo.githubusercontent.com/892fd31e60699cb343b2f7b5f37565b3dc993d242816972de5b5208b70ba936c/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303231303230333139323732343335312e706e67)

递归三部曲：

1.确定递归函数和参数：参数就是要传入节点的指针，不需要其他参数了，通常此时定下来主要参数，如果在写递归的逻辑中发现还需要其他参数的时候，随时补充。

```
TreeNode* invertTree(TreeNode* root)
```

2.确定终止条件

```
if (root == NULL) return root;
```

3.单层递归逻辑

```
swap(root->left, root->right);
invertTree(root->left);
invertTree(root->right);
```

```python
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
```

```python
#前序遍历的方法
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None      
        stack = [root]        
        while stack:
            node = stack.pop()   
            node.left, node.right = node.right, node.left                   
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)  
        return root
```

