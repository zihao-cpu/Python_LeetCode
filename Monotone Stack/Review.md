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



```python
def monotonic_decreasing_stack(arr):
    stack = []
    result = []

    for i, num in enumerate(arr):
        while stack and arr[stack[-1]] < num:
            stack.pop()
        if stack:
            result.append(stack[-1])  # 记录前一个更大元素的下标
        else:
            result.append(-1)
        stack.append(i)
    
    return result
```









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



# 下一个元素

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0496.%E4%B8%8B%E4%B8%80%E4%B8%AA%E6%9B%B4%E5%A4%A7%E5%85%83%E7%B4%A0I.md

保证栈是单调递增的

判断数组2的元素 是否在数组1中出现过

```python
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1]*len(nums1)
        stack = [0]
        for i in range(1,len(nums2)):
            # 情况一情况二
            if nums2[i]<=nums2[stack[-1]]:
                stack.append(i)
            # 情况三
            else:
                while len(stack)!=0 and nums2[i]>nums2[stack[-1]]:
                    if nums2[stack[-1]] in nums1:
                        index = nums1.index(nums2[stack[-1]])
                        result[index]=nums2[i]
                    stack.pop()                 
                stack.append(i)
        return result

```

# 下一个元素2

将两个nums数组拼接在一起，使用单调栈计算出每一个元素的下一个最大值，最后再把结果集即result数组resize到原数组大小就可以了。

```python
// 版本一
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        // 拼接一个新的nums
        vector<int> nums1(nums.begin(), nums.end());
        nums.insert(nums.end(), nums1.begin(), nums1.end());
        // 用新的nums大小来初始化result
        vector<int> result(nums.size(), -1);
        if (nums.size() == 0) return result;

        // 开始单调栈
        stack<int> st;
        st.push(0);
        for (int i = 1; i < nums.size(); i++) { 
            if (nums[i] < nums[st.top()]) st.push(i); 
            else if (nums[i] == nums[st.top()]) st.push(i);
            else { 
                while (!st.empty() && nums[i] > nums[st.top()]) {
                    result[st.top()] = nums[i];
                    st.pop();
                }
                st.push(i);
            }
        }
        // 最后再把结果集即result数组resize到原数组大小
        result.resize(nums.size() / 2);
        return result;
    }
};
```

# 接雨水

**栈顶元素是中间位置**

[60,20,20,10,30]

首先，stack=[],加入 60 的index=0，stack=[0];

循环开始：加入20的index=1,stack=[0,1];

加入20的index=2,stack=[0,1,2];

加入10的index=3,stack=[0,1,2,3];

加入30的index=4，此时要弹出了，弹出的就是中间位置：弹出10的index=3，右侧是30，左侧是弹出10后的栈顶也就是20，此时计算面积。

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        # 单调栈
        '''
        单调栈是按照 行 的方向来计算雨水
        从栈顶到栈底的顺序：从小到大
        通过三个元素来接水：栈顶，栈顶的下一个元素，以及即将入栈的元素
        雨水高度是 min(凹槽左边高度, 凹槽右边高度) - 凹槽底部高度
        雨水的宽度是 凹槽右边的下标 - 凹槽左边的下标 - 1（因为只求中间宽度）
        '''
        # stack储存index，用于计算对应的柱子高度
        stack = [0]
        result = 0
        for i in range(1, len(height)):
            # 情况一
            if height[i] < height[stack[-1]]:
                stack.append(i)

            # 情况二
            # 当当前柱子高度和栈顶一致时，左边的一个是不可能存放雨水的，所以保留右侧新柱子
            # 需要使用最右边的柱子来计算宽度
            elif height[i] == height[stack[-1]]:
                stack.pop()
                stack.append(i)

            # 情况三
            else:
                # 抛出所有较低的柱子
                while stack and height[i] > height[stack[-1]]:
                    # 栈顶就是中间的柱子：储水槽，就是凹槽的地步
                    mid_height = height[stack[-1]]
                    stack.pop()
                    if stack:
                        right_height = height[i]
                        left_height = height[stack[-1]]
                        # 两侧的较矮一方的高度 - 凹槽底部高度
                        h = min(right_height, left_height) - mid_height
                        # 凹槽右侧下标 - 凹槽左侧下标 - 1: 只求中间宽度
                        w = i - stack[-1] - 1
                        # 体积：高乘宽
                        result += h * w
                stack.append(i)
        return result
```

双指针的解法

`leftheight` 数组表示从左边看每个位置左侧（包含当前位置）的最高柱子高度

`rightheight` 数组表示从右边看每个位置右侧（包含当前位置）的最高柱子高度。

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        leftheight, rightheight = [0]*len(height), [0]*len(height)

        leftheight[0]=height[0]
        for i in range(1,len(height)):
            leftheight[i]=max(leftheight[i-1],height[i])
        rightheight[-1]=height[-1]
        for i in range(len(height)-2,-1,-1):
            rightheight[i]=max(rightheight[i+1],height[i])

        result = 0
        for i in range(0,len(height)):
            summ = min(leftheight[i],rightheight[i])-height[i]
            result += summ
        return result
```

# 柱状图中最大的矩形

https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0084.%E6%9F%B1%E7%8A%B6%E5%9B%BE%E4%B8%AD%E6%9C%80%E5%A4%A7%E7%9A%84%E7%9F%A9%E5%BD%A2.md

```python
# 双指针 
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)
        # 两个DP数列储存的均是下标index
        min_left_index = [0] * size
        min_right_index = [0] * size
        result = 0

        # 记录每个柱子的左侧第一个矮一级的柱子的下标
        #例如heights=[3,2,4,3] -> min_left_index=[-1,-1,1,1]
        min_left_index[0] = -1  # 初始化防止while死循环
        for i in range(1, size):
            # 以当前柱子为主心骨，向左迭代寻找次级柱子
            temp = i - 1
            while temp >= 0 and heights[temp] >= heights[i]:
                # 当左侧的柱子持续较高时，尝试这个高柱子自己的次级柱子（DP
                temp = min_left_index[temp]
            # 当找到左侧矮一级的目标柱子时
            min_left_index[i] = temp
        
        # 记录每个柱子的右侧第一个矮一级的柱子的下标
        #例如heights=[3,2,4,3] -> min_left_index=[1,4,3,4]
        min_right_index[size-1] = size  # 初始化防止while死循环
        for i in range(size-2, -1, -1):
            # 以当前柱子为主心骨，向右迭代寻找次级柱子
            temp = i + 1
            while temp < size and heights[temp] >= heights[i]:
                # 当右侧的柱子持续较高时，尝试这个高柱子自己的次级柱子（DP
                temp = min_right_index[temp]
            # 当找到右侧矮一级的目标柱子时
            min_right_index[i] = temp
        
        for i in range(size):
            area = heights[i] * (min_right_index[i] - min_left_index[i] - 1)
            result = max(area, result)
        
        return result
```

