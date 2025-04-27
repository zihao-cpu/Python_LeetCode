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







def knapsack(i, W, weight, value):
    # 递归的基本终止条件
    if i == 0 or W == 0:
        return 0
    
    # 如果当前物品的重量大于背包的容量，不能选择该物品
    if weight[i - 1] > W:
        return knapsack(i - 1, W, weight, value)
    else:
        # 比较选择当前物品和不选择当前物品的最大价值
        return max(knapsack(i - 1, W, weight, value),
                   value[i - 1] + knapsack(i - 1, W - weight[i - 1], weight, value))

# 示例：物品的重量和价值
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5  # 背包容量

# 计算最大价值
n = len(weights)
max_value = knapsack(n, capacity, weights, values)
print(f"最大价值: {max_value}")
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

# 整数拆分

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0343.%E6%95%B4%E6%95%B0%E6%8B%86%E5%88%86.md

1.确定dp数组以及下标的含义:

dp[i]：分拆数字i，可以得到的最大乘积为dp[i]。

2.确定递推公式：

其实可以从1遍历j，然后有两种渠道得到dp[i].

一个是j * (i - j) 直接相乘。

一个是j * dp[i - j]，相当于是拆分(i - j)，对这个拆分不理解的话，可以回想dp数组的定义。

**dp[i] = max(dp[i], max((i - j) * j, dp[i - j] * j));**

3.确定初始条件:

不少同学应该疑惑，dp[0] dp[1]应该初始化多少呢？

有的题解里会给出dp[0] = 1，dp[1] = 1的初始化，但解释比较牵强，主要还是因为这么初始化可以把题目过了。

严格从dp[i]的定义来说，dp[0] dp[1] 就不应该初始化，也就是没有意义的数值。

拆分0和拆分1的最大乘积是多少？

这是无解的。

这里我只初始化dp[2] = 1，从dp[i]的定义来说，拆分数字2，得到的最大乘积是1，这个没有任何异议！
4.确定遍历顺序：

dp[i] 是依靠 dp[i - j]的状态，所以遍历i一定是从前向后遍历，先有dp[i - j]再有dp[i]。



```python
class Solution:
         # 假设对正整数 i 拆分出的第一个正整数是 j（1 <= j < i），则有以下两种方案：
        # 1) 将 i 拆分成 j 和 i−j 的和，且 i−j 不再拆分成多个正整数，此时的乘积是 j * (i-j)
        # 2) 将 i 拆分成 j 和 i−j 的和，且 i−j 继续拆分成多个正整数，此时的乘积是 j * dp[i-j]
    def integerBreak(self, n):
        dp = [0] * (n + 1)   # 创建一个大小为n+1的数组来存储计算结果
        dp[2] = 1  # 初始化dp[2]为1，因为当n=2时，只有一个切割方式1+1=2，乘积为1
       
        # 从3开始计算，直到n
        for i in range(3, n + 1):
            # 遍历所有可能的切割点
            for j in range(1, i // 2 + 1):#这里是为什么  j<i-1 也可以只是会造成重复

                # 计算切割点j和剩余部分(i-j)的乘积，并与之前的结果进行比较取较大值
                
                dp[i] = max(dp[i], (i - j) * j, dp[i - j] * j)
        
        return dp[n]  # 返回最终的计算结果
```

# 01背包问题（滚动数组）

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/%E8%83%8C%E5%8C%85%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%8001%E8%83%8C%E5%8C%85-2.md

