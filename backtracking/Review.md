# 回溯算法模板

```
void backtracking(参数) {
    if (终止条件) {
        存放结果;
        return;
    }

    for (选择：本层集合中元素（树中节点孩子的数量就是集合的大小）) {
        处理节点;
        backtracking(路径，选择列表); // 递归
        回溯，撤销处理结果
    }
}
```

# 组合1

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

# 组合3

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

# 电话号码字符组合

[leetcode-master/problems/0017.电话号码的字母组合.md at master · zihao-cpu/leetcode-master](https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0017.%E7%94%B5%E8%AF%9D%E5%8F%B7%E7%A0%81%E7%9A%84%E5%AD%97%E6%AF%8D%E7%BB%84%E5%90%88.md)

数字和字母如何映射

```
const string letterMap[10] = {
    "", // 0
    "", // 1
    "abc", // 2
    "def", // 3
    "ghi", // 4
    "jkl", // 5
    "mno", // 6
    "pqrs", // 7
    "tuv", // 8
    "wxyz", // 9
};
```

递归三部曲：

1.确定递归函数和参数：

首先需要一个字符串s来收集叶子节点的结果，然后用一个字符串数组result保存起来，这两个变量我依然定义为全局。

再来看参数，参数指定是有题目中给的string digits，然后还要有一个参数就是int型的index。

