# 贪心算法

局部最优->全局最优



# 分发饼干

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0455.%E5%88%86%E5%8F%91%E9%A5%BC%E5%B9%B2.md

为了满足更多的小孩，就不要造成饼干尺寸的浪费。

大尺寸的饼干既可以满足胃口大的孩子也可以满足胃口小的孩子，那么就应该优先满足胃口大的。

**这里的局部最优就是大饼干喂给胃口大的，充分利用饼干尺寸喂饱一个，全局最优就是喂饱尽可能多的小孩**。

可以尝试使用贪心策略，先将饼干数组和小孩数组排序。

然后从后向前遍历小孩数组，用大饼干优先满足胃口大的，并统计满足小孩数量。

```python
class Solution:
    def findContentChildren(self, g, s):
        g.sort()  # 将孩子的贪心因子排序
        s.sort()  # 将饼干的尺寸排序
        index = len(s) - 1  # 饼干数组的下标，从最后一个饼干开始
        result = 0  # 满足孩子的数量
        for i in range(len(g)-1, -1, -1):  # 遍历胃口，从最后一个孩子开始
            if index >= 0 and s[index] >= g[i]:  # 遍历饼干
                result += 1
                index -= 1
        return result
```

# 摆动序列

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0376.%E6%91%86%E5%8A%A8%E5%BA%8F%E5%88%97.md



那么我们应该什么时候更新 prediff 呢？

我们只需要在 这个坡度 摆动变化的时候，更新 prediff 就行，这样 prediff 在 单调区间有平坡的时候 就不会发生变化，造成我们的误判。

```python
class Solution:
    def wiggleMaxLength(self, nums):
        if len(nums) <= 1:
            return len(nums)  # 如果数组长度为0或1，则返回数组长度
        curDiff = 0  # 当前一对元素的差值
        preDiff = 0  # 前一对元素的差值
        result = 1  # 记录峰值的个数，初始为1（默认最右边的元素被视为峰值）
        for i in range(len(nums) - 1):
            curDiff = nums[i + 1] - nums[i]  # 计算下一个元素与当前元素的差值
            # 如果遇到一个峰值
            if (preDiff <= 0 and curDiff > 0) or (preDiff >= 0 and curDiff < 0):
                result += 1  # 峰值个数加1
                preDiff = curDiff  # 注意这里，只在摆动变化的时候更新preDiff
        return result  # 返回最长摆动子序列的长度
```

# 最大子序和

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0053.%E6%9C%80%E5%A4%A7%E5%AD%90%E5%BA%8F%E5%92%8C.md

局部最优：当前“连续和”为负数的时候立刻放弃，从下一个元素重新计算“连续和”，因为负数加上下一个元素 “连续和”只会越来越小。**遍历 nums，从头开始用 count 累积，如果 count 一旦加上 nums[i]变为负数，那么就应该从 nums[i+1]开始从 0 累积 count 了，因为已经变为负数的 count，只会拖累总和。**

```python
class Solution:
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

# 买卖股票2

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0122.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BAII.md

![122.买卖股票的最佳时机II](https://camo.githubusercontent.com/afca931d44f9a0a879bc1fc29d9dc4255e0df106f151a5bb7b007bb195861824/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f323032303131323931373438303835382d32303233303331303133343635393437372e706e67)

从图中可以发现，其实我们需要收集每天的正利润就可以，**收集正利润的区间，就是股票买卖的区间，而我们只需要关注最终利润，不需要记录区间**。

那么只收集正利润就是贪心所贪的地方！

**局部最优：收集每天的正利润，全局最优：求得最大利润**。

局部最优可以推出全局最优，找不出反例，试一试贪心！

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(1, len(prices)):
            result += max(prices[i] - prices[i - 1], 0)
        return result
```



# 跳跃游戏

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0055.%E8%B7%B3%E8%B7%83%E6%B8%B8%E6%88%8F.md

