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