![img](https://camo.githubusercontent.com/e166e3b0e14b1304254d0426106aca0e4a143b4ee10bc08c60c43addc45ebd5d/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303234303733303131343232382e706e67)

**其实可以发现如果把dp[i - 1]那一层拷贝到dp[i]上，表达式完全可以是：$$dp[i][j] = max(dp[i][j], dp[i][j - weight[i]] + value[i]);$$**

**与其把dp[i - 1]这一层拷贝到dp[i]上，不如只用一个一维数组了**，只用dp[j]

递推公式为：dp[j] = max(dp[j], dp[j - weight[i]] + value[i]);

遍历顺序：第一层遍历物品；第二层倒序遍历背包（为了保证每个物品放入一次）。

**如果正序遍历**

**dp[1] = dp[1 - weight[0]] + value[0] = 15**

**dp[2] = dp[2 - weight[0]] + value[0] = 30**

**此时dp[2]就已经是30了，意味着物品0，被放入了两次，所以不能正序遍历。**

**为什么倒序遍历，就可以保证物品只放入一次呢？**

**倒序就是先算dp[2]**

**dp[2] = dp[2 - weight[0]] + value[0] = 15 （dp数组已经都初始化为0）**

**dp[1] = dp[1 - weight[0]] + value[0] = 15**

```python
n, bagweight = map(int, input().split())
weight = list(map(int, input().split()))
value = list(map(int, input().split()))

dp = [0] * (bagweight + 1)  # 创建一个动态规划数组dp，初始值为0

dp[0] = 0  # 初始化dp[0] = 0,背包容量为0，价值最大为0

for i in range(n):  # 应该先遍历物品，如果遍历背包容量放在上一层，那么每个dp[j]就只会放入一个物品
    for j in range(bagweight, weight[i]-1, -1):  # 倒序遍历背包容量是为了保证物品i只被放入一次
        dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

print(dp[bagweight])

#这里解释下 为什么第二层for循环 是这样的
#对于 j < weight[i] 的这些 j，j - weight[i] 是 负数，不合法！
for i in range(n):
    for j in range(bagweight + 1):
        if j >= weight[i]:
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])




```

# 分割等和子集

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0416.%E5%88%86%E5%89%B2%E7%AD%89%E5%92%8C%E5%AD%90%E9%9B%86.md

其实就是01背包问题

 **套到本题，dp[j]表示 背包总容量（所能装的总重量）是j，放进物品后，背的最大重量为dp[j]**。

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _sum = 0

        # dp[i]中的i表示背包内总和
        # 题目中说：每个数组中的元素不会超过 100，数组的大小不会超过 200
        # 总和不会大于20000，背包最大只需要其中一半，所以10001大小就可以了
        dp = [0] * 10001
        for num in nums:
            _sum += num
        # 也可以使用内置函数一步求和
        # _sum = sum(nums)
        if _sum % 2 == 1:
            return False
        target = _sum // 2

        # 开始 0-1背包
        for num in nums:
            for j in range(target, num - 1, -1):  # 每一个元素一定是不可重复放入，所以从大到小遍历
                dp[j] = max(dp[j], dp[j - num] + num)

        # 集合中的元素正好可以凑成总和target
        if dp[target] == target:
            return True
        return False
     
```

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        target_sum = total_sum // 2
        dp = [[False] * (target_sum + 1) for _ in range(len(nums) + 1)]

        # 初始化第一行（空子集可以得到和为0）
        for i in range(len(nums) + 1):
            dp[i][0] = True

        for i in range(1, len(nums) + 1):
            for j in range(1, target_sum + 1):
                if j < nums[i - 1]:
                    # 当前数字大于目标和时，无法使用该数字
                    dp[i][j] = dp[i - 1][j]
                else:
                    # 当前数字小于等于目标和时，可以选择使用或不使用该数字
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

        return dp[len(nums)][target_sum]
```

# 最后一块石头的重量2

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/1049.%E6%9C%80%E5%90%8E%E4%B8%80%E5%9D%97%E7%9F%B3%E5%A4%B4%E7%9A%84%E9%87%8D%E9%87%8FII.md

**本题其实就是尽量让石头分成重量相同的两堆，相撞之后剩下的石头最小，这样就化解成01背包问题了。**

本题物品的重量为stones[i]，物品的价值也为stones[i]。

**和上一题很像**



```python
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = [0] * 15001
        total_sum = sum(stones)
        target = total_sum // 2

        for stone in stones:  # 遍历物品
            for j in range(target, stone - 1, -1):  # 遍历背包
                dp[j] = max(dp[j], dp[j - stone] + stone)

        return total_sum - dp[target] - dp[target]
        
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        target = total_sum // 2
        
        # 创建二维dp数组，行数为石头的数量加1，列数为target加1
        # dp[i][j]表示前i个石头能否组成总重量为j
        dp = [[False] * (target + 1) for _ in range(len(stones) + 1)]
        
        # 初始化第一列，表示总重量为0时，前i个石头都能组成
        for i in range(len(stones) + 1):
            dp[i][0] = True
        
        for i in range(1, len(stones) + 1):
            for j in range(1, target + 1):
                # 如果当前石头重量大于当前目标重量j，则无法选择该石头
                if stones[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    # 可选择该石头或不选择该石头
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - stones[i - 1]]
        
        # 找到最大的重量i，使得dp[len(stones)][i]为True
        # 返回总重量减去两倍的最接近总重量一半的重量
        for i in range(target, -1, -1):
            if dp[len(stones)][i]:
                return total_sum - 2 * i
        
        return 0
    
    
    
    
#递归的版本    
from functools import lru_cache
from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        target = total_sum // 2

        @lru_cache(maxsize=None)
        def dfs(i, curr_sum):
            # 终止条件：没有石头了，返回当前累积的重量
            if i == len(stones):
                return curr_sum

            # 如果加上当前石头不会超过 target，可以选择加或不加
            take = 0
            if curr_sum + stones[i] <= target:
                take = dfs(i + 1, curr_sum + stones[i])
            not_take = dfs(i + 1, curr_sum)

            return max(take, not_take)

        closest = dfs(0, 0)
        return total_sum - 2 * closest
```

# 目标和

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0494.%E7%9B%AE%E6%A0%87%E5%92%8C.md

**既然为target，那么就一定有 left组合 - right组合 = target。**

**left + right = sum，而sum是固定的。right = sum - left**

**left - (sum - left) = target 推导出 left = (target + sum)/2 。**

**target是固定的，sum是固定的，left就可以求出来。**

**此时问题就是在集合nums中找出和为left的组合。**



**这次和之前遇到的背包问题不一样了，之前都是求容量为j的背包，最多能装多少。**

**本题则是装满有几种方法。其实这就是一个组合问题了。**

**1.只考虑物品0：**



![img](https://camo.githubusercontent.com/e18f43bfc14625ddd12d59fb7eb069bd4d8e5bb9882120f0f0a7a214bc896faa/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303234303830383136313734372e706e67)

**2.考虑物品0和物品1：**

![img](https://camo.githubusercontent.com/9039c929049fb4f64a97ccb9a38f5ad65a2ea7cbb5034aea2d78b6df8ad5250b/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303234303830383136323035322e706e67)

装满背包容量为0 的方法个数是1，即 放0件物品。

装满背包容量为1 的方法个数是2，即 放物品0 或者 放物品1。

装满背包容量为2 的方法个数是1，即 放物品0 和 放物品1。

其他容量都不能装满，所以方法是0。

**3.考虑物品0,1,2：**

![img](https://camo.githubusercontent.com/df358e582a9ac9cafe226ca772857b04b095c65439ca6a71dca530e037a36b65/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303234303830383136323533332e706e67)

装满背包容量为0 的方法个数是1，即 放0件物品。

装满背包容量为1 的方法个数是3，即 放物品0 或者 放物品1 或者 放物品2。

装满背包容量为2 的方法个数是3，即 放物品0 和 放物品1、放物品0 和 物品2、放物品1 和 物品2。

装满背包容量为3的方法个数是1，即 放物品0 和 物品1 和 物品2。

- **不放物品i**：即背包容量为j，里面不放物品i，装满有$$dp[i - 1][j]$$中方法。

- **不放物品i**：即：先空出物品i的容量，背包容量为（j - 物品i容量），放满背包有 dp[i - 1][j - 物品i容量] 种方法。

  ![img](https://camo.githubusercontent.com/d236c73885b6f30f83913f7c34c8355bf39c20dbc8436d05abbe41643914363c/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303234303832363131353830302e706e67)

  ​

  ```python
  class Solution:
      def findTargetSumWays(self, nums: List[int], target: int) -> int:
          total_sum = sum(nums)  # 计算nums的总和
          if abs(target) > total_sum:
              return 0  # 此时没有方案
          if (target + total_sum) % 2 == 1:
              return 0  # 此时没有方案
          target_sum = (target + total_sum) // 2  # 目标和

          # 创建二维动态规划数组，行表示选取的元素数量，列表示累加和
          dp = [[0] * (target_sum + 1) for _ in range(len(nums) + 1)]

          # 初始化状态
          dp[0][0] = 1

          # 动态规划过程
          for i in range(1, len(nums) + 1):
              for j in range(target_sum + 1):
                  dp[i][j] = dp[i - 1][j]  # 不选取当前元素
                  if j >= nums[i - 1]:
                      dp[i][j] += dp[i - 1][j - nums[i - 1]]  # 选取当前元素

          return dp[len(nums)][target_sum]  # 返回达到目标和的方案数
  ```

  ​


# 一和零

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0474.%E4%B8%80%E5%92%8C%E9%9B%B6.md

**这里本来是三维的dp 只不过 这里变成二维 ：类似于 经典01问题变成一维滚动数组**

1.确定dp数组以及下标的含义：

$$dp[i][j]$$：最多有i个0和j个1的strs的最大子集的大小为$$dp[i][j]$$。

2.确定递推公式：

$$dp[i][j] 可以由前一个strs里的字符串推导出来，strs里的字符串有zeroNum个0，oneNum个1。$$

$$dp[i][j] 就可以是 dp[i - zeroNum][j - oneNum] + 1。$$

然后我们在遍历的过程中，取$$dp[i][j]$$的最大值。

所以递推公式：$$dp[i][j] = max(dp[i][j], dp[i - zeroNum][j - oneNum] + 1)$$;

此时大家可以回想一下01背包的递推公式：dp[j] = max(dp[j], dp[j - weight[i]] + value[i]);

对比一下就会发现，字符串的zeroNum和oneNum相当于物品的重量（weight[i]），字符串本身的个数相当于物品的价值（value[i]）。

**这就是一个典型的01背包！** 只不过物品的重量有了两个维度而已。

3.一定是外层for循环遍历物品，内层for循环遍历背包容量且从后向前遍历！

```python
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # 创建二维动态规划数组，初始化为0
        # 遍历物品
        for s in strs:
            ones = s.count('1')  # 统计字符串中1的个数
            zeros = s.count('0')  # 统计字符串中0的个数
            # 遍历背包容量且从后向前遍历
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)  # 状态转移方程
        return dp[m][n]
      
      
      
from functools import lru_cache

def findMaxForm(strs, m, n):
    # 预处理每个字符串中0和1的数量
    counts = []
    for s in strs:
        zeros = s.count('0')
        ones = s.count('1')
        counts.append((zeros, ones))

    @lru_cache(maxsize=None)
    def dfs(index, zeros_left, ones_left):
        # 递归终止条件：字符串用完了或容量用尽
        if index == len(strs):
            return 0

        z, o = counts[index]

        # 不选当前字符串
        not_pick = dfs(index + 1, zeros_left, ones_left)

        # 选当前字符串（前提是容量足够）
        pick = 0
        if zeros_left >= z and ones_left >= o:
            pick = 1 + dfs(index + 1, zeros_left - z, ones_left - o)

        return max(pick, not_pick)

    return dfs(0, m, n)
```

# 完全背包

普通0 1 背包问题的变体

```python
def complete_knapsack_2d(weight, value, bagweight):
    n = len(weight)
    dp = [[0] * (bagweight + 1) for _ in range(n)]

    # 初始化第一行（第0号物品可以选多次）
    for j in range(weight[0], bagweight + 1):
        # 完全背包，物品可重复
        dp[0][j] = (j // weight[0]) * value[0]

    for i in range(1, n):  # 遍历物品
        for j in range(bagweight + 1):  # 遍历容量
            if j < weight[i]:
                dp[i][j] = dp[i - 1][j]  # 不选当前物品
            else:
                # 完全背包：当前物品可以重复使用，所以用的是 dp[i][j - weight[i]]
                dp[i][j] = max(
                    dp[i - 1][j],                # 不选当前物品
                    dp[i][j - weight[i]] + value[i]  # 选当前物品（可重复）
                )

    return dp[n - 1][bagweight]
  
  
  

def complete_knapsack(weight, value, bagweight):
    n = len(weight)
    dp = [0] * (bagweight + 1)

    for i in range(n):  # 遍历每一个物品
        for j in range(weight[i], bagweight + 1):  # 从前往后遍历容量（允许重复使用）
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

    return dp[bagweight]
```

**注意 和 普通版的不同：**

| 对比点      | 0-1 背包（二维）                               | 完全背包（二维）                                 |
| -------- | ---------------------------------------- | :--------------------------------------- |
| 可否重复选择物品 | ❌ 不能重复使用                                 | ✅ 可以重复使用                                 |
| 状态转移公式   | $$ dp[i][j] = \max(dp[i-1][j],\ dp[i-1][j-w_i] + v_i) $$ | $$ dp[i][j] = \max(dp[i-1][j],\ dp[i][j-w_i] + v_i) $$ |
| 状态转移依赖的行 | 依赖上一行 `i-1`（每个物品最多选一次）                   | 依赖当前行 `i`（当前物品可重复使用）                     |
| 初始化第一行   | $$ dp[0][j] = v_0 \quad \text{(当 } j \geq w_0 \text{时)} $$ | $$ dp[0][j] = \left\lfloor \frac{j}{w_0} \right\rfloor \cdot v_0 $$ |

# 组合总和

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0377.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8C%E2%85%A3.md

完全背包

**如果求组合数就是外层for循环遍历物品，内层for遍历背包**。

**如果求排列数就是外层for遍历背包，内层for循环遍历物品**。

```python 
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)  # 创建动态规划数组，用于存储组合总数
        dp[0] = 1  # 初始化背包容量为0时的组合总数为1

        for i in range(1, target + 1):  # 遍历背包容量
            for j in nums:  # 遍历物品列表
                if i >= j:  # 当背包容量大于等于当前物品重量时
                    dp[i] += dp[i - j]  # 更新组合总数

        return dp[-1]  # 返回背包容量为target时的组合总数
```









# 完全平方数

```python
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, int(n ** 0.5) + 1):  # 遍历物品
            for j in range(i * i, n + 1):  # 遍历背包
                # 更新凑成数字 j 所需的最少完全平方数数量
                dp[j] = min(dp[j - i * i] + 1, dp[j])

        return dp[n]
        
        
class Solution:
    def numSquares(self, n: int) -> int:
        # 生成完全平方数列表
        squares = [i * i for i in range(1, int(n ** 0.5) + 1)]
        
        # 初始化二维 DP 数组，dp[i][j] 表示使用前 i 个完全平方数来凑成 j 的最小完全平方数数量
        dp = [[float('inf')] * (n + 1) for _ in range(len(squares) + 1)]
        
        # 初始化基准情况：dp[i][0] = 0，表示凑成 0 需要 0 个完全平方数
        for i in range(len(squares) + 1):
            dp[i][0] = 0
        
        # 填充 DP 表
        for i in range(1, len(squares) + 1):
            for target in range(1, n + 1):
                # 不选择当前完全平方数
                dp[i][target] = dp[i - 1][target]
                # 选择当前完全平方数
                if target >= squares[i - 1]:
                    dp[i][target] = min(dp[i][target], dp[i][target - squares[i - 1]] + 1)
        
        return dp[len(squares)][n]


        
class Solution:
    def numSquares(self, n: int) -> int:
        # 生成完全平方数列表
        squares = [i * i for i in range(1, int(n ** 0.5) + 1)]
        
        # 递归函数，求解最小的完全平方数数量
        def helper(target):
            if target == 0:
                return 0
            min_count = float('inf')
            for square in squares:
                if target >= square:
                    min_count = min(min_count, helper(target - square) + 1)
            return min_count
        
        return helper(n)

```
# 单词拆分

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0139.%E5%8D%95%E8%AF%8D%E6%8B%86%E5%88%86.md

单词就是物品，字符串s就是背包，单词能否组成字符串s，就是问物品能不能把背包装满。

拆分时可以重复使用字典中的单词，说明就是一个完全背包！

1.确定dp数组和下标的意义：

**dp[i] : 字符串长度为i的话，dp[i]为true，表示可以拆分为一个或多个在字典中出现的单词**。

2.确认递归函数：

如果确定dp[j] 是true，且 [j, i] 这个区间的子串出现在字典里，那么dp[i]一定是true。（j < i ）。

所以递推公式是 if([j, i] 这个区间的子串出现在字典里 && dp[j]是true) 那么 dp[i] = true。

3.初始化

4.确定遍历顺序

**如果求组合数就是外层for循环遍历物品，内层for遍历背包**。

**如果求排列数就是外层for遍历背包，内层for循环遍历物品**。



```python
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = [[False] * (n + 1) for _ in range(n + 1)]  # dp[i][j] 表示 s[j:i] 可被拼出（注意：i > j）

        for i in range(1, n + 1):  # i 表示右边界
            for j in range(i):    # j 表示左边界
                if s[j:i] in wordSet:
                    if j == 0 or any(dp[j][k] for k in range(j)):
                        dp[i][j] = True

        # 检查是否存在一个 j，使得 dp[n][j] == True 并且前面的部分都可拼出
        return any(dp[n][j] and (j == 0 or any(dp[j][k] for k in range(j))) for j in range(n))


      
      class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)  # dp[i] 表示字符串的前 i 个字符是否可以被拆分成单词
        dp[0] = True  # 初始状态，空字符串可以被拆分成单词

        for i in range(1, n + 1): # 遍历背包
            for j in range(i): # 遍历单词
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True  # 如果 s[0:j] 可以被拆分成单词，并且 s[j:i] 在单词集合中存在，则 s[0:i] 可以被拆分成单词
                    break     
    
    
    
    
```
# 打家劫舍

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0198.%E6%89%93%E5%AE%B6%E5%8A%AB%E8%88%8D.md

1.确定dp数组和下标含义

**dp[i]：考虑下标i（包括i）以内的房屋，最多可以偷窃的金额为dp[i]**。

2.确定递推公式：

如果偷第i房间，那么dp[i] = dp[i - 2] + nums[i] ，即：第i-1房一定是不考虑的，找出 下标i-2（包括i-2）以内的房屋，最多可以偷窃的金额为dp[i-2] 加上第i房间偷到的钱。

如果不偷第i房间，那么dp[i] = dp[i - 1]，即考 虑i-1房，（**注意这里是考虑，并不是一定要偷i-1房，这是很多同学容易混淆的点**）

  **$$dp[i][0] = max(dp[i-1][0], dp[i-1][1])$$  # 不抢劫第i个房屋，最大金额为前一个房屋抢劫和不抢劫的最大值** **注意这里！！！**



然后dp[i]取最大值，即dp[i] = max(dp[i - 2] + nums[i], dp[i - 1]);

3.初始化:

从dp[i]的定义上来讲，dp[0] 一定是 nums[0]，dp[1]就是nums[0]和nums[1]的最大值即：dp[1] = max(nums[0], nums[1]);



```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:  # 如果没有房屋，返回0
            return 0
        if len(nums) == 1:  # 如果只有一个房屋，返回其金额
            return nums[0]

        # 创建一个动态规划数组，用于存储最大金额
        dp = [0] * len(nums)
        dp[0] = nums[0]  # 将dp的第一个元素设置为第一个房屋的金额
        dp[1] = max(nums[0], nums[1])  # 将dp的第二个元素设置为第一二个房屋中的金额较大者

        # 遍历剩余的房屋
        for i in range(2, len(nums)):
            # 对于每个房屋，选择抢劫当前房屋和抢劫前一个房屋的最大金额
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]  # 返回最后一个房屋中可抢劫的最大金额
        
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:  # 如果没有房屋，返回0
            return 0

        n = len(nums)
        dp = [[0, 0] for _ in range(n)]  # 创建二维动态规划数组，dp[i][0]表示不抢劫第i个房屋的最大金额，dp[i][1]表示抢劫第i个房屋的最大金额

        dp[0][1] = nums[0]  # 抢劫第一个房屋的最大金额为第一个房屋的金额

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])  # 不抢劫第i个房屋，最大金额为前一个房屋抢劫和不抢劫的最大值
            dp[i][1] = dp[i-1][0] + nums[i]  # 抢劫第i个房屋，最大金额为前一个房屋不抢劫的最大金额加上当前房屋的金额

        return max(dp[n-1][0], dp[n-1][1])  # 返回最后一个房屋中可抢劫的最大金额        
        
```

# 打家劫舍2

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0213.%E6%89%93%E5%AE%B6%E5%8A%AB%E8%88%8DII.md

- 情况一：考虑不包含首尾元素

  ![213.打家劫舍II](https://camo.githubusercontent.com/7f391db0697aa01735429b2320c860ae36bf63ab2ea51794a28c077d995f5de8/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303231303132393136303734383634332d32303233303331303133343030303639322e6a7067)

- 情况二：考虑包含首元素，不包含尾元素

  ​

- 情况三：考虑包含尾元素，不包含首元素

![213.打家劫舍II2](https://camo.githubusercontent.com/07a36fda6455d107eb2dd352d0e38989f386959d12f010f81764e1ff36207db9/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303231303132393136303834323439312d32303233303331303133343030383133332e6a7067)

**情况2、3 包含了 情况1**

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        result1 = self.robRange(nums, 0, len(nums) - 2)  # 情况二
        result2 = self.robRange(nums, 1, len(nums) - 1)  # 情况三
        return max(result1, result2)
    # 198.打家劫舍的逻辑
    def robRange(self, nums: List[int], start: int, end: int) -> int:
        if end == start:
            return nums[start]
        
        prev_max = nums[start]
        curr_max = max(nums[start], nums[start + 1])
        
        for i in range(start + 2, end + 1):
            temp = curr_max
            curr_max = max(prev_max + nums[i], curr_max)
            prev_max = temp
        
        return curr_max
        
  class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        # 情况二：不抢劫第一个房屋
        result1 = self.robRange(nums[:-1])

        # 情况三：不抢劫最后一个房屋
        result2 = self.robRange(nums[1:])

        return max(result1, result2)

    def robRange(self, nums):
        dp = [[0, 0] for _ in range(len(nums))]
        dp[0][1] = nums[0]

        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i - 1])
            dp[i][1] = dp[i - 1][0] + nums[i]

        return max(dp[-1])
      
  
```

# 打家劫舍3

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0337.%E6%89%93%E5%AE%B6%E5%8A%AB%E8%88%8DIII.md

**暴力递归的方法**



```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right  is None:
            return root.val
        # 偷父节点
        val1 = root.val
        if root.left:
            val1 += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            val1 += self.rob(root.right.left) + self.rob(root.right.right)
        # 不偷父节点
        val2 = self.rob(root.left) + self.rob(root.right)
        return max(val1, val2)
```

**记忆化递归**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    memory = {}
    def rob(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right  is None:
            return root.val
        if self.memory.get(root) is not None:
            return self.memory[root]
        # 偷父节点
        val1 = root.val
        if root.left:
            val1 += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            val1 += self.rob(root.right.left) + self.rob(root.right.right)
        # 不偷父节点
        val2 = self.rob(root.left) + self.rob(root.right)
        self.memory[root] = max(val1, val2)
        return max(val1, val2)
```

**树形dp**

而动态规划其实就是使用状态转移容器来记录状态的变化，这里可以使用一个长度为2的数组，记录当前节点偷与不偷所得到的的最大金钱。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # dp数组（dp table）以及下标的含义：
        # 1. 下标为 0 记录 **不偷该节点** 所得到的的最大金钱
        # 2. 下标为 1 记录 **偷该节点** 所得到的的最大金钱
        dp = self.traversal(root)
        return max(dp)

    # 要用后序遍历, 因为要通过递归函数的返回值来做下一步计算
    def traversal(self, node):
        
        # 递归终止条件，就是遇到了空节点，那肯定是不偷的
        if not node:
            return (0, 0)

        left = self.traversal(node.left)
        right = self.traversal(node.right)

        # 不偷当前节点, 偷子节点
        val_0 = max(left[0], left[1]) + max(right[0], right[1])

        # 偷当前节点, 不偷子节点
        val_1 = node.val + left[0] + right[0]

        return (val_0, val_1)
```

# 买卖股票的最佳时机(交易一次)

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0121.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BA.md

$$dp[i][0]$$ 表示第i天持有股票所得最多现金 

$$dp[i][1]$$ 表示第i天不持有股票所得最多现金

2.确定递推公式

2.1如果第i天持有股票$$dp[i][0]$$， 那么可以由两个状态推出来:



- 第i-1天就持有股票，那么就保持现状，所得现金就是昨天持有股票的所得现金 即：$$dp[i - 1][0]$$
- 第i天买入股票，所得现金就是买入今天的股票后所得现金即：-prices[i]

**这里可能有同学疑惑，本题中只能买卖一次，持有股票之后哪还有现金呢？**

其实一开始现金是0，那么加入第i天买入股票现金就是 -prices[i]， 这是一个负数。

那么$$dp[i][0]$$应该选所得现金最大的，所以$$dp[i][0] = max(dp[i - 1][0], -prices[i]);$$



2.2如果第i天不持有股票即$$dp[i][1]$$， 也可以由两个状态推出来:

- 第i-1天就不持有股票，那么就保持现状，所得现金就是昨天不持有股票的所得现金 即：$$dp[i - 1][1]$$
- 第i天卖出股票，所得现金就是按照今天股票价格卖出后所得现金即：$$prices[i] + dp[i - 1][0]$$

同样$$dp[i][1]$$取最大的，$$dp[i][1] = max(dp[i - 1][1], prices[i] + dp[i - 1][0]);$$

3.初始化：

由递推公式 $$dp[i][0] = max(dp[i - 1][0], -prices[i]); 和 dp[i][1] = max(dp[i - 1][1], prices[i] + dp[i - 1][0]);$$可以看出

其基础都是要从$$dp[0][0]$$和$$dp[0][1]$$推导出来。

那么$$dp[0][0]$$表示第0天持有股票，此时的持有股票就一定是买入股票了，因为不可能有前一天推出来，所以$$dp[0][0] = -prices[0];$$

$$dp[0][1]$$表示第0天不持有股票，不持有股票那么现金就是0，所以$$dp[0][1] = 0;$$

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        dp0, dp1 = -prices[0], 0 #注意这里只维护两个常量，因为dp0的更新不受dp1的影响
        for i in range(1, length):
            dp1 = max(dp1, dp0 + prices[i])
            dp0 = max(dp0, -prices[i])
        return dp1
```

# 买卖股票的最佳时机2(交易多次)

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0122.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BAII%EF%BC%88%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%EF%BC%89.md

如果第i天持有股票即$$dp[i][0]$$， 那么可以由两个状态推出来

- 第i-1天就持有股票，那么就保持现状，所得现金就是昨天持有股票的所得现金 即：$$dp[i - 1][0]$$
- 第i天买入股票，所得现金就是昨天不持有股票的所得现金减去 今天的股票价格 即：$$dp[i - 1][1] - prices[i]$$

如果第i天不持有股票即dp[i][1]的情况， 依然可以由两个状态推出来

- 第i-1天就不持有股票，那么就保持现状，所得现金就是昨天不持有股票的所得现金 即：$$dp[i - 1][1]$$
- 第i天卖出股票，所得现金就是按照今天股票价格卖出后所得现金即：$$prices[i] + dp[i - 1][0]$$

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        dp0, dp1 = -prices[0], 0 #注意这里只维护两个常量，因为dp0的更新不受dp1的影响
        for i in range(1, length):
            dp1 = max(dp1, dp0 + prices[i])
            dp0 = max(dp0, dp1-prices[i])
        return dp1
```

# 买卖股票的最佳时机3(最多两次)

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0123.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BAIII.md

1.定义dp数组含义：

0.没有操作 （其实我们也可以不设置这个状态）

1.第一次持有股票

2.第一次不持有股票

3.第二次持有股票

4.第二次不持有股票

$$dp[i][j]$$中 i表示第i天，j为 [0 - 4] 五个状态，$$dp[i][j]$$表示第i天状态j所剩最大现金。

2.1达到$$dp[i][1]$$状态，有两个具体操作：

- 操作一：第i天买入股票了，那么$$dp[i][1] = dp[i-1][0] - prices[i]$$
- 操作二：第i天没有操作，而是沿用前一天买入的状态，即：$$dp[i][1] = dp[i - 1][1]$$

$$dp[i][1] = max(dp[i-1][0] - prices[i], dp[i - 1][1]);$$

2.2同理$$dp[i][2]$$也有两个操作

- 操作一：第i天卖出股票了，那么$$dp[i][2] = dp[i - 1][1] + prices[i]$$
- 操作二：第i天没有操作，沿用前一天卖出股票的状态，即：$$dp[i][2] = dp[i - 1][2]$$

$$dp[i][2] = max(dp[i - 1][1] + prices[i], dp[i - 1][2])$$

2.3递推

$$dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i]);$$

$$dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i]);$$

3.初始化

第0天没有操作，这个最容易想到，就是0，即：$$dp[0][0] = 0;$$

第0天做第一次买入的操作，$$dp[0][1] = -prices[0];$$

此时还没有买入，怎么就卖出呢？ 其实大家可以理解当天买入，当天卖出，所以$$dp[0][2] = 0;$$

所以第二次买入操作，初始化为：$$dp[0][3] = -prices[0];$$

同理第二次卖出初始化$$dp[0][4] = 0;$$

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        dp = [[0] * 5 for _ in range(len(prices))]
        dp[0][1] = -prices[0]
        dp[0][3] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = dp[i-1][0]
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
            dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i])
        return dp[-1][4]
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        dp = [0] * 5 
        dp[1] = -prices[0]
        dp[3] = -prices[0]
        for i in range(1, len(prices)):
            dp[1] = max(dp[1], dp[0] - prices[i])
            dp[2] = max(dp[2], dp[1] + prices[i])
            dp[3] = max(dp[3], dp[2] - prices[i])
            dp[4] = max(dp[4], dp[3] + prices[i])
        return dp[4]        
        
        
```
# 买卖股票的最佳时机4(交易k次)

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0188.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BAIV.md

```python
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        dp = [[0] * (2*k+1) for _ in range(len(prices))]
        for j in range(1, 2*k, 2):
            dp[0][j] = -prices[0]
        for i in range(1, len(prices)):
            for j in range(0, 2*k-1, 2):
                dp[i][j+1] = max(dp[i-1][j+1], dp[i-1][j] - prices[i])
                dp[i][j+2] = max(dp[i-1][j+2], dp[i-1][j+1] + prices[i])
        return dp[-1][2*k]
      
      
     
```

# 最佳买卖股票时机含冷冻期

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0309.%E6%9C%80%E4%BD%B3%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E6%97%B6%E6%9C%BA%E5%90%AB%E5%86%B7%E5%86%BB%E6%9C%9F.md

状态一：持有股票状态（今天买入股票，或者是之前就买入了股票然后没有操作，一直持有）

状态二：保持卖出股票的状态（两天前就卖出了股票，度过一天冷冻期。或者是前一天就是卖出股票状态，一直没操作），没有股票

状态三：今天卖出股票，没有股票

状态四：冷冻期

1.确定递推公式：

**达到买入股票状态**（状态一）即：$$dp[i][0]$$，有两个具体操作：

- 操作一：前一天就是持有股票状态（状态一），$$dp[i][0] = dp[i - 1][0]$$
- 操作二：今天买入了，有两种情况
  - 前一天是冷冻期（状态四），$$dp[i - 1][3] - prices[i]$$
  - 前一天是保持卖出股票的状态（状态二），$$dp[i - 1][1] - prices[i]$$

那么$$dp[i][0] = max(dp[i - 1][0], dp[i - 1][3] - prices[i], dp[i - 1][1] - prices[i]);$$

**达到保持卖出股票状态**（状态二）即：dp[i][1]，有两个具体操作：

- 操作一：前一天就是状态二
- 操作二：前一天是冷冻期（状态四）

$$dp[i][1] = max(dp[i - 1][1], dp[i - 1][3]);$$

**达到今天就卖出股票状态**（状态三），即：$$dp[i][2]$$ ，只有一个操作：

昨天一定是持有股票状态（状态一），今天卖出

即：$$dp[i][2] = dp[i - 1][0] + prices[i];$$

**达到冷冻期状态**（状态四），即：$$dp[i][3]$$，只有一个操作：

昨天卖出了股票（状态三）

$$dp[i][3] = dp[i - 1][2];$$

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dp = [[0] * 4 for _ in range(n)]  # 创建动态规划数组，4个状态分别表示持有股票、不持有股票且处于冷冻期、不持有股票且不处于冷冻期、不持有股票且当天卖出后处于冷冻期
        dp[0][0] = -prices[0]  # 初始状态：第一天持有股票的最大利润为买入股票的价格
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], max(dp[i-1][3], dp[i-1][1]) - prices[i])  # 当前持有股票的最大利润等于前一天持有股票的最大利润或者前一天不持有股票且不处于冷冻期的最大利润减去当前股票的价格
            dp[i][1] = max(dp[i-1][1], dp[i-1][3])  # 当前不持有股票且处于冷冻期的最大利润等于前一天持有股票的最大利润加上当前股票的价格
            dp[i][2] = dp[i-1][0] + prices[i]  # 当前不持有股票且不处于冷冻期的最大利润等于前一天不持有股票的最大利润或者前一天处于冷冻期的最大利润
            dp[i][3] = dp[i-1][2]  # 当前不持有股票且当天卖出后处于冷冻期的最大利润等于前一天不持有股票且不处于冷冻期的最大利润
        return max(dp[n-1][3], dp[n-1][1], dp[n-1][2])  # 返回最后一天不持有股票的最大利润

```

# 买卖股票的最佳时机含手续费

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0714.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BA%E5%90%AB%E6%89%8B%E7%BB%AD%E8%B4%B9%EF%BC%88%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%EF%BC%89.md

在**买卖股票的最佳时机2**基础上 修改

```python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = -prices[0] #持股票
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i] - fee)
        return max(dp[-1][0], dp[-1][1])
```

# 最长上升子序列

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0300.%E6%9C%80%E9%95%BF%E4%B8%8A%E5%8D%87%E5%AD%90%E5%BA%8F%E5%88%97.md

1.dp的定义:

**dp[i]表示i之前包括i的以nums[i]结尾的最长递增子序列的长度**

2.状态转移方程：

位置i的最长升序子序列等于j从0到i-1各个位置的最长升序子序列 + 1 的最大值。

所以：if (nums[i] > nums[j]) dp[i] = max(dp[i], dp[j] + 1);

3.初始化:

一个i，对应的dp[i]（即最长递增子序列）起始大小至少都是1.

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        dp = [1] * len(nums)
        result = 1
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            result = max(result, dp[i]) #取长的子序列
        return result
```

# 最长连续递增序列

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0674.%E6%9C%80%E9%95%BF%E8%BF%9E%E7%BB%AD%E9%80%92%E5%A2%9E%E5%BA%8F%E5%88%97.md

1.dp的定义:

**dp[i]表示i之前包括i的以nums[i]结尾的最长连续递增子序列的长度**

2.状态转移方程：

如果 nums[i] > nums[i - 1]，那么以 i 为结尾的连续递增的子序列长度 一定等于 以i - 1为结尾的连续递增的子序列长度 + 1 。

dp[i] = dp[i - 1] + 1;

3.初始化：

以下标i为结尾的连续递增的子序列长度最少也应该是1，即就是nums[i]这一个元素。

所以dp[i]应该初始1;

```python
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        result = 1
        dp = [1] * len(nums)
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]: #连续记录
                dp[i+1] = dp[i] + 1
            result = max(result, dp[i+1])
        return result
```
# 最长重复子数组

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0718.%E6%9C%80%E9%95%BF%E9%87%8D%E5%A4%8D%E5%AD%90%E6%95%B0%E7%BB%84.md

- A: [1,2,3,2,1]
- B: [3,2,1,4,7]
- 输出：3
- 解释：长度最长的公共子数组是 [3, 2, 1] 。

1.确定dp数组

$$dp[i][j]$$ ：以下标i - 1为结尾的A，和以下标j - 1为结尾的B，最长重复子数组长度为$$dp[i][j]$$。

2.确定递推公式

根据$$dp[i][j]$$的定义，$$dp[i][j$$的状态只能由$$dp[i - 1][j - 1]$$推导出来。

即当A[i - 1] 和B[j - 1]相等的时候，$$dp[i][j] = dp[i - 1][j - 1] + 1$$;

根据递推公式可以看出，遍历i 和 j 要从1开始！

3.初始化

所以dp[i][0] 和dp[0][j]初始化为0。

```python
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # 创建一个二维数组 dp，用于存储最长公共子数组的长度
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        # 记录最长公共子数组的长度
        result = 0

        # 遍历数组 nums1
        for i in range(1, len(nums1) + 1):
            # 遍历数组 nums2
            for j in range(1, len(nums2) + 1):
                # 如果 nums1[i-1] 和 nums2[j-1] 相等
                if nums1[i - 1] == nums2[j - 1]:
                    # 在当前位置上的最长公共子数组长度为前一个位置上的长度加一
                    dp[i][j] = dp[i - 1][j - 1] + 1
                # 更新最长公共子数组的长度
                if dp[i][j] > result:
                    result = dp[i][j]

        # 返回最长公共子数组的长度
        return result
```

# 最长公共子序列

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/1143.%E6%9C%80%E9%95%BF%E5%85%AC%E5%85%B1%E5%AD%90%E5%BA%8F%E5%88%97.md

- 输入：text1 = "abcde", text2 = "ace"
- 输出：3
- 解释：最长公共子序列是 "ace"，它的长度为 3。

1.确定含义 ：

$$dp[i][j]$$：长度为[0, i - 1]的字符串text1与长度为[0, j - 1]的字符串text2的最长公共子序列为$$dp[i][j]$$

2.确定递推公式 ：

如果text1[i - 1] 与 text2[j - 1]相同，那么找到了一个公共元素，所以$$dp[i][j] = dp[i - 1][j - 1] + 1$$;

如果text1[i - 1] 与 text2[j - 1]不相同，那就看看text1[0, i - 2]与text2[0, j - 1]的最长公共子序列 和 text1[0, i - 1]与text2[0, j - 2]的最长公共子序列，取最大的。即：$$dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])$$;

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 创建一个二维数组 dp，用于存储最长公共子序列的长度
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        
        # 遍历 text1 和 text2，填充 dp 数组
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    # 如果 text1[i-1] 和 text2[j-1] 相等，则当前位置的最长公共子序列长度为左上角位置的值加一
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # 如果 text1[i-1] 和 text2[j-1] 不相等，则当前位置的最长公共子序列长度为上方或左方的较大值
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # 返回最长公共子序列的长度
        return dp[len(text1)][len(text2)]