注意这个index可不是 [77.组合](https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html)和[216.组合总和III](https://programmercarl.com/0216.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CIII.html)中的startIndex了。

这个index是记录遍历第几个数字了，就是用来遍历digits的（题目中给出数字字符串），同时index也表示树的深度。

```
vector<string> result;
string s;
void backtracking(const string& digits, int index)
```

2.确定终止条件：

例如输入用例"23"，两个数字，那么根节点往下递归两层就可以了，叶子节点就是要收集的结果集。

那么终止条件就是如果index 等于 输入的数字个数（digits.size）了（本来index就是用来遍历digits的）。

然后收集结果，结束本层递归。

```
if (index == digits.size()) {
    result.push_back(s);
    return;
}
```

3.确定单层递归逻辑：

首先要取index指向的数字，并找到对应的字符集（手机键盘的字符集）。

然后for循环来处理这个字符集，代码如下：

```
int digit = digits[index] - '0';        // 将index指向的数字转为int
string letters = letterMap[digit];      // 取数字对应的字符集
for (int i = 0; i < letters.size(); i++) {
    s.push_back(letters[i]);            // 处理
    backtracking(digits, index + 1);    // 递归，注意index+1，一下层要处理下一个数字了
    s.pop_back();                       // 回溯
}
```



![17. 电话号码的字母组合](https://camo.githubusercontent.com/ae8f089040e7c9fabedfaeddc935a028db0dd74672d8d1205b7da91ec52210d1/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303230313132333230303330343436392e706e67)

```python
class Solution:
    def __init__(self):
        self.letterMap = [
            "",     # 0
            "",     # 1
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs", # 7
            "tuv",  # 8
            "wxyz"  # 9
        ]
        self.result = []
        self.s = ""

    def backtracking(self, digits, index):
        if index == len(digits):
            self.result.append(self.s)
            return
        digit = int(digits[index])    # 将索引处的数字转换为整数
        letters = self.letterMap[digit]    # 获取对应的字符集
        for i in range(len(letters)):
            self.s += letters[i]    # 处理字符
            self.backtracking(digits, index + 1)    # 递归调用，注意索引加1，处理下一个数字
            self.s = self.s[:-1]    # 回溯，删除最后添加的字符

    def letterCombinations(self, digits):
        if len(digits) == 0:
            return self.result
        self.backtracking(digits, 0)
        return self.result
```
# 组合总和

[leetcode-master/problems/0039.组合总和.md at master · zihao-cpu/leetcode-master](https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0039.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8C.md)

![39.组合总和](https://camo.githubusercontent.com/7c8b1de05154bec1e4bdbe6aa4d6e647905fc1a0d56489a4c32c25cd5f825b62/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303230313232333137303733303336372e706e67)

递归三部曲：

1.确定递归函数和参数

这里依然是定义两个全局变量，二维数组result存放结果集，数组path存放符合条件的结果。（这两个变量可以作为函数参数传入）

首先是题目中给出的参数，集合candidates, 和目标值target。

此外我还定义了int型的sum变量来统计单一结果path里的总和，其实这个sum也可以不用，用target做相应的减法就可以了，最后如何target==0就说明找到符合的结果了，但为了代码逻辑清晰，我依然用了sum。**本题还需要startIndex来控制for循环的起始位置，对于组合问题，什么时候需要startIndex呢？**

我举过例子，**如果是一个集合来求组合的话，就需要startIndex**

```
vector<vector<int>> result;
vector<int> path;
void backtracking(vector<int>& candidates, int target, int sum, int startIndex)
```

2.递归终止条件：

从叶子节点可以清晰看到，终止只有两种情况，sum大于target和sum等于target。

sum等于target的时候，需要收集结果，代码如下：

```
if (sum > target) {
    return;
}
if (sum == target) {
    result.push_back(path);
    return;
}
```

3.单层递归逻辑：

单层for循环依然是从startIndex开始，搜索candidates集合。

**注意本题和77.组合、216.组合总和III的一个区别是：本题元素为可重复选取的**。

如何重复选取呢，看代码，注释部分：

```
for (int i = startIndex; i < candidates.size(); i++) {
    sum += candidates[i];
    path.push_back(candidates[i]);
    backtracking(candidates, target, sum, i); // 关键点:不用i+1了，表示可以重复读取当前的数
    sum -= candidates[i];   // 回溯
    path.pop_back();        // 回溯
}
```

```python
class Solution:

    def backtracking(self, candidates, target, total, startIndex, path, result):
        if total > target:
            return
        if total == target:
            result.append(path[:])
            return

        for i in range(startIndex, len(candidates)):
            total += candidates[i]
            path.append(candidates[i])
            self.backtracking(candidates, target, total, i, path, result)  # 不用i+1了，表示可以重复读取当前的数
            total -= candidates[i]
            path.pop()

    def combinationSum(self, candidates, target):
        result = []
        self.backtracking(candidates, target, 0, 0, [], result)
        return result
```

# 组合总和2

递归三部曲：

1.确定递归函数和参数:

```
vector<vector<int>> result; // 存放组合集合
vector<int> path;           // 符合条件的组合
void backtracking(vector<int>& candidates, int target, int sum, int startIndex, vector<bool>& used) {
```

2.确定终止条件：

```
if (sum > target) { // 这个条件其实可以省略
    return;
}
if (sum == target) {
    result.push_back(path);
    return;
}
```

3.确定单层递归逻辑：

前面我们提到：要去重的是“同一树层上的使用过”，如何判断同一树层上元素（相同的元素）是否使用过了呢。

**如果candidates[i] == candidates[i - 1] 并且 used[i - 1] == false，就说明：前一个树枝，使用了candidates[i - 1]，也就是说同一树层使用过candidates[i - 1]**。

此时for循环里就应该做continue的操作。

![40.组合总和II1](https://camo.githubusercontent.com/ed15c1a2231344d68975dbe8adace2e04788d8e1dec1e48bffd91207969d81a9/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303233303331303030303935342e706e67)

我在图中将used的变化用橘黄色标注上，可以看出在candidates[i] == candidates[i - 1]相同的情况下：

- used[i - 1] == true，说明同一树枝candidates[i - 1]使用过
- used[i - 1] == false，说明同一树层candidates[i - 1]使用过

![img](https://camo.githubusercontent.com/0f8088f3c695785f6e4084aca29ff788cd31632e610901be43b6a9f7ee723b93/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303232313032313136333831322e706e67)

```
for (int i = startIndex; i < candidates.size() && sum + candidates[i] <= target; i++) {
    // used[i - 1] == true，说明同一树枝candidates[i - 1]使用过
    // used[i - 1] == false，说明同一树层candidates[i - 1]使用过
    // 要对同一树层使用过的元素进行跳过
    if (i > 0 && candidates[i] == candidates[i - 1] && used[i - 1] == false) {
        continue;
    }
    sum += candidates[i];
    path.push_back(candidates[i]);
    used[i] = true;
    backtracking(candidates, target, sum, i + 1, used); // 和39.组合总和的区别1：这里是i+1，每个数字在每个组合中只能使用一次
    used[i] = false;
    sum -= candidates[i];
    path.pop_back();
}
```

class Solution:


```python
def backtracking(self, candidates, target, total, startIndex, used, path, result):
    if total == target:
        result.append(path[:])
        return

    for i in range(startIndex, len(candidates)):
        # 对于相同的数字，只选择第一个未被使用的数字，跳过其他相同数字
        if i > startIndex and candidates[i] == candidates[i - 1] and not used[i - 1]:
            continue

        if total + candidates[i] > target:
            break

        total += candidates[i]
        path.append(candidates[i])
        used[i] = True
        self.backtracking(candidates, target, total, i + 1, used, path, result)
        used[i] = False
        total -= candidates[i]
        path.pop()

def combinationSum2(self, candidates, target):
    used = [False] * len(candidates)
    result = []
    candidates.sort()
    self.backtracking(candidates, target, 0, 0, used, [], result)
    return result
```
class Solution:


```python
def backtracking(self, candidates, target, total, startIndex, path, result):
    if total == target:
        result.append(path[:])
        return

    for i in range(startIndex, len(candidates)):
        if i > startIndex and candidates[i] == candidates[i - 1]:
            continue

        if total + candidates[i] > target:
            break

        total += candidates[i]
        path.append(candidates[i])
        self.backtracking(candidates, target, total, i + 1, path, result)
        total -= candidates[i]
        path.pop()

def combinationSum2(self, candidates, target):
    result = []
    candidates.sort()
    self.backtracking(candidates, target, 0, 0, [], result)
    return result
```


```python
class Solution:


    def backtracking(self, candidates, target, total, startIndex, path, result):
        if total == target:
            result.append(path[:])
            return

        for i in range(startIndex, len(candidates)):
            if i > startIndex and candidates[i] == candidates[i - 1]:
                continue

            if total + candidates[i] > target:
                break

            total += candidates[i]
            path.append(candidates[i])
            self.backtracking(candidates, target, total, i + 1, path, result)
            total -= candidates[i]
            path.pop()

    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()
        self.backtracking(candidates, target, 0, 0, [], result)
        return result

```



# 分割回文串

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0131.%E5%88%86%E5%89%B2%E5%9B%9E%E6%96%87%E4%B8%B2.md

![131.分割回文串](https://camo.githubusercontent.com/eb7d2ca0bbcbe1950d45c6927f10b39d50f6e436591ca0ba1d5ddeea49e0f6c2/68747470733a2f2f636f64652d7468696e6b696e672e63646e2e626365626f732e636f6d2f706963732f3133312e2545352538382538362545352538392542322545352539422539452545362539362538372545342542382542322e6a7067)

递归三部曲：

1.确定递归函数和参数：

全局变量数组path存放切割后回文的子串，二维数组result存放结果集。 （这两个参数可以放到函数参数里）

本题递归函数参数还需要startIndex，因为切割过的地方，不能重复切割，和组合问题也是保持一致的。

```
vector<vector<string>> result;
vector<string> path; // 放已经回文的子串
void backtracking (const string& s, int startIndex) {
```

2.确定终止条件：

在处理组合问题的时候，递归参数需要传入startIndex，表示下一轮递归遍历的起始位置，这个startIndex就是切割线。

所以终止条件代码如下：

```
void backtracking (const string& s, int startIndex) {
    // 如果起始位置已经大于s的大小，说明已经找到了一组分割方案了
    if (startIndex >= s.size()) {
        result.push_back(path);
        return;
    }
}
```

3.单层递归逻辑：

```
for (int i = startIndex; i < s.size(); i++) {
    if (isPalindrome(s, startIndex, i)) { // 是回文子串
        // 获取[startIndex,i]在s中的子串
        string str = s.substr(startIndex, i - startIndex + 1);
        path.push_back(str);
    } else {                // 如果不是则直接跳过
        continue;
    }
    backtracking(s, i + 1); // 寻找i+1为起始位置的子串
    path.pop_back();        // 回溯过程，弹出本次已经添加的子串
}
```

```python
class Solution:

    def partition(self, s: str) -> List[List[str]]:
        '''
        递归用于纵向遍历
        for循环用于横向遍历
        当切割线迭代至字符串末尾，说明找到一种方法
        类似组合问题，为了不重复切割同一位置，需要start_index来做标记下一轮递归的起始位置(切割线)
        '''
        result = []
        self.backtracking(s, 0, [], result)
        return result

    def backtracking(self, s, start_index, path, result ):
        # Base Case
        if start_index == len(s):
            result.append(path[:])
            return
        
        # 单层递归逻辑
        for i in range(start_index, len(s)):
            # 此次比其他组合题目多了一步判断：
            # 判断被截取的这一段子串([start_index, i])是否为回文串
            if self.is_palindrome(s, start_index, i):
                path.append(s[start_index:i+1])
                self.backtracking(s, i+1, path, result)   # 递归纵向遍历：从下一处进行切割，判断其余是否仍为回文串
                path.pop()             # 回溯


    def is_palindrome(self, s: str, start: int, end: int) -> bool:
        i: int = start        
        j: int = end
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True 
```

# 复原IP地址

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0093.%E5%A4%8D%E5%8E%9FIP%E5%9C%B0%E5%9D%80.md

递归三部曲：

1.确定递归函数和参数：

在[131.分割回文串](https://programmercarl.com/0131.%E5%88%86%E5%89%B2%E5%9B%9E%E6%96%87%E4%B8%B2.html)中我们就提到切割问题类似组合问题。

startIndex一定是需要的，因为不能重复分割，记录下一层递归分割的起始位置。

本题我们还需要一个变量pointNum，记录添加逗点的数量。

所以代码如下：

```
vector<string> result;// 记录结果
// startIndex: 搜索的起始位置，pointNum:添加逗点的数量
void backtracking(string& s, int startIndex, int pointNum) {
```

2.确定终止条件：

终止条件和[131.分割回文串](https://programmercarl.com/0131.%E5%88%86%E5%89%B2%E5%9B%9E%E6%96%87%E4%B8%B2.html)情况就不同了，本题明确要求只会分成4段，所以不能用切割线切到最后作为终止条件，而是分割的段数作为终止条件。

pointNum表示逗点数量，pointNum为3说明字符串分成了4段了。

然后验证一下第四段是否合法，如果合法就加入到结果集里

代码如下：

```
if (pointNum == 3) { // 逗点数量为3时，分隔结束
    // 判断第四段子字符串是否合法，如果合法就放进result中
    if (isValid(s, startIndex, s.size() - 1)) {
        result.push_back(s);
    }
    return;
}
```

3.确定单层递归逻辑：

在[131.分割回文串](https://programmercarl.com/0131.%E5%88%86%E5%89%B2%E5%9B%9E%E6%96%87%E4%B8%B2.html)中已经讲过在循环遍历中如何截取子串。

在`for (int i = startIndex; i < s.size(); i++)`循环中 [startIndex, i] 这个区间就是截取的子串，需要判断这个子串是否合法。

如果合法就在字符串后面加上符号`.`表示已经分割。

如果不合法就结束本层循环，如图中剪掉的分支

![93.复原IP地址](https://camo.githubusercontent.com/7e8d3b4814c59bfb7f5e13bb177f83aca30ef0cfd000e29405a7e8cf1b5d6679/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303230313132333230333733353933332d32303233303331303133323331343130392e706e67)

然后就是递归和回溯的过程：

递归调用时，下一层递归的startIndex要从i+2开始（因为需要在字符串中加入了分隔符`.`），同时记录分割符的数量pointNum 要 +1。

回溯的时候，就将刚刚加入的分隔符`.` 删掉就可以了，pointNum也要-1。

代码如下：

```
for (int i = startIndex; i < s.size(); i++) {
    if (isValid(s, startIndex, i)) { // 判断 [startIndex,i] 这个区间的子串是否合法
        s.insert(s.begin() + i + 1 , '.');  // 在i的后面插入一个逗点
        pointNum++;
        backtracking(s, i + 2, pointNum);   // 插入逗点之后下一个子串的起始位置为i+2
        pointNum--;                         // 回溯
        s.erase(s.begin() + i + 1);         // 回溯删掉逗点
    } else break; // 不合法，直接结束本层循环
}
```



```python
class Solution:
    def __init__(self):
        self.result = []  # 用于存储结果

    def restoreIpAddresses(self, s: str):
        if len(s) > 12:  # 算是剪枝了
            return self.result  # 如果字符串长度大于12，直接返回空结果
        self.backTrack(s, 0, 0)  # 初始化回溯
        return self.result

    # start_index: 搜索的起始位置， point_num: 添加逗点的数量
    def backTrack(self, s, start_index, point_num):
        if point_num == 3:  # 逗点数量为3时，分隔结束
            if self.isValid(s, start_index, len(s) - 1):  # 判断第四段子字符串是否合法
                self.result.append(s)  # 如果合法，将结果添加到list中
            return

        for i in range(start_index, len(s)):
            if self.isValid(s, start_index, i):  # 判断 [start_index, i] 这个区间的子串是否合法
                s = s[:i + 1] + "." + s[i + 1:]  # 在s[i+1]后面插入一个逗点
                point_num += 1
                self.backTrack(s, i + 2, point_num)  # 插入逗点后，下一个子串的起始位置为i+2
                point_num -= 1  # 回溯
                s = s[:i + 1] + s[i + 2:]  # 回溯删除逗点
            else:
                break  # 不合法，直接结束本层循环

    # 判断字符串s在[start, end]所组成的数字是否合法
    def isValid(self, s, start, end):
        if start > end:
            return False
        if s[start] == '0' and start != end:  # 0开头的数字不合法
            return False
        num = 0
        for i in range(start, end + 1):
            if s[i] > '9' or s[i] < '0':  # 遇到非数字字符不合法
                return False
            num = num * 10 + int(s[i])  # 计算数字
            if num > 255:  # 如果数字大于255，不合法
                return False
        return True
```



# 子集

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0078.%E5%AD%90%E9%9B%86.md

求子集问题和[77.组合](https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html)和[131.分割回文串](https://programmercarl.com/0131.%E5%88%86%E5%89%B2%E5%9B%9E%E6%96%87%E4%B8%B2.html)又不一样了。

如果把 子集问题、组合问题、分割问题都抽象为一棵树的话，**那么组合问题和分割问题都是收集树的叶子节点，而子集问题是找树的所有节点！**

其实子集也是一种组合问题，因为它的集合是无序的，子集{1,2} 和 子集{2,1}是一样的。

**那么既然是无序，取过的元素不会重复取，写回溯算法的时候，for就要从startIndex开始，而不是从0开始！**

有同学问了，什么时候for可以从0开始呢？

求排列问题的时候，就要从0开始，因为集合是有序的，{1, 2} 和{2, 1}是两个集合，排列问题我们后续的文章就会讲到的。

递归三部曲：

1.确定递归函数和参数：

全局变量数组path为子集收集元素，二维数组result存放子集组合。（也可以放到递归函数参数里）

递归函数参数在上面讲到了，需要startIndex。

```
vector<vector<int>> result;
vector<int> path;
void backtracking(vector<int>& nums, int startIndex) {
```

2.确定终止函数

```
if (startIndex >= nums.size()) {
    return;
}
```

3.确定单层递归逻辑：

```
for (int i = startIndex; i < nums.size(); i++) {
    path.push_back(nums[i]);    // 子集收集元素
    backtracking(nums, i + 1);  // 注意从i+1开始，元素不重复取
    path.pop_back();            // 回溯
}
```

```python
class Solution:
    def subsets(self, nums):
        result = []
        path = []
        self.backtracking(nums, 0, path, result)
        return result

    def backtracking(self, nums, startIndex, path, result):
        result.append(path[:])  # 收集子集，要放在终止添加的上面，否则会漏掉自己
         if startIndex >= len(nums):  # 终止条件可以不加
             return
        for i in range(startIndex, len(nums)):
            path.append(nums[i])
            self.backtracking(nums, i + 1, path, result)
            path.pop()
```
# 子集2

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0090.%E5%AD%90%E9%9B%86II.md

![90.子集II](https://camo.githubusercontent.com/6c5581f950c575b696075adb09ff83b20da855bfe8885d56340a46c003f52d14/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303230313132343139353431313937372e706e67)

```python
class Solution:
    def subsetsWithDup(self, nums):
        result = []
        path = []
        used = [False] * len(nums)
        nums.sort()  # 去重需要排序
        self.backtracking(nums, 0, used, path, result)
        return result

    def backtracking(self, nums, startIndex, used, path, result):
        result.append(path[:])  # 收集子集
        for i in range(startIndex, len(nums)):
            # used[i - 1] == True，说明同一树枝 nums[i - 1] 使用过
            # used[i - 1] == False，说明同一树层 nums[i - 1] 使用过
            # 而我们要对同一树层使用过的元素进行跳过
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            path.append(nums[i])
            used[i] = True
            self.backtracking(nums, i + 1, used, path, result)
            used[i] = False
            path.pop()
```

用set来去重

```python
class Solution:
    def subsetsWithDup(self, nums):
        result = []
        path = []
        nums.sort()  # 去重需要排序
        self.backtracking(nums, 0, path, result)
        return result

    def backtracking(self, nums, startIndex, path, result):
        result.append(path[:])  # 收集子集
        uset = set()
        for i in range(startIndex, len(nums)):
            if nums[i] in uset:
                continue
            uset.add(nums[i])
            path.append(nums[i])
            self.backtracking(nums, i + 1, path, result)
            path.pop()
```



# 递增子序列

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0491.%E9%80%92%E5%A2%9E%E5%AD%90%E5%BA%8F%E5%88%97.md

![img](https://camo.githubusercontent.com/b6f87952d3994dd67f64866a26c5ed7d73c932ea5d7b9d36d9cdaec085dfdf10/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303230313132343230303232393832342e706e67)

在[90.子集II](https://programmercarl.com/0090.%E5%AD%90%E9%9B%86II.html)中我们是通过排序，再加一个标记数组来达到去重的目的。

而本题求自增子序列，是不能对原数组进行排序的，排完序的数组都是自增子序列了

递归三部曲：

1.确定递归函数和参数：

```
vector<vector<int>> result;
vector<int> path;
void backtracking(vector<int>& nums, int startIndex)
```

2.确定终止条件：

```
if (path.size() > 1) {
    result.push_back(path);
    // 注意这里不要加return，因为要取树上的所有节点
}
```

3.单层递归逻辑：

![491. 递增子序列1](https://camo.githubusercontent.com/af5364c9333b307f1b6af25b3a1c2c810bf500420f001cd9c625d9b6c635038d/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303230313132343230303232393832342d32303233303331303133313634303037302e706e67)

```python
class Solution:
    def findSubsequences(self, nums):
        result = []
        path = []
        self.backtracking(nums, 0, path, result)
        return result
    
    def backtracking(self, nums, startIndex, path, result):
        if len(path) > 1:
            result.append(path[:])  # 注意要使用切片将当前路径的副本加入结果集
            # 注意这里不要加return，要取树上的节点
        
        uset = set()  # 使用集合对本层元素进行去重
        for i in range(startIndex, len(nums)):
            if (path and nums[i] < path[-1]) or nums[i] in uset:
                continue
            
            uset.add(nums[i])  # 记录这个元素在本层用过了，本层后面不能再用了
            path.append(nums[i])
            self.backtracking(nums, i + 1, path, result)
            path.pop()
```

# 全排列

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0046.%E5%85%A8%E6%8E%92%E5%88%97.md

递归三部曲：

1.确定递归函数和参数：

**首先排列是有序的，也就是说 [1,2] 和 [2,1] 是两个集合，这和之前分析的子集以及组合所不同的地方**。

可以看出元素1在[1,2]中已经使用过了，但是在[2,1]中还要在使用一次1，所以处理排列问题就不用使用startIndex了。

但排列问题需要一个used数组，标记已经选择的元素，如图橘黄色部分所示:

![img](https://camo.githubusercontent.com/7e6b2ad9dfa8e2918ca2c78b4b01e2714f13bb2c6bfef2a4b7c39b21aa87d2fc/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303234303830333138303331382e706e67)

2.确定终止条件：

```
// 此时说明找到了一组
if (path.size() == nums.size()) {
    result.push_back(path);
    return;
}
```

3.确定单层逻辑：

因为排列问题，每次都要从头开始搜索，例如元素1在[1,2]中已经使用过了，但是在[2,1]中还要再使用一次1。

**而used数组，其实就是记录此时path里都有哪些元素使用了，一个排列里一个元素只能使用一次**。

```
for (int i = 0; i < nums.size(); i++) {
    if (used[i] == true) continue; // path里已经收录的元素，直接跳过
    used[i] = true;
    path.push_back(nums[i]);
    backtracking(nums, used);
    path.pop_back();
    used[i] = false;
}
```

```python
class Solution:
    def permute(self, nums):
        result = []
        self.backtracking(nums, [], [False] * len(nums), result)
        return result

    def backtracking(self, nums, path, used, result):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            self.backtracking(nums, path, used, result)
            path.pop()
            used[i] = False
```

