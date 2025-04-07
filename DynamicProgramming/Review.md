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

