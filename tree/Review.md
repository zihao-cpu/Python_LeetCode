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

层次遍历里面的queue就是每一层的节点和level一样

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

# 对称二叉树

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0101.%E5%AF%B9%E7%A7%B0%E4%BA%8C%E5%8F%89%E6%A0%91.md

![101. 对称二叉树1](https://camo.githubusercontent.com/af0be100cd04a571c2f4ab50c3ba23c77326ee2ed2a8073df2aeacf130ba0fd6/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303231303230333134343632343431342e706e67)

递归三部曲：

1.确定递归函数和参数：因为我们要比较的是根节点的两个子树是否是相互翻转的，进而判断这个树是不是对称树，所以要比较的是两个树，参数自然也是左子树节点和右子树节点。

```
bool compare(TreeNode* left, TreeNode* right)
```

2.确定终止条件：要比较两个节点数值相不相同，首先要把两个节点为空的情况弄清楚！否则后面比较数值的时候就会操作空指针了。

节点为空的情况有：（**注意我们比较的其实不是左孩子和右孩子，所以如下我称之为左节点右节点**）

- 左节点为空，右节点不为空，不对称，return false
- 左不为空，右为空，不对称 return false
- 左右都为空，对称，返回true

此时已经排除掉了节点为空的情况，那么剩下的就是左右节点不为空：

- 左右都不为空，比较节点数值，不相同就return false

此时左右节点不为空，且数值也不相同的情况我们也处理了。

```
if (left == NULL && right != NULL) return false;
else if (left != NULL && right == NULL) return false;
else if (left == NULL && right == NULL) return true;
else if (left->val != right->val) return false; // 注意这里我没有使用else
```

3.确定单层递归逻辑：

此时才进入单层递归的逻辑，单层递归的逻辑就是处理 左右节点都不为空，且数值相同的情况。

- 比较二叉树外侧是否对称：传入的是左节点的左孩子，右节点的右孩子。
- 比较内侧是否对称，传入左节点的右孩子，右节点的左孩子。
- 如果左右都对称就返回true ，有一侧不对称就返回false 。

```
bool outside = compare(left->left, right->right);   // 左子树：左、 右子树：右
bool inside = compare(left->right, right->left);    // 左子树：右、 右子树：左
bool isSame = outside && inside;                    // 左子树：中、 右子树：中（逻辑处理）
return isSame;
```

```python
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.compare(root.left, root.right)
        
    def compare(self, left, right):
        #首先排除空节点的情况
        if left == None and right != None: return False
        elif left != None and right == None: return False
        elif left == None and right == None: return True
        #排除了空节点，再排除数值不相同的情况
        elif left.val != right.val: return False
        
        #此时就是：左右节点都不为空，且数值相同的情况
        #此时才做递归，做下一层的判断
        outside = self.compare(left.left, right.right) #左子树：左、 右子树：右
        inside = self.compare(left.right, right.left) #左子树：右、 右子树：左
        isSame = outside and inside #左子树：中、 右子树：中 （逻辑处理）
        return isSame
```

迭代法：

![101.对称二叉树](https://camo.githubusercontent.com/d45272d4885e733b0b7a68e685bcccf036ddf54350b5b945054aaa8e1ee61d5f/68747470733a2f2f636f64652d7468696e6b696e672e63646e2e626365626f732e636f6d2f676966732f3130312e2545352541462542392545372541372542302545342542412538432545352538462538392545362541302539312e676966)





        1
       / \
      2   2
     / \ / \
    3  4 4  3
1. **初始状态**：
   - 队列：`[2, 2]`
2. **第一次循环**：
   - 取出 `2` 和 `2`，比较它们的值，相等。
   - 将它们的子节点加入队列：`[3, 3, 4, 4]`
3. **第二次循环**：
   - 取出 `3` 和 `3`，比较它们的值，相等。
   - 它们的子节点都为空，不加入队列。
   - 队列状态：`[4, 4]`
4. **第三次循环**：
   - 取出 `4` 和 `4`，比较它们的值，相等。
   - 它们的子节点都为空，不加入队列。
   - 队列状态：`[]`

```python
import collections
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = collections.deque()
        queue.append(root.left) #将左子树头结点加入队列
        queue.append(root.right) #将右子树头结点加入队列
        while queue: #接下来就要判断这这两个树是否相互翻转
            leftNode = queue.popleft()
            rightNode = queue.popleft()
            if not leftNode and not rightNode: #左节点为空、右节点为空，此时说明是对称的
                continue
            
            #左右一个节点不为空，或者都不为空但数值不相同，返回false
            if not leftNode or not rightNode or leftNode.val != rightNode.val:
                return False
            queue.append(leftNode.left) #加入左节点左孩子
            queue.append(rightNode.right) #加入右节点右孩子
            queue.append(leftNode.right) #加入左节点右孩子
            queue.append(rightNode.left) #加入右节点左孩子
        return True
```

```python
  #层序遍历 
  def isSymmetric(self,root):
        if not root:
            return True
        queue=collections.deque([root.left,root.right])
        while queue:
            if len(queue)%2!=0:
                return False
            level=[]
            for _ in range(len(queue)):
                cur=queue.popleft
                if cur:
                    level.append(cur.value)
                    queue.append(cur.left)
                    queue.append(cur.right)
                else:
                    level.append(None)
            if level!=level[::-1]:return False

        return True
```

# 二叉树的最大深度

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0104.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E5%A4%A7%E6%B7%B1%E5%BA%A6.md

采用后序遍历

递归三部曲

1.确定递归函数和参数：确定递归函数的参数和返回值：参数就是传入树的根节点，返回就返回这棵树的深度，所以返回值为int类型。

```
int getdepth(TreeNode* node)
```

2.确定终止条件：如果为空节点的话，就返回0，表示高度为0。

```
if (node == NULL) return 0;
```

3.确定单层递归的逻辑：先求它的左子树的深度，再求右子树的深度，最后取左右深度最大的数值 再+1 （加1是因为算上当前中间节点）就是目前节点为根节点的树的深度。

```
int leftdepth = getdepth(node->left);       // 左
int rightdepth = getdepth(node->right);     // 右
int depth = 1 + max(leftdepth, rightdepth); // 中
return depth;
```

```python
class Solution:
    def maxdepth(self, root: treenode) -> int:
        return self.getdepth(root)
        
    def getdepth(self, node):
        if not node:
            return 0
        leftheight = self.getdepth(node.left) #左
        rightheight = self.getdepth(node.right) #右
        height = 1 + max(leftheight, rightheight) #中
        return height
```

迭代层次遍历

```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        depth = 0
        queue = collections.deque([root])
        
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return depth
```

# 二叉树的最小深度

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0111.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E5%B0%8F%E6%B7%B1%E5%BA%A6.md

递归三部曲：

1.确定递归函数和参数：参数为要传入的二叉树根节点，返回的是int类型的深度。

```
int getDepth(TreeNode* node)
```

2.确定终止条件：

```
if (node == NULL) return 0;
```

3.确定单层递归逻辑

```
int leftDepth = getDepth(node->left);           // 左
int rightDepth = getDepth(node->right);         // 右
                                                // 中
// 当一个左子树为空，右不为空，这时并不是最低点
if (node->left == NULL && node->right != NULL) { 
    return 1 + rightDepth;
}   
// 当一个右子树为空，左不为空，这时并不是最低点
if (node->left != NULL && node->right == NULL) { 
    return 1 + leftDepth;
}
int result = 1 + min(leftDepth, rightDepth);
return result;
```

```python
class Solution:
    def getDepth(self, node):
        if node is None:
            return 0
        leftDepth = self.getDepth(node.left)  # 左
        rightDepth = self.getDepth(node.right)  # 右
        
        # 当一个左子树为空，右不为空，这时并不是最低点
        if node.left is None and node.right is not None:
            return 1 + rightDepth
        
        # 当一个右子树为空，左不为空，这时并不是最低点
        if node.left is not None and node.right is None:
            return 1 + leftDepth
        
        result = 1 + min(leftDepth, rightDepth)
        return result

    def minDepth(self, root):
        return self.getDepth(root)
```

迭代法

```python
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth = 0
        queue = collections.deque([root])
        
        while queue:
            depth += 1 
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if not node.left and not node.right:
                    return depth
            
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)

        return depth
```