![img](https://camo.githubusercontent.com/20d86ba18186ae1352192c7898b01e33519a374d94c5e1b5b97a19aeffd3c448/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303233303230333130353633342e706e67)

其实跳几步无所谓，关键在于可跳的覆盖范围！

不一定非要明确一次究竟跳几步，每次取最大的跳跃步数，这个就是可以跳跃的覆盖范围。

这个范围内，别管是怎么跳的，反正一定可以跳过来。

**那么这个问题就转化为跳跃覆盖范围究竟可不可以覆盖到终点！**

每次移动取最大跳跃步数（得到最大的覆盖范围），每移动一个单位，就更新最大覆盖范围。

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0
        if len(nums) == 1: return True
        i = 0
        # python不支持动态修改for循环中变量,使用while循环代替
        while i <= cover:
            cover = max(i + nums[i], cover)
            if cover >= len(nums) - 1: return True
            i += 1
        return False
      
      
 ## for循环
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0
        if len(nums) == 1: return True
        for i in range(len(nums)):
            if i <= cover:
                cover = max(i + nums[i], cover)
                if cover >= len(nums) - 1: return True
        return False
```

# 跳跃游戏2

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0045.%E8%B7%B3%E8%B7%83%E6%B8%B8%E6%88%8FII.md

![45.跳跃游戏II](https://camo.githubusercontent.com/2edd43825df9eb9106f2727e9295e7a558734e2c2f6139ef40cf66d493d1844d/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303230313230313233323330393130332e706e67)

本题要计算最少步数，那么就要想清楚什么时候步数才一定要加一呢？

贪心的思路，局部最优：**当前可移动距离尽可能多走，如果还没到终点，步数再加一**。整体最优：一步尽可能多走，从而达到最少步数。

**所以真正解题的时候，要从覆盖范围出发，不管怎么跳，覆盖范围内一定是可以跳到的，以最小的步数增加覆盖范围，覆盖范围一旦覆盖了终点，得到的就是最少步数！**



```
 cur_distance = 0  # 当前覆盖最远距离下标
 next_distance = 0  # 下一步覆盖最远距离下标
```

```python
class Solution:
    def jump(self, nums):
        if len(nums) == 1:
            return 0
        
        cur_distance = 0  # 当前覆盖最远距离下标
        ans = 0  # 记录走的最大步数
        next_distance = 0  # 下一步覆盖最远距离下标
        
        for i in range(len(nums)):
            next_distance = max(nums[i] + i, next_distance)  # 更新下一步覆盖最远距离下标
            if i == cur_distance:  # 遇到当前覆盖最远距离下标
                ans += 1  # 需要走下一步
                cur_distance = next_distance  # 更新当前覆盖最远距离下标（相当于加油了）
                if next_distance >= len(nums) - 1:  # 当前覆盖最远距离达到数组末尾，不用再做ans++操作，直接结束
                    break
        
        return ans
```

# K次取反后最大化

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/1005.K%E6%AC%A1%E5%8F%96%E5%8F%8D%E5%90%8E%E6%9C%80%E5%A4%A7%E5%8C%96%E7%9A%84%E6%95%B0%E7%BB%84%E5%92%8C.md

让绝对值大的负数变为正数，当前数值达到最大，整体最优：整个数组和达到最大。

那么如果将负数都转变为正数了，K依然大于0，此时的问题是一个有序正整数序列，如何转变K次正负，让 数组和 达到最大。

那么又是一个贪心：局部最优：只找数值最小的正整数进行反转，当前数值和可以达到最大

- 第一步：将数组按照绝对值大小从大到小排序，**注意要按照绝对值的大小**
- 第二步：从前向后遍历，遇到负数将其变为正数，同时K--
- 第三步：如果K还大于0，那么反复转变数值最小的元素，将K用完
- 第四步：求和

```python
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort(key=lambda x: abs(x), reverse=True)  # 第一步：按照绝对值降序排序数组A

        for i in range(len(A)):  # 第二步：执行K次取反操作
            if A[i] < 0 and K > 0:
                A[i] *= -1
                K -= 1

        if K % 2 == 1:  # 第三步：如果K还有剩余次数，将绝对值最小的元素取反
            A[-1] *= -1

        result = sum(A)  # 第四步：计算数组A的元素和
        return result
```





