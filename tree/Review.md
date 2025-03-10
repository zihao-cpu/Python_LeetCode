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

# 翻转二叉树(前序遍历)

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

# 对称二叉树(层序遍历)

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

![101.对称二叉树](https://camo.githubusercontent.com/d45272d4885e733b0b7a68e685bcccf036ddf54350b5b945054aaa8e1ee61d5f/68747470733a2f2f636f64652d7468696e6b696e672e63646e2e626365626f732e636f6d2f676966732f3130312e2545352541462542392545372541372542302545342542412538432545352538462538392545362541302539312e676966



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

# 二叉树的最大深度(后序遍历)

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

# 二叉树的最小深度(后序遍历)

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

# 平衡二叉树(后序遍历)

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0110.%E5%B9%B3%E8%A1%A1%E4%BA%8C%E5%8F%89%E6%A0%91.md

一棵高度平衡二叉树定义为：一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1

- 二叉树节点的深度：指从根节点到该节点的最长简单路径边的条数。
- 二叉树节点的高度：指从该节点到叶子节点的最长简单路径边的条数

**此时大家应该明白了既然要求比较高度，必然是要后序遍历。**

递归三部曲：

1.确定递归函数和参数：参数：当前传入节点。 返回值：以当前传入节点为根节点的树的高度。

那么如何标记左右子树是否差值大于1呢？

如果当前传入节点为根节点的二叉树已经不是二叉平衡树了，还返回高度的话就没有意义了。

所以如果已经不是二叉平衡树了，可以返回-1 来标记已经不符合平衡树的规则了。

```
// -1 表示已经不是平衡二叉树了，否则返回值是以该节点为根节点树的高度
int getHeight(TreeNode* node)
```

2.确定终止条件：

```
if (node == NULL) {
    return 0;
}
```

3.确定单层递归逻辑

```
int leftHeight = getHeight(node->left); // 左
if (leftHeight == -1) return -1;
int rightHeight = getHeight(node->right); // 右
if (rightHeight == -1) return -1;

int result;
if (abs(leftHeight - rightHeight) > 1) {  // 中
    result = -1;
} else {
    result = 1 + max(leftHeight, rightHeight); // 以当前节点为根节点的树的最大高度
}

return result;
```

```python
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if self.get_height(root) != -1:
            return True
        else:
            return False

    def get_height(self, root: TreeNode) -> int:
        # Base Case
        if not root:
            return 0
        # 左
        if (left_height := self.get_height(root.left)) == -1:
            return -1
        # 右
        if (right_height := self.get_height(root.right)) == -1:
            return -1
        # 中
        if abs(left_height - right_height) > 1:
            return -1
        else:
            return 1 + max(left_height, right_height)
```

# 二叉树的所有路径(前序遍历)

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0257.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%89%80%E6%9C%89%E8%B7%AF%E5%BE%84.md

递归三部曲：

1.确定递归函数和参数：

要传入根节点，记录每一条路径的path，和存放结果集的result，这里递归不需要返回值，代码如下：

```
void traversal(TreeNode* cur, vector<int>& path, vector<string>& result)
```

2.确定终止条件：

```
if (cur->left == NULL && cur->right == NULL) {
    终止处理逻辑
}
确定终止条件并完成拼接
if (cur->left == NULL && cur->right == NULL) { // 遇到叶子节点
    string sPath;
    for (int i = 0; i < path.size() - 1; i++) { // 将path里记录的路径转为string格式
        sPath += to_string(path[i]);
        sPath += "->";
    }
    sPath += to_string(path[path.size() - 1]); // 记录最后一个节点（叶子节点）
    result.push_back(sPath); // 收集一个路径
    return;
}

```

3.确定单层递归逻辑

**回溯和递归是一一对应的，有一个递归，就要有一个回溯**，**所以回溯要和递归永远在一起**

```
if (cur->left) {
    traversal(cur->left, path, result);
    path.pop_back(); // 回溯
}
if (cur->right) {
    traversal(cur->right, path, result);
    path.pop_back(); // 回溯
}
```

```python
# Definition for a binary tree node.
class Solution:
    def traversal(self, cur, path, result):
        path.append(cur.val)  # 中
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
```

迭代法

```
        cur = stack.pop()
        path = path_st.pop()
        关键在于一起弹出来
```
```python
class Solution:

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        # 题目中节点数至少为1
        stack, path_st, result = [root], [str(root.val)], []

        while stack:
            cur = stack.pop()
            path = path_st.pop()
            # 如果当前节点为叶子节点，添加路径到结果中
            if not (cur.left or cur.right):
                result.append(path)
            if cur.right:
                stack.append(cur.right)
                path_st.append(path + '->' + str(cur.right.val))
            if cur.left:
                stack.append(cur.left)
                path_st.append(path + '->' + str(cur.left.val))

        return result
```

# 相同的树

```python
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.compare(p, q)
        
    def compare(self, tree1, tree2):
        if not tree1 and tree2:
            return False
        elif tree1 and not tree2:
            return False
        elif not tree1 and not tree2:
            return True
        elif tree1.val != tree2.val: #注意这里我没有使用else
            return False
        
        #此时就是：左右节点都不为空，且数值相同的情况
        #此时才做递归，做下一层的判断
        compareLeft = self.compare(tree1.left, tree2.left) #左子树：左、 右子树：左
        compareRight = self.compare(tree1.right, tree2.right) #左子树：右、 右子树：右
        isSame = compareLeft and compareRight #左子树：中、 右子树：中（逻辑处理）
        return isSame
```

# 左叶子之和(前序遍历)

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0404.%E5%B7%A6%E5%8F%B6%E5%AD%90%E4%B9%8B%E5%92%8C.md

因为题目中其实没有说清楚左叶子究竟是什么节点，那么我来给出左叶子的明确定义：**节点A的左孩子不为空，且左孩子的左右孩子都为空（说明是叶子节点），那么A节点的左孩子为左叶子节点**

递归三部曲：

1.确定递归函数和参数：

判断一个树的左叶子节点之和，那么一定要传入树的根节点，递归函数的返回值为数值之和，所以为int

```
int sumOfLeftLeaves(TreeNode* root)
```

2.确定终止条件

```
        if (root == NULL) return 0;
        if (root->left == NULL && root->right== NULL) return 0;
```

3.确定单层递归逻辑

当遇到左叶子节点的时候，记录数值，然后通过递归求取左子树左叶子之和，和 右子树左叶子之和，相加便是整个树的左叶子之和。

```
        if (root->left != NULL && root->left->left == NULL && root->left->right == NULL) {
            curleftValue = root->left->val;
        }
        curleftValue + sumOfLeftLeaves(root->left) + sumOfLeftLeaves(root->right)
```

```python
class Solution:
    def sumOfLeftLeaves(self, root):
        if root is None:
            return 0
        leftValue = 0
        if root.left is not None and root.left.left is None and root.left.right is None:
            leftValue = root.left.val
        return leftValue + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

```

迭代法：

弹出的时候判断



```python
class Solution:
    def sumOfLeftLeaves(self, root):
        if root is None:
            return 0
        st = [root]
        result = 0
        while st:
            node = st.pop()
            if node.left and node.left.left is None and node.left.right is None:
                result += node.left.val
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
        return result
```

# 找树左下角的值(层次遍历)

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0513.%E6%89%BE%E6%A0%91%E5%B7%A6%E4%B8%8B%E8%A7%92%E7%9A%84%E5%80%BC.md

层次遍历最简单

**找到最后一行的第一个数**

```python
from collections import deque
class Solution:
    def findBottomLeftValue(self, root):
        if root is None:
            return 0
        queue = deque()
        queue.append(root)
        result = 0
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i == 0:
                    result = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
```

# 路径总和(前序遍历)

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0112.%E8%B7%AF%E5%BE%84%E6%80%BB%E5%92%8C.md

递归三部曲：

1.确定递归函数和参数：参数：需要二叉树的根节点，还需要一个计数器，这个计数器用来计算二叉树的一条边之和是否正好是目标和，计数器为int型。

- **如果要搜索其中一条符合条件的路径，那么递归一定需要返回值，因为遇到符合条件的路径了就要及时返回。（本题的情况）**

  ​

2.确定终止条件：

首先计数器如何统计这一条路径的和呢？

不要去累加然后判断是否等于目标和，那么代码比较麻烦，可以用递减，让计数器count初始为目标和，然后每次减去遍历路径节点上的数值。

如果最后count == 0，同时到了叶子节点的话，说明找到了目标和。

如果遍历到了叶子节点，count不为0，就是没找到。

递归终止条件代码如下：

```
if (!cur->left && !cur->right && count == 0) return true; // 遇到叶子节点，并且计数为0
if (!cur->left && !cur->right) return false; // 遇到叶子节点而没有找到合适的边，直接返回
```

3.确定单层递归逻辑：

因为终止条件是判断叶子节点，所以递归的过程中就不要让空节点进入递归了。

递归函数是有返回值的，如果递归函数返回true，说明找到了合适的路径，应该立刻返回。

```
if (cur->left) { // 左 （空节点不遍历）
    // 遇到叶子节点返回true，则直接返回true
    if (traversal(cur->left, count - cur->left->val)) return true; // 注意这里有回溯的逻辑
}
if (cur->right) { // 右 （空节点不遍历）
    // 遇到叶子节点返回true，则直接返回true
    if (traversal(cur->right, count - cur->right->val)) return true; // 注意这里有回溯的逻辑
}
return false;
```

```
if (cur->left) { // 左
    count -= cur->left->val; // 递归，处理节点;
    if (traversal(cur->left, count)) return true;
    count += cur->left->val; // 回溯，撤销处理结果
}
if (cur->right) { // 右
    count -= cur->right->val;
    if (traversal(cur->right, count)) return true;
    count += cur->right->val;
}
return false;
```

```python
class Solution:
    def traversal(self, cur: TreeNode, count: int) -> bool:
        if not cur.left and not cur.right and count == 0: # 遇到叶子节点，并且计数为0
            return True
        if not cur.left and not cur.right: # 遇到叶子节点直接返回
            return False
        
        if cur.left: # 左
            count -= cur.left.val
            if self.traversal(cur.left, count): # 递归，处理节点
                return True
            count += cur.left.val # 回溯，撤销处理结果
            
        if cur.right: # 右
            count -= cur.right.val
            if self.traversal(cur.right, count): # 递归，处理节点
                return True
            count += cur.right.val # 回溯，撤销处理结果
            
        return False
    
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        return self.traversal(root, sum - root.val)      
```

迭代法，思想和二叉树的所有路径一样

```python
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        # 此时栈里要放的是pair<节点指针，路径数值>
        st = [(root, root.val)]
        while st:
            node, path_sum = st.pop()
            # 如果该节点是叶子节点了，同时该节点的路径数值等于sum，那么就返回true
            if not node.left and not node.right and path_sum == sum:
                return True
            # 右节点，压进去一个节点的时候，将该节点的路径数值也记录下来
            if node.right:
                st.append((node.right, path_sum + node.right.val))
            # 左节点，压进去一个节点的时候，将该节点的路径数值也记录下来
            if node.left:
                st.append((node.left, path_sum + node.left.val))
        return False
```

# 从中序与后序遍历序列构造二叉树

![106.从中序与后序遍历序列构造二叉树](https://camo.githubusercontent.com/0b007e4086174a2587b02c3ea8eaa8dba0534ab8e639a2907e13047917cd9db5/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303231303230333135343234393836302e706e67)

来看一下一共分几步：

- 第一步：如果数组大小为零的话，说明是空节点了。
- 第二步：如果不为空，那么取后序数组最后一个元素作为节点元素。
- 第三步：找到后序数组最后一个元素在中序数组的位置，作为切割点
- 第四步：切割中序数组，切成中序左数组和中序右数组 （顺序别搞反了，一定是先切中序数组）
- 第五步：切割后序数组，切成后序左数组和后序右数组
- 第六步：递归处理左区间和右区间

```
TreeNode* traversal (vector<int>& inorder, vector<int>& postorder) {

    // 第一步
    if (postorder.size() == 0) return NULL;

    // 第二步：后序遍历数组最后一个元素，就是当前的中间节点
    int rootValue = postorder[postorder.size() - 1];
    TreeNode* root = new TreeNode(rootValue);

    // 叶子节点
    if (postorder.size() == 1) return root;

    // 第三步：找切割点
    int delimiterIndex;
    for (delimiterIndex = 0; delimiterIndex < inorder.size(); delimiterIndex++) {
        if (inorder[delimiterIndex] == rootValue) break;
    }

    // 第四步：切割中序数组，得到 中序左数组和中序右数组
    // 第五步：切割后序数组，得到 后序左数组和后序右数组

    // 第六步
    root->left = traversal(中序左数组, 后序左数组);
    root->right = traversal(中序右数组, 后序右数组);

    return root;
}
```

```python
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # 第一步: 特殊情况讨论: 树为空. (递归终止条件)
        if not postorder:
            return None

        # 第二步: 后序遍历的最后一个就是当前的中间节点.
        root_val = postorder[-1]
        root = TreeNode(root_val)

        # 第三步: 找切割点.
        separator_idx = inorder.index(root_val)

        # 第四步: 切割inorder数组. 得到inorder数组的左,右半边.
        inorder_left = inorder[:separator_idx]
        inorder_right = inorder[separator_idx + 1:]

        # 第五步: 切割postorder数组. 得到postorder数组的左,右半边.
        # ⭐️ 重点1: 中序数组大小一定跟后序数组大小是相同的.
        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left): len(postorder) - 1]

        # 第六步: 递归
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)
         # 第七步: 返回答案
        return root
```

# 最大二叉树

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0654.%E6%9C%80%E5%A4%A7%E4%BA%8C%E5%8F%89%E6%A0%91.md

递归三部曲

1.确定递归函数和参数：参数传入的是存放元素的数组，返回该数组构造的二叉树的头结点，返回类型是指向节点的指针。

```
TreeNode* constructMaximumBinaryTree(vector<int>& nums)
```

2.确定终止条件

判断nums是否为空

3.确定单层递归逻辑

1.先要找到数组中最大的值和对应的下标， 最大的值构造根节点，下标用来下一步分割数组。

```
int maxValue = 0;
int maxValueIndex = 0;
for (int i = 0; i < nums.size(); i++) {
    if (nums[i] > maxValue) {
        maxValue = nums[i];
        maxValueIndex = i;
    }
}
TreeNode* node = new TreeNode(0);
node->val = maxValue;
```

2.最大值所在的下标左区间 构造左子树

这里要判断maxValueIndex > 0，因为要保证左区间至少有一个数值。

```
if (maxValueIndex > 0) {
    vector<int> newVec(nums.begin(), nums.begin() + maxValueIndex);
    node->left = constructMaximumBinaryTree(newVec);
}
```

3.最大值所在的下标右区间 构造右子树

判断maxValueIndex < (nums.size() - 1)，确保右区间至少有一个数值。

```
if (maxValueIndex < (nums.size() - 1)) {
    vector<int> newVec(nums.begin() + maxValueIndex + 1, nums.end());
    node->right = constructMaximumBinaryTree(newVec);
}
```

```python
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        max_val = max(nums)
        max_index = nums.index(max_val)
        node = TreeNode(max_val)
        node.left = self.constructMaximumBinaryTree(nums[:max_index])
        node.right = self.constructMaximumBinaryTree(nums[max_index+1:])
        return node
```

# 合并二叉树(前序遍历+层次遍历)

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0617.%E5%90%88%E5%B9%B6%E4%BA%8C%E5%8F%89%E6%A0%91.md

递归三部曲

1.确定递归函数和参数：首先要合入两个二叉树，那么参数至少是要传入两个二叉树的根节点，返回值就是合并之后二叉树的根节点。

```
TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
```

2.确定终止条件：因为是传入了两个树，那么就有两个树遍历的节点t1 和 t2，如果t1 == NULL 了，两个树合并就应该是 t2 了（如果t2也为NULL也无所谓，合并之后就是NULL）。

反过来如果t2 == NULL，那么两个数合并就是t1（如果t1也为NULL也无所谓，合并之后就是NULL）。

```
if (t1 == NULL) return t2; // 如果t1为空，合并之后就应该是t2
if (t2 == NULL) return t1; // 如果t2为空，合并之后就应该是t1
```

3.单层递归逻辑

单层递归的逻辑就比较好写了，这里我们重复利用一下t1这个树，t1就是合并之后树的根节点（就是修改了原来树的结构）。

那么单层递归中，就要把两棵树的元素加到一起。

```
t1->val += t2->val;
t1->left = mergeTrees(t1->left, t2->left);
t1->right = mergeTrees(t1->right, t2->right);
return t1;
```

```python
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        # 递归终止条件: 
        #  但凡有一个节点为空, 就立刻返回另外一个. 如果另外一个也为None就直接返回None. 
        if not root1: 
            return root2
        if not root2: 
            return root1
        # 上面的递归终止条件保证了代码执行到这里root1, root2都非空. 
        root1.val += root2.val # 中
        root1.left = self.mergeTrees(root1.left, root2.left) #左
        root1.right = self.mergeTrees(root1.right, root2.right) # 右
        
        return root1
```

迭代法

和对称二叉树解题类似

```python
from collections import deque

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1

        queue = deque()
        queue.append((root1, root2))

        while queue:
            node1, node2 = queue.popleft()
            node1.val += node2.val

            if node1.left and node2.left:
                queue.append((node1.left, node2.left))
            elif not node1.left:
                node1.left = node2.left

            if node1.right and node2.right:
                queue.append((node1.right, node2.right))
            elif not node1.right:
                node1.right = node2.right

        return root1
```

# 二叉搜索树

二叉搜索树是一个有序树：

- 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
- 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
- 它的左、右子树也分别为二叉搜索树

# 二叉搜索树中的搜索

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0700.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E6%90%9C%E7%B4%A2.md

![700.二叉搜索树中的搜索](https://camo.githubusercontent.com/cf55fdf9637675b74a15c3d3372691529f3abc26048901ea5f1e01701100783d/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303231303230343135353532323437362e706e67)

递归三部曲

1.确定递归函数和参数：递归函数的参数传入的就是根节点和要搜索的数值，返回的就是以这个搜索数值所在的节点。

```
TreeNode* searchBST(TreeNode* root, int val)
```

2.确定终止条件：如果root为空，或者找到这个数值了，就返回root节点。

```
if (root == NULL || root->val == val) return root;
```

3.确定单层递归逻辑

看看二叉搜索树的单层递归逻辑有何不同。

因为二叉搜索树的节点是有序的，所以可以有方向的去搜索。

如果root->val > val，搜索左子树，如果root->val < val，就搜索右子树，最后如果都没有搜索到，就返回NULL。

```
TreeNode* result = NULL;
if (root->val > val) result = searchBST(root->left, val);
if (root->val < val) result = searchBST(root->right, val);
return result;
```

```python
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # 为什么要有返回值: 
        #   因为搜索到目标节点就要立即return，
        #   这样才是找到节点就返回（搜索某一条边），如果不加return，就是遍历整棵树了。

        if not root or root.val == val: 
            return root

        if root.val > val: 
            return self.searchBST(root.left, val)

        if root.val < val: 
            return self.searchBST(root.right, val)
```

迭代法：

```python
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            if val < root.val: root = root.left
            elif val > root.val: root = root.right
            else: return root
        return None
```

```python
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        stack = [root]
        while stack:
            node = stack.pop()
            # 根据TreeNode的定义
            # node携带有三类信息 node.left/node.right/node.val
            # 找到val直接返回node 即是找到了该节点为根的子树
            # 此处node.left/node.right/val的前后顺序可打乱
            if node.val == val: 
                return node
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return None
```

# 验证二叉搜索树(中序遍历)

要知道中序遍历下，输出的二叉搜索树节点的数值是有序序列。

有了这个特性，**验证二叉搜索树，就相当于变成了判断一个序列是不是递增的了。**

```python
class Solution:
    def __init__(self):
        self.vec = []

    def traversal(self, root):
        if root is None:
            return
        self.traversal(root.left)
        self.vec.append(root.val)  # 将二叉搜索树转换为有序数组
        self.traversal(root.right)

    def isValidBST(self, root):
        self.vec = []  # 清空数组
        self.traversal(root)
        for i in range(1, len(self.vec)):
            # 注意要小于等于，搜索树里不能有相同元素
            if self.vec[i] <= self.vec[i - 1]:
                return False
        return True
```

迭代法：

```python
class Solution:
    def isValidBST(self, root):
        stack = []
        cur = root
        pre = None  # 记录前一个节点
        while cur is not None or len(stack) > 0:
            if cur is not None:
                stack.append(cur)
                cur = cur.left  # 左
            else:
                cur = stack.pop()  # 中
                if pre is not None and cur.val <= pre.val:
                    return False
                pre = cur  # 保存前一个访问的结点
                cur = cur.right  # 右
        return True
```

# 二叉搜索树的最小绝对差

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0530.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E6%9C%80%E5%B0%8F%E7%BB%9D%E5%AF%B9%E5%B7%AE.md

题目中要求在二叉搜索树上任意两节点的差的绝对值的最小值。

**注意是二叉搜索树**，二叉搜索树可是有序的。

遇到在二叉搜索树上求什么最值啊，差值之类的，就把它想成在一个有序数组上求最值，求差值，这样就简单多了。

```python
class Solution:
    def __init__(self):
        self.vec = []

    def traversal(self, root):
        if root is None:
            return
        self.traversal(root.left)
        self.vec.append(root.val)  # 将二叉搜索树转换为有序数组
        self.traversal(root.right)

    def getMinimumDifference(self, root):
        self.vec = []
        self.traversal(root)
        if len(self.vec) < 2:
            return 0
        result = float('inf')
        for i in range(1, len(self.vec)):
            # 统计有序数组的最小差值
            result = min(result, self.vec[i] - self.vec[i - 1])
        return result
```

迭代法 + 记录前一个节点的指针

```python
class Solution:
    def __init__(self):
        self.result = float('inf')
        self.pre = None

    def traversal(self, cur):
        if cur is None:
            return
        self.traversal(cur.left)  # 左
        if self.pre is not None:  # 中
            self.result = min(self.result, cur.val - self.pre.val)
        self.pre = cur  # 记录前一个
        self.traversal(cur.right)  # 右

    def getMinimumDifference(self, root):
        self.traversal(root)
        return self.result
```

# 二叉搜索树中的众数

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0501.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E4%BC%97%E6%95%B0.md

递归法来遍历树，用map来记录

```python
from collections import defaultdict

class Solution:
    def searchBST(self, cur, freq_map):
        if cur is None:
            return
        freq_map[cur.val] += 1  # 统计元素频率
        self.searchBST(cur.left, freq_map)
        self.searchBST(cur.right, freq_map)

    def findMode(self, root):
        freq_map = defaultdict(int)  # key:元素，value:出现频率
        result = []
        if root is None:
            return result
        self.searchBST(root, freq_map)
        max_freq = max(freq_map.values())
        for key, freq in freq_map.items():
            if freq == max_freq:
                result.append(key)
        return result
```

# 二叉树的最近公共祖先(后序遍历)

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0236.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88.md

情况一：**如果找到一个节点，发现左子树出现结点p，右子树出现节点q，或者 左子树出现结点q，右子树出现节点p，那么该节点就是节点p和q的最近公共祖先。**

判断逻辑是 如果递归遍历遇到q，就将q返回，遇到p 就将p返回，那么如果 左右子树的返回值都不为空，说明此时的中节点，一定是q 和p 的最近祖先。

情况二：**就是节点本身p(q)，它拥有一个子孙节点q(p)。**

1.确定递归函数以及参数

```
TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q)
```

2.确定终止条件

遇到空的话，因为树都是空了，所以返回空。

那么我们来说一说，如果 root == q，或者 root == p，说明找到 q p ，则将其返回，这个返回值，后面在中节点的处理过程中会用到，那么中节点的处理逻辑，下面讲解。

```
if (root == q || root == p || root == NULL) return root;
```

3.确定单层递归逻辑

```
left = 递归函数(root->left);  // 左
right = 递归函数(root->right); // 右
left与right的逻辑处理;         // 中
如果left 和 right都不为空，说明此时root就是最近公共节点。这个比较好理解

如果left为空，right不为空，就返回right，说明目标节点是通过right返回的，反之依然。

```

```python

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root == q or root == p or root is None:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None and right is not None:
            return root

        if left is None and right is not None:
            return right
        elif left is not None and right is None:
            return left
        else: 
            return None
```

![236.二叉树的最近公共祖先2](https://camo.githubusercontent.com/8aaf71724e838ca2fd761f10b83ec4bffe8bc48054868a012d3378fd1d34fccb/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f3230323130323034313531323538322e706e67)

# 二叉搜索树的最近公共祖先

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0235.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88.md



```python
class Solution:
    def traversal(self, cur, p, q):
        if cur is None:
            return cur
                                                        # 中
        if cur.val > p.val and cur.val > q.val:           # 左
            left = self.traversal(cur.left, p, q)
            if left is not None:
                return left

        if cur.val < p.val and cur.val < q.val:           # 右
            right = self.traversal(cur.right, p, q)
            if right is not None:
                return right

        return cur

    def lowestCommonAncestor(self, root, p, q):
        return self.traversal(root, p, q)
```

迭代法：

```python
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
```

# 二叉树中的插入操作

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0701.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E6%8F%92%E5%85%A5%E6%93%8D%E4%BD%9C.md



```python
class Solution:
    def insertIntoBST(self, root, val):
        if root is None:
            node = TreeNode(val)
            return node

        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)

        return root
```





```python
class Solution:
    def insertIntoBST(self, root, val):
        if root is None:  # 如果根节点为空，创建新节点作为根节点并返回
            node = TreeNode(val)
            return node

        cur = root
        parent = root  # 记录上一个节点，用于连接新节点
        while cur is not None:
            parent = cur
            if cur.val > val:
                cur = cur.left
            else:
                cur = cur.right

        node = TreeNode(val)
        if val < parent.val:
            parent.left = node  # 将新节点连接到父节点的左子树
        else:
            parent.right = node  # 将新节点连接到父节点的右子树

        return root       
```
# 删除二叉搜索树中的节点

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0450.%E5%88%A0%E9%99%A4%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E8%8A%82%E7%82%B9.md

递归三部曲：

1.确定递归函数和参数

```
TreeNode* deleteNode(TreeNode* root, int key)
```

2.确定终止条件

```
if (root == nullptr) return root;
```

3.确定单层递归逻辑

有以下五种情况：

- 第一种情况：没找到删除的节点，遍历到空节点直接返回了
- 找到删除的节点
  - 第二种情况：左右孩子都为空（叶子节点），直接删除节点， 返回NULL为根节点
  - 第三种情况：删除节点的左孩子为空，右孩子不为空，删除节点，右孩子补位，返回右孩子为根节点
  - 第四种情况：删除节点的右孩子为空，左孩子不为空，删除节点，左孩子补位，返回左孩子为根节点
  - 第五种情况：左右孩子节点都不为空，则将删除节点的左子树头结点（左孩子）放到删除节点的右子树的最左面节点的左孩子上，返回删除节点右孩子为新的根节点。

![450.删除二叉搜索树中的节点](https://camo.githubusercontent.com/08973539011a17808beec01ad99749f6eb5c74ee46f4e5cdfd698ba93eed9456/68747470733a2f2f636f64652d7468696e6b696e672e63646e2e626365626f732e636f6d2f676966732f3435302e2545352538382541302545392539392541342545342542412538432545352538462538392545362539302539432545372542342541322545362541302539312545342542382541442545372539412538342545382538412538322545372538322542392e676966)

```python
class Solution:
    def deleteNode(self, root, key):
        if root is None:
            return root
        if root.val == key:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                cur = root.right
                while cur.left is not None:
                    cur = cur.left
                cur.left = root.left
                return root.right
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        return root
```

版本二

```python
class Solution:
    def deleteNode(self, root, key):
        if root is None:  # 如果根节点为空，直接返回
            return root
        if root.val == key:  # 找到要删除的节点
            if root.right is None:  # 如果右子树为空，直接返回左子树作为新的根节点
                return root.left
            cur = root.right
            while cur.left:  # 找到右子树中的最左节点
                cur = cur.left
            root.val, cur.val = cur.val, root.val  # 将要删除的节点值与最左节点值交换
        root.left = self.deleteNode(root.left, key)  # 在左子树中递归删除目标节点
        root.right = self.deleteNode(root.right, key)  # 在右子树中递归删除目标节点
        return root
```

# 修剪二叉搜索树

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0669.%E4%BF%AE%E5%89%AA%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.md

递归三部曲:

1.确定递归函数和参数：

这里我们为什么需要返回值呢？

因为是要遍历整棵树，做修改，其实不需要返回值也可以，我们也可以完成修剪（其实就是从二叉树中移除节点）的操作。

但是有返回值，更方便，可以通过递归函数的返回值来移除节点。

```
TreeNode* trimBST(TreeNode* root, int low, int high)
```

2.确定单层递归逻辑：

如果root（当前节点）的元素小于low的数值，那么应该递归右子树，并返回右子树符合条件的头结点。

代码如下：

```
if (root->val < low) {
    TreeNode* right = trimBST(root->right, low, high); // 寻找符合区间[low, high]的节点
    return right;
}
```

如果root(当前节点)的元素大于high的，那么应该递归左子树，并返回左子树符合条件的头结点。

```
if (root->val > high) {
    TreeNode* left = trimBST(root->left, low, high); // 寻找符合区间[low, high]的节点
    return left;
}
```

接下来要将下一层处理完左子树的结果赋给root->left，处理完右子树的结果赋给root->right。最后返回root节点，代码如下：

```
root->left = trimBST(root->left, low, high); // root->left接入符合条件的左孩子
root->right = trimBST(root->right, low, high); // root->right接入符合条件的右孩子
return root;
```

![669.修剪二叉搜索树1](https://camo.githubusercontent.com/6e56cef023c285aaeab11fbce95b54bf334dbb1137a030cccf33c4c090006ecb/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303231303230343135353332373230332d32303233303331303132303132363733382e706e67)

如下代码相当于把节点0的右孩子（节点2）返回给上一层，

```
if (root->val < low) {
    TreeNode* right = trimBST(root->right, low, high); // 寻找符合区间[low, high]的节点
    return right;
}
```

然后如下代码相当于用节点3的左孩子 把下一层返回的 节点0的右孩子（节点2） 接住。

```
root->left = trimBST(root->left, low, high);
```

```python
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if root is None:
            return None
        if root.val < low:
            # 寻找符合区间 [low, high] 的节点
            return self.trimBST(root.right, low, high)
        if root.val > high:
            # 寻找符合区间 [low, high] 的节点
            return self.trimBST(root.left, low, high)
        root.left = self.trimBST(root.left, low, high)  # root.left 接入符合条件的左孩子
        root.right = self.trimBST(root.right, low, high)  # root.right 接入符合条件的右孩子
        return root
```

迭代法：

因为二叉搜索树的有序性，不需要使用栈模拟递归的过程。

在剪枝的时候，可以分为三步：

- 将root移动到[L, R] 范围内，注意是左闭右闭区间
- 剪枝左子树
- 剪枝右子树

```python
class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return None
        
        # 处理头结点，让root移动到[L, R] 范围内，注意是左闭右闭
        while root and (root.val < L or root.val > R):
            if root.val < L:
                root = root.right  # 小于L往右走
            else:
                root = root.left  # 大于R往左走
        
        cur = root
        
        # 此时root已经在[L, R] 范围内，处理左孩子元素小于L的情况
        while cur:
            while cur.left and cur.left.val < L:
                cur.left = cur.left.right
            cur = cur.left
        
        cur = root
        
        # 此时root已经在[L, R] 范围内，处理右孩子大于R的情况
        while cur:
            while cur.right and cur.right.val > R:
                cur.right = cur.right.left
            cur = cur.right
        
        return root
```
# 将有序数组转换为二叉搜索树

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0108.%E5%B0%86%E6%9C%89%E5%BA%8F%E6%95%B0%E7%BB%84%E8%BD%AC%E6%8D%A2%E4%B8%BA%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.md

递归三部曲：

1.确定递归函数和参数：

```
// 左闭右闭区间[left, right]
TreeNode* traversal(vector<int>& nums, int left, int right)
```

2.确定终止条件：

```
if (left > right) return nullptr;
```

3.确定单层递归逻辑

```
int mid = left + ((right - left) / 2);
TreeNode* root = new TreeNode(nums[mid]);
root->left = traversal(nums, left, mid - 1);
root->right = traversal(nums, mid + 1, right);
return root;
```

```python
class Solution:
    def traversal(self, nums: List[int], left: int, right: int) -> TreeNode:
        if left > right:
            return None
        
        mid = left + (right - left) // 2
        root = TreeNode(nums[mid])
        root.left = self.traversal(nums, left, mid - 1)
        root.right = self.traversal(nums, mid + 1, right)
        return root
    
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        root = self.traversal(nums, 0, len(nums) - 1)
        return root
```

# 把二叉搜索树转换成累加树(反中序遍历)

**其实这就是一棵树，大家可能看起来有点别扭，换一个角度来看，这就是一个有序数组[2, 5, 13]，求从后到前的累加数组，也就是[20, 18, 13]，是不是感觉这就简单了。**

因为数组大家都知道怎么遍历啊，从后向前，挨个累加就完事了，这换成了二叉搜索树，看起来就别扭了一些是不是。

那么知道如何遍历这个二叉树，也就迎刃而解了，**从树中可以看出累加的顺序是右中左，所以我们需要反中序遍历这个二叉树，然后顺序累加就可以了**。

![538.把二叉搜索树转换为累加树](https://camo.githubusercontent.com/87981180b104dc1521e68fbc96f92c77732d9a9320ef2400dfb9fea7a29c8987/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303231303230343135333434303636362e706e67)

本题依然需要一个pre指针记录当前遍历节点cur的前一个节点，这样才方便做累加。

pre指针的使用技巧，我们在**二叉树：搜索树的最小绝对差**提到了，这是常用的操作手段。

递归三部曲：

1.确定递归函数和参数：

```
int pre = 0; // 记录前一个节点的数值
void traversal(TreeNode* cur)
```

2.确定终止条件：

```
if (cur == NULL) return;
```

3.确定单层递归逻辑

```
traversal(cur->right);  // 右
cur->val += pre;        // 中
pre = cur->val;
traversal(cur->left);   // 左
```

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.pre = 0  # 记录前一个节点的数值
        self.traversal(root)
        return root
    def traversal(self, cur):
        if cur is None:
            return        
        self.traversal(cur.right)
        cur.val += self.pre
        self.pre = cur.val
        self.traversal(cur.left)
```

迭代法：

```python
class Solution:
    def __init__(self):
        self.pre = 0  # 记录前一个节点的数值
    
    def traversal(self, root):
        stack = []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.right  # 右
            else:
                cur = stack.pop()  # 中
                cur.val += self.pre
                self.pre = cur.val
                cur = cur.left  # 左
    
    def convertBST(self, root):
        self.pre = 0
        self.traversal(root)
        return root
```