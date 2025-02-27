# 组合

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0077.%E7%BB%84%E5%90%88.md

![77.组合](https://camo.githubusercontent.com/d2c6f37e31e4caef0dd145680cb58e591c8cf75ff2856eea770a8c359300c217/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303230313132333139353232333934302e706e67)

递归三部曲：

1.确定递归函数和参数：

其实不定义这两个全局变量也是可以的，把这两个变量放进递归函数的参数里，但函数里参数太多影响可读性，所以我定义全局变量了。

函数里一定有两个参数，既然是集合n里面取k个数，那么n和k是两个int型的参数。

然后还需要一个参数，为int型变量startIndex，这个参数用来记录本层递归的中，集合从哪里开始遍历（集合就是[1,...,n] ）。

为什么要有这个startIndex呢？

从下图中红线部分可以看出，在集合[1,2,3,4]取1之后，下一层递归，就要在[2,3,4]中取数了，那么下一层递归如何知道从[2,3,4]中取数呢，靠的就是startIndex。

![77.组合2](https://camo.githubusercontent.com/365aed5b932e1c30228446f5357e60604be6f631793b56d7d3ddb3136e7e8910/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303230313132333139353332383937362e706e67)

```
vector<vector<int>> result; // 存放符合条件结果的集合
vector<int> path; // 用来存放符合条件单一结果
void backtracking(int n, int k, int startIndex)
```

2.确定终止条件：

什么时候到达所谓的叶子节点了呢？

path这个数组的大小如果达到k，说明我们找到了一个子集大小为k的组合了，在图中path存的就是根节点到叶子节点的路径。

![77.组合3](https://camo.githubusercontent.com/4f01340297709eb8129de4caec0d11b4b7a2522d06c6dc0f09595e3da4aca5f2/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303230313132333139353430373930372e706e67)

```
if (path.size() == k) {
    result.push_back(path);
    return;
}
```

3.确定单层递归逻辑：

![77.组合1](https://camo.githubusercontent.com/558dd7ef431a376d273b6355d3ed95b8a9fe3b0d0cf77ee083072136386e4b25/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303230313132333139353234323839392e706e67)

```
for (int i = startIndex; i <= n; i++) { // 控制树的横向遍历
    path.push_back(i); // 处理节点
    backtracking(n, k, i + 1); // 递归：控制树的纵向遍历，注意下一层搜索要从i+1开始
    path.pop_back(); // 回溯，撤销处理的节点
}
```

```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []  # 存放结果集
        self.backtracking(n, k, 1, [], result)
        return result
    def backtracking(self, n, k, startIndex, path, result):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(startIndex, n + 1):  # 需要优化的地方
            path.append(i)  # 处理节点
            self.backtracking(n, k, i + 1, path, result)
            path.pop()  # 回溯，撤销处理的节点

```

# 组合$\mathrm{iii}$

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0216.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CIII.md

![216.组合总和III](https://camo.githubusercontent.com/3b0efa7e7cb574f29096b649007b85d8011684da9e87235d1459c3c634502894/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303230313132333139353731373937352e706e67)

递归三部曲：

1.确定递归函数和参数：

这里我依然定义path 和 result为全局变量。

至于为什么取名为path？从上面树形结构中，可以看出，结果其实就是一条根节点到叶子节点的路径。

```
vector<vector<int>> result; // 存放结果集
vector<int> path; // 符合条件的结果
```

- targetSum（int）目标和，也就是题目中的n。

- k（int）就是题目中要求k个数的集合。

- sum（int）为已经收集的元素的总和，也就是path里元素的总和。

- startIndex（int）为下一层for循环搜索的起始位置

  ```
  vector<vector<int>> result;
  vector<int> path;
  void backtracking(int targetSum, int k, int sum, int startIndex)
  ```

2.确定终止条件：

```
if (path.size() == k) {
    if (sum == targetSum) result.push_back(path);
    return; // 如果path.size() == k 但sum != targetSum 直接返回
}
```

3.确定单层递归逻辑：

![216.组合总和III](https://camo.githubusercontent.com/083c837711f645096bf34703c22532004b31751931cfddf3ac83a0286f04d77a/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303230313132333139353731373937352d32303233303331303131333534363030332e706e67)

```
for (int i = startIndex; i <= 9; i++) {
    sum += i;
    path.push_back(i);
    backtracking(targetSum, k, sum, i + 1); // 注意i+1调整startIndex
    sum -= i; // 回溯
    path.pop_back(); // 回溯
}
```

```python
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []  # 存放结果集
        self.backtracking(n, k, 0, 1, [], result)
        return result

    def backtracking(self, targetSum, k, currentSum, startIndex, path, result):
        if currentSum > targetSum:  # 剪枝操作
            return  # 如果path的长度等于k但currentSum不等于targetSum，则直接返回
        if len(path) == k:
            if currentSum == targetSum:
                result.append(path[:])
            return
        for i in range(startIndex, 9 - (k - len(path)) + 2):  # 剪枝
            currentSum += i  # 处理
            path.append(i)  # 处理
            self.backtracking(targetSum, k, currentSum, i + 1, path, result)  # 注意i+1调整startIndex
            currentSum -= i  # 回溯
            path.pop()  # 回溯
```