```

# 不相交的线

解法同上一题



# 最大子序和

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0053.%E6%9C%80%E5%A4%A7%E5%AD%90%E5%BA%8F%E5%92%8C.md

贪心的做法:

局部最优：当前“连续和”为负数的时候立刻放弃，从下一个元素重新计算“连续和”，因为负数加上下一个元素 “连续和”只会越来越小。**遍历 nums，从头开始用 count 累积，如果 count 一旦加上 nums[i]变为负数，那么就应该从 nums[i+1]开始从 0 累积 count 了，因为已经变为负数的 count，只会拖累总和。**

```python
def maxSubArray(self, nums):
    result = float('-inf')  # 初始化结果为负无穷大
    count = 0
    for i in range(len(nums)):
        count += nums[i]
        if count > result:  # 取区间累计的最大值（相当于不断确定最大子序终止位置）
            result = count
        if count <= 0:  # 相当于重置最大子序起始位置，因为遇到负数一定是拉低总和
            count = 0
    return result
```
1.确定dp 含义：

**dp[i]：包括下标i（以nums[i]为结尾）的最大连续子序列和为dp[i]**。

2.递推公式：

dp[i]只有两个方向可以推出来：

- dp[i - 1] + nums[i]，即：nums[i]加入当前连续子序列和
- nums[i]，即：从头开始计算当前连续子序列和
- 一定是取最大的，所以dp[i] = max(dp[i - 1] + nums[i], nums[i]);

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        result = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i]) #状态转移公式
            result = max(result, dp[i]) #result 保存dp[i]的最大值
        return result
      
      
  #递归的写法
  class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        from functools import lru_cache

        n = len(nums)

        @lru_cache(maxsize=None)  # 记忆化递归
        def helper(i):
            if i == 0:
                return nums[0]
            return max(helper(i - 1) + nums[i], nums[i])

        # 扫描所有 i，找出最大值
        return max(helper(i) for i in range(n))
    
```

