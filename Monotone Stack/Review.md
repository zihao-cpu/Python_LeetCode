# 单调栈

[算法数据结构——关于单调栈（Monotone Stack）的详细讲解及应用案例-CSDN博客](https://blog.csdn.net/zy_dreamer/article/details/131036101)

**单调递增栈的入栈、出栈过程如下：**

1.假设当前进栈元素为 x，如果 x 比栈顶元素小，则直接入栈。

2.否则从栈顶开始遍历栈中元素，把小于 x 或者等于 x 的元素弹出栈，直到遇到一个大于 x 的元素为止，然后再把 x 压入栈中。

下面我们以数组 [2, 7, 5, 4, 6, 3, 4, 2] 为例，模拟一下「单调递增栈」的进栈、出栈过程。具体过程如下：

| 第 i 步 | 待插入元素 | 操作             | 结果（左侧为栈底）    | 作用                     |
| ----- | ----- | -------------- | ------------ | ---------------------- |
| 1     | 2     | 2 入栈           | [2]          | 元素 2 的左侧无比 2 大的元素      |
| 2     | 7     | 2 出栈，7 入栈      | [7]          | 元素 7 的左侧无比 7 大的元素      |
| 3     | 5     | 5 入栈           | [7, 5]       | 元素 5 的左侧第一个比 5 大的元素为：7 |
| 4     | 4     | 4 入栈           | [7, 5, 4]    | 元素 4 的左侧第一个比 4 大的元素为：5 |
| 5     | 6     | 4 出栈，5 出栈，6 入栈 | [7, 6]       | 元素 6 的左侧第一个比 6 大的元素为：7 |
| 6     | 3     | 3 入栈           | [7, 6, 3]    | 元素 3 的左侧第一个比 3 大的元素为：6 |
| 7     | 4     | 3 出栈，4 入栈      | [7, 6, 4]    | 元素 4 的左侧第一个比 4 大的元素为：6 |
| 8     | 2     | 2 入栈           | [7, 6, 4, 2] | 元素 2 的左侧第一个比 2 大的元素为：4 |

**单调递减栈的入栈、出栈过程如下：**

1.假设当前进栈元素为 x，如果 x 比栈顶元素大，则直接入栈。

2.否则从栈顶开始遍历栈中元素，把大于 x 或者等于 x 的元素弹出栈，直到遇到一个小于 x 的元素为止，然后再把 x 压入栈中。

下面我们以数组 [4, 3, 2, 5, 7, 4, 6, 8] 为例，模拟一下「单调递减栈」的进栈、出栈过程。具体过程如下：

| 第 i 步 | 待插入元素 | 操作             | 结果（左侧为栈底）    | 作用                     |
| ----- | ----- | -------------- | ------------ | ---------------------- |
| 1     | 4     | 4 入栈           | [4]          | 元素 4 的左侧无比 4 小的元素      |
| 2     | 3     | 4 出栈，3 入栈      | [3]          | 元素 3 的左侧无比 3 小的元素      |
| 3     | 2     | 3 出栈，2 入栈      | [2]          | 元素 2 的左侧无比 2 小的元素      |
| 4     | 5     | 5 入栈           | [2, 5]       | 元素 5 的左侧第一个比 5 小的元素是：2 |
| 5     | 7     | 7 入栈           | [2, 5, 7]    | 元素 7 的左侧第一个比 7 小的元素是：5 |
| 6     | 4     | 7 出栈，5 出栈，4 入栈 | [2, 4]       | 元素 4 的左侧第一个比 4 小的元素是：2 |
| 7     | 6     | 6 入栈           | [2, 4, 6]    | 元素 6 的左侧第一个比 6 小的元素是：4 |
| 8     | 8     | 8 入栈           | [2, 4, 6, 8] | 元素 8 的左侧第一个比 8 小的元素是：6 |

原文链接：https://blog.csdn.net/zy_dreamer/article/details/131036101

# 每日温度

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0739.%E6%AF%8F%E6%97%A5%E6%B8%A9%E5%BA%A6.md

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while len(stack)>0 and temperatures[i] > temperatures[stack[-1]]:
                answer[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return answer
      
      
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        stack = [0]
        for i in range(1,len(temperatures)):
            # 情况一和情况二
            if temperatures[i]<=temperatures[stack[-1]]:
                stack.append(i)
            # 情况三
            else:
                while len(stack) != 0 and temperatures[i]>temperatures[stack[-1]]:
                    answer[stack[-1]]=i-stack[-1]
                    stack.pop()
                stack.append(i)

        return answer
```

