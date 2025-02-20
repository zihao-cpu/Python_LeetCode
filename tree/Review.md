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