# 判断子序列

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0392.%E5%88%A4%E6%96%AD%E5%AD%90%E5%BA%8F%E5%88%97.md

1.确定dp 的含义

**$$dp[i][j]$$ 表示以下标i-1为结尾的字符串s，和以下标j-1为结尾的字符串t，相同子序列的长度为$$dp[i][j]$$**。

2.确定递推公式

在确定递推公式的时候，首先要考虑如下两种操作，整理如下：

- if (s[i - 1] == t[j - 1])
  - t中找到了一个字符在s中也出现了
- if (s[i - 1] != t[j - 1])
  - 相当于t要删除元素，继续匹配

if (s[i - 1] == t[j - 1])，那么$$dp[i][j] = dp[i - 1][j - 1] + 1$$;，因为找到了一个相同的字符，相同子序列长度自然要在$$dp[i-1][j-1]$$的基础上加1（**如果不理解，在回看一下$$dp[i][j]$$的定义**）

if (s[i - 1] != t[j - 1])，此时相当于t要删除元素，t如果把当前元素t[j - 1]删除，那么$$dp[i][j]$$ 的数值就是 看s[i - 1]与 t[j - 2]的比较结果了，即：$$dp[i][j] = dp[i][j - 1]$$;

其实这里 大家可以发现和 [1143.最长公共子序列](https://programmercarl.com/1143.%E6%9C%80%E9%95%BF%E5%85%AC%E5%85%B1%E5%AD%90%E5%BA%8F%E5%88%97.html) 的递推公式基本那就是一样的，区别就是 本题 如果删元素一定是字符串t，而 1143.最长公共子序列 是两个字符串都可以删元素。

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dp = [[0] * (len(t)+1) for _ in range(len(s)+1)]
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i][j-1]
        if dp[-1][-1] == len(s):
            return True
        return False
