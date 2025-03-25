**4.确定遍历顺序：从递归公式dp[i] = dp[i - 1] + dp[i - 2];中可以看出，dp[i]是依赖 dp[i - 1] 和 dp[i - 2]，那么遍历的顺序一定是从前到后遍历的**

**5.举例推导dp数组**

```python
class Solution:
    def fib(self, n: int) -> int:
       
        # 排除 Corner Case
        if n == 0:
            return 0
        
        # 创建 dp table 
        dp = [0] * (n + 1)

        # 初始化 dp 数组
        dp[0] = 0
        dp[1] = 1

        # 遍历顺序: 由前向后。因为后面要用到前面的状态
        for i in range(2, n + 1):

            # 确定递归公式/状态转移公式
            dp[i] = dp[i - 1] + dp[i - 2]
        
        # 返回答案
```

# 01背包问题

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/%E8%83%8C%E5%8C%85%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%8001%E8%83%8C%E5%8C%85-1.md



![动态规划-背包问题1](https://camo.githubusercontent.com/cc3a4b299e49893a6d42cd1b17d1efea92fbd2b7be3a3821daa0b756e1b68009/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303231303131303130333030333336312e706e67)

那么这里 i 、j、$$\text{dp}[i][j] $$分别表示什么呢？

i 来表示物品、j表示背包容量。



**1.我们先看把物品0 放入背包的情况：**

![img](https://camo.githubusercontent.com/2eae5c25034913169f6625c72261afc45b06d24eee427fcf135b6b90c06a4443/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303234303733303131333435352e706e67)

背包容量为0，放不下物品0，此时背包里的价值为0。

背包容量为1，可以放下物品0，此时背包里的价值为15.

背包容量为2，依然可以放下物品0 （注意 01背包里物品只有一个），此时背包里的价值为15。

以此类推。

**2.再看把物品1 放入背包：**

![img](https://camo.githubusercontent.com/e166e3b0e14b1304254d0426106aca0e4a143b4ee10bc08c60c43addc45ebd5d/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303234303733303131343232382e706e67)

背包容量为 0，放不下物品0 或者物品1，此时背包里的价值为0。

背包容量为 1，只能放下物品0，背包里的价值为15。

背包容量为 2，只能放下物品0，背包里的价值为15。

背包容量为 3，上一行同一状态，背包只能放物品0，这次也可以选择物品1了，背包可以放物品1 或者 物品0，物品1价值更大，背包里的价值为20。

背包容量为 4，上一行同一状态，背包只能放物品0，这次也可以选择物品1了，背包可以放下物品0 和 物品1，背包价值为35。



- **不放物品i：背包容量为j，里面不放物品i的最大价值是$$dp[i - 1][j]$$。**
- **放物品i：背包空出物品i的容量后，背包容量为j - weight[i]，$$dp[i - 1][j]$$为背包容量为j - weight[i]且不放物品i的最大价值，那么$$dp[i - 1][j-weight[i]]$$+ value[i] （物品i的价值），就是背包放物品i得到的最大价值**



```python
n, bagweight = map(int, input().split())

weight = list(map(int, input().split()))
value = list(map(int, input().split()))

dp = [[0] * (bagweight + 1) for _ in range(n)]

for j in range(weight[0], bagweight + 1):
    dp[0][j] = value[0]

for i in range(1, n):#遍历物品
    for j in range(bagweight + 1):#遍历背包
        if j < weight[i]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])

print(dp[n - 1][bagweight])
```

# 爬楼梯

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0070.%E7%88%AC%E6%A5%BC%E6%A2%AF.md

1. 确定dp数组以及下标的含义：dp[i]： 爬到第i层楼梯，有dp[i]种方法
2. 首先是dp[i - 1]，上i-1层楼梯，有dp[i - 1]种方法，那么再一步跳一个台阶不就是dp[i]了么。还有就是dp[i - 2]，上i-2层楼梯，有dp[i - 2]种方法，那么再一步跳两个台阶不就是dp[i]了么。那么dp[i]就是 dp[i - 1]与dp[i - 2]之和！所以dp[i] = dp[i - 1] + dp[i - 2] 。在推导dp[i]的时候，一定要时刻想着dp[i]的定义，否则容易跑偏。这体现出确定dp数组以及下标的含义的重要性！
3. 再回顾一下dp[i]的定义：爬到第i层楼梯，有dp[i]种方法。
4. 从递推公式dp[i] = dp[i - 1] + dp[i - 2];中可以看出，遍历顺序一定是从前向后遍历的
5. 举例推导dp数组

```python
# 空间复杂度为O(n)版本
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
      
      
# 空间复杂度为O(3)版本
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        
        dp = [0] * 3
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n + 1):
            total = dp[1] + dp[2]
            dp[1] = dp[2]
            dp[2] = total
        
        return dp[2]
      
# 空间复杂度为O(1)版本
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        
        prev1 = 1
        prev2 = 2
        
        for i in range(3, n + 1):
            total = prev1 + prev2
            prev1 = prev2
            prev2 = total
        
        return prev2
      
#递归版本 
class Solution:	
   def climbStairs(n):
      # 基础条件
      if n == 0:
          return 1
      elif n == 1:
          return 1
      # 递归
      return climbStairs(n-1) + climbStairs(n-2)
```

# 使用最小代价爬楼梯

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0746.%E4%BD%BF%E7%94%A8%E6%9C%80%E5%B0%8F%E8%8A%B1%E8%B4%B9%E7%88%AC%E6%A5%BC%E6%A2%AF.md

1.确定dp数组以及下标的含义:

使用动态规划，就要有一个数组来记录状态，本题只需要一个一维数组dp[i]就可以了。

**dp[i]的定义：到达第i台阶所花费的最少体力为dp[i]**。

2.确定递推公式：

**可以有两个途径得到dp[i]，一个是dp[i-1] 一个是dp[i-2]**。

dp[i - 1] 跳到 dp[i] 需要花费 dp[i - 1] + cost[i - 1]。

dp[i - 2] 跳到 dp[i] 需要花费 dp[i - 2] + cost[i - 2]。

那么究竟是选从dp[i - 1]跳还是从dp[i - 2]跳呢？

**一定是选最小的，所以dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]);**

3.dp数组的初始化：

4.确定遍历顺序：

因为是模拟台阶，而且dp[i]由dp[i-1]dp[i-2]推出，所以是从前到后遍历cost数组就可以了。

```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        dp[0] = 0  # 初始值，表示从起点开始不需要花费体力
        dp[1] = 0  # 初始值，表示经过第一步不需要花费体力
        
        for i in range(2, len(cost) + 1):
            # 在第i步，可以选择从前一步（i-1）花费体力到达当前步，或者从前两步（i-2）花费体力到达当前步
            # 选择其中花费体力较小的路径，加上当前步的花费，更新dp数组
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        
        return dp[len(cost)]  # 返回到达楼顶的最小花费
```

# 不同路径

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0062.%E4%B8%8D%E5%90%8C%E8%B7%AF%E5%BE%84.md

![img](https://camo.githubusercontent.com/63c57cb05ca42b118e5007f26a5dea9d0a381571cf7498087f8844aed5ab4f70/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303231303131303137343033333231352e706e67)

1.确定dp数组以及下标的含义:

$$dp[i][j]$$ ：表示从（0 ，0）出发，到(i, j) 有$$dp[i][j]$$条不同的路径。

2.确定递推公式：

想要求dp[i][j]，只能有两个方向来推导出来，即$$dp[i - 1][j] 和 dp[i][j - 1]$$。

此时在回顾一下$$ dp[i - 1][j] 表示啥，是从(0, 0)的位置到(i - 1, j)有几条路径，dp[i][j - 1]同理$$。

那么很自然，$$dp[i][j] = dp[i - 1][j] + dp[i][j - 1]$$，因为dp[i][j]只有这两个方向过来。

3.初始化：

如何初始化呢，首先dp[i][0]一定都是1，因为从(0, 0)的位置到(i, 0)的路径只有一条，那么dp[0][j]也同理。

```
for (int i = 0; i < m; i++) dp[i][0] = 1;
for (int j = 0; j < n; j++) dp[0][j] = 1;
```

4.确认遍历顺序：

这里要看一下递推公式$$dp[i][j] = dp[i - 1][j] + dp[i][j - 1]，dp[i][j]$$都是从其上方和左方推导而来，那么从左到右一层一层遍历就可以了。

这样就可以保证推导$$dp[i][j]$$的时候，$$dp[i - 1][j] 和 dp[i][j - 1]$$一定是有数值的。

```python
#递归的版本
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
#dp      
 class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 创建一个二维列表用于存储唯一路径数
        dp = [[0] * n for _ in range(m)]
        
        # 设置第一行和第一列的基本情况
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        # 计算每个单元格的唯一路径数
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        # 返回右下角单元格的唯一路径数
        return dp[m - 1][n - 1]     
      
```

# 不同路径2

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0063.%E4%B8%8D%E5%90%8C%E8%B7%AF%E5%BE%84II.md

1.确定dp数组以及下标的含义：

$$dp[i][j] ：表示从（0 ，0）出发，到(i, j) 有dp[i][j]条不同的路径。$$

2.确定递推公式：

注意这里是没有障碍物的时候才去记录的

```
if (obstacleGrid[i][j] == 0) { // 当(i, j)没有障碍的时候，再推导dp[i][j]
    dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
}
```

3.dp数组初始化：

![63.不同路径II](https://camo.githubusercontent.com/5a545948c1bcdd8c971ff487afad0c12864fda4f5c7a5ff9edbe2fdec6fb4b32/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303231303130343131343531333932382e706e67)

注意如果有个地方有障碍物 则 后面的都不能通过

4.确定遍历顺序



```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[m - 1][n - 1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 0:  # 遇到障碍物时，直接退出循环，后面默认都是0
                dp[i][0] = 1
            else:
                break
        for j in range(n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            else:
                break
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]
```