```

# 不同的子序列

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0115.%E4%B8%8D%E5%90%8C%E7%9A%84%E5%AD%90%E5%BA%8F%E5%88%97.md

1.dp数组 

$$dp[i][j]$$：以i-1为结尾的s子序列中出现以j-1为结尾的t的个数为$$dp[i][j]$$。

2.确定递推公式

- s[i - 1] 与 t[j - 1]相等
- s[i - 1] 与 t[j - 1] 不相等

所以当s[i - 1] 与 t[j - 1]相等时，$$dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]$$;

当s[i - 1] 与 t[j - 1]相等时，$$dp[i][j]$$可以有两部分组成。

一部分是用s[i - 1]来匹配，那么个数为$$dp[i - 1][j - 1]$$。即不需要考虑当前s子串和t子串的最后一位字母，所以只需要 $$dp[i-1][j-1]$$。

一部分是不用s[i - 1]来匹配，个数为$$dp[i - 1][j]$$。当s[i - 1] 与 t[j - 1]不相等时，dp[i][j]只有一部分组成，不用s[i - 1]来匹配（就是模拟在s中删除这个元素），即：$$dp[i - 1][j]$$

所以递推公式为：$$dp[i][j] = dp[i - 1][j]$$;



```python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(t)+1) for _ in range(len(s)+1)]
        for i in range(len(s)):
            dp[i][0] = 1
        for j in range(1, len(t)):
            dp[0][j] = 0
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
```

# 两个字符串的删除操作

1.确定dp 数组的含义 

$$dp[i][j]$$：以i-1为结尾的字符串word1，和以j-1位结尾的字符串word2，想要达到相等，所需要删除元素的最少次数。

2.确定递推公式

- 当word1[i - 1] 与 word2[j - 1]相同的时候
- 当word1[i - 1] 与 word2[j - 1]不相同的时候

当word1[i - 1] 与 word2[j - 1]相同的时候，$$dp[i][j] = dp[i - 1][j - 1]$$;

当word1[i - 1] 与 word2[j - 1]不相同的时候，有三种情况：

情况一：删word1[i - 1]，最少操作次数为$$dp[i - 1][j]$$ + 1

情况二：删word2[j - 1]，最少操作次数为$$dp[i][j - 1]$$ + 1

情况三：同时删word1[i - 1]和word2[j - 1]，操作的最少次数为$$dp[i - 1][j - 1]$$ + 2

那最后当然是取最小值，所以当word1[i - 1] 与 word2[j - 1]不相同的时候，递推公式：$$dp[i][j] = min({dp[i - 1][j - 1] + 2, dp[i - 1][j] + 1, dp[i][j - 1] + 1})$$;

3.初始化

从递推公式中，可以看出来，$$dp[i][0] 和 dp[0][j]$$是一定要初始化的。

$$dp[i][0]：word2为空字符串，以i-1为结尾的字符串word1要删除多少个元素，才能和word2相同呢，很明显dp[i][0] = i。$$

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(len(word1)+1):
            dp[i][0] = i
        for j in range(len(word2)+1):
            dp[0][j] = j
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1] + 2, dp[i-1][j] + 1, dp[i][j-1] + 1)
        return dp[-1][-1]
```

# 编辑距离

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0072.%E7%BC%96%E8%BE%91%E8%B7%9D%E7%A6%BB.md

给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

- 插入一个字符

- 删除一个字符

- 替换一个字符

  ​

1.确定dp 数组

$$dp[i][j]$$ 表示以下标i-1为结尾的字符串word1，和以下标j-1为结尾的字符串word2，最近编辑距离为$$dp[i][j]$$。

2.确定递推公式

`if (word1[i - 1] == word2[j - 1])` 那么说明不用任何编辑，`dp[i][j]` 就应该是 `dp[i - 1][j - 1]`，即`dp[i][j] = dp[i - 1][j - 1];`

此时可能有同学有点不明白，为啥要即`dp[i][j] = dp[i - 1][j - 1]`呢？

那么就在回顾上面讲过的`dp[i][j]`的定义，`word1[i - 1]` 与 `word2[j - 1]`相等了，那么就不用编辑了，以下标i-2为结尾的字符串word1和以下标j-2为结尾的字符串`word2`的最近编辑距离`dp[i - 1][j - 1]`就是 `dp[i][j]`了。

`if (word1[i - 1] != word2[j - 1])`，此时就需要编辑了，如何编辑呢？

- 操作一：word1删除一个元素，那么就是以下标i - 2为结尾的word1 与 j-1为结尾的word2的最近编辑距离 再加上一个操作。即 `dp[i][j] = dp[i - 1][j] + 1;`
- 操作二：word2删除一个元素，那么就是以下标i - 1为结尾的word1 与 j-2为结尾的word2的最近编辑距离 再加上一个操作。即 `dp[i][j] = dp[i][j - 1] + 1;`
- 操作三：替换元素，`word1`替换`word1[i - 1]`，使其与`word2[j - 1]`相同，此时不用增删加元素。可以回顾一下，`if (word1[i - 1] == word2[j - 1])`的时候我们的操作 是 `dp[i][j] = dp[i - 1][j - 1]` 。那么只需要一次替换的操作，就可以让 word1[i - 1] 和 word2[j - 1] 相同。所以 `dp[i][j] = dp[i - 1][j - 1] + 1;`

3.初始化

$$dp[i][0]$$ ：以下标i-1为结尾的字符串word1，和空字符串word2，最近编辑距离为$$dp[i][0]$$。那么$$dp[i][0]$$就应该是i，对word1里的元素全部做删除操作，即：$$dp[i][0] = i$$;同理$$dp[0][j] = j$$;

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(len(word1)+1):
            dp[i][0] = i
        for j in range(len(word2)+1):
            dp[0][j] = j
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        return dp[-1][-1]v
```

# 回文子串

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0647.%E5%9B%9E%E6%96%87%E5%AD%90%E4%B8%B2.md

1.确定dp数组含义

布尔类型的$$dp[i][j]$$：表示区间范围[i,j] （注意是左闭右闭）的子串是否是回文子串，如果是$$dp[i][j]$$为true，否则为false。

2.确定递推公式

在确定递推公式时，就要分析如下几种情况。

整体上是两种，就是s[i]与s[j]相等，s[i]与s[j]不相等这两种。

当s[i]与s[j]不相等，那没啥好说的了，dp[i][j]一定是false。

当s[i]与s[j]相等时，这就复杂一些了，有如下三种情况

- 情况一：下标i 与 j相同，同一个字符例如a，当然是回文子串

- 情况二：下标i 与 j相差为1，例如aa，也是回文子串

- 情况三：下标：i 与 j相差大于1的时候，例如cabac，此时s[i]与s[j]已经相同了，我们看i到j区间是不是回文子串就看aba是不是回文就可以了，那么aba的区间就是 i+1 与 j-1区间，这个区间是不是回文就看$$dp[i + 1][j - 1]$$是否为true。

  ​

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        result = 0
        for i in range(len(s)-1, -1, -1): #注意遍历顺序
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1: #情况一 和 情况二
                        result += 1
                        dp[i][j] = True
                    elif dp[i+1][j-1]: #情况三
                        result += 1
                        dp[i][j] = True
        return result
      
 #双指针 从中间扩散  
 class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            result += self.extend(s, i, i, len(s)) #以i为中心
            result += self.extend(s, i, i+1, len(s)) #以i和i+1为中心
        return result
    
    def extend(self, s, i, j, n):
        res = 0
        while i >= 0 and j < n and s[i] == s[j]:
            i -= 1
            j += 1
            res += 1
        return res       
        
```

