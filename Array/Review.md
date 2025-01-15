# 双指针



##1.移除元素：
  https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0027.%E7%A7%BB%E9%99%A4%E5%85%83%E7%B4%A0.md; 

```
from typing import List
class Solution:
    def removeElement(self,nums:List[int],val:int)->int:
        slow=0
        size=len    (nums)
        for fast in range(0,size):
            if val != nums[fast]:
                
                nums[slow]=nums[fast]
                slow +=1
        return slow
```

##2.移除0值： 

  https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0283.%E7%A7%BB%E5%8A%A8%E9%9B%B6.md；


```python
def moveZeros(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    slow=0
    for fast in range(len(nums)):

        if nums[fast]!=0:
            nums[slow]=nums[fast]
            slow+=1

            
    for i in range(slow,len(nums)):
        nums[i]=0
```

## 3.有序数组的平方

[leetcode-master/problems/0977.有序数组的平方.md at master · zihao-cpu/leetcode-master](https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0977.%E6%9C%89%E5%BA%8F%E6%95%B0%E7%BB%84%E7%9A%84%E5%B9%B3%E6%96%B9.md)

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r, i = 0, len(nums)-1, len(nums)-1
        res = [float('inf')] * len(nums) # 需要提前定义列表，存放结果
        while l <= r:
            if nums[l] ** 2 < nums[r] ** 2: # 左右边界进行对比，找出最大值
                res[i] = nums[r] ** 2
                r -= 1 # 右指针往左移动
            else:
                res[i] = nums[l] ** 2
                l += 1 # 左指针往右移动
            i -= 1 # 存放结果的指针需要往前平移一位
        return res
```



# 滑动窗口

1.首先确定窗口里面是什么

2.如何移动窗口的起始位置

3.如何移动窗口的结束位置

## 4.长度最小的子数组

[leetcode-master/problems/0209.长度最小的子数组.md at master · zihao-cpu/leetcode-master](https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0209.%E9%95%BF%E5%BA%A6%E6%9C%80%E5%B0%8F%E7%9A%84%E5%AD%90%E6%95%B0%E7%BB%84.md)

```python
#窗口内是 满足其和 ≥ s 的长度最小的 连续 子数组。
#窗口的起始位置如何移动：如果当前窗口的值大于等于s了，窗口就要向前移动了（也就是该缩小了）。
#窗口的结束位置如何移动：窗口的结束位置就是遍历数组的指针，也就是for循环里的索引。
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left = 0
        right = 0
        min_len = float('inf') #窗口的长度
        cur_sum = 0 #当前的累加值 窗口内的和        
        while right < len(nums):
            cur_sum += nums[right]
            while cur_sum >= s: # 当前累加值大于目标值
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1
            right += 1
        
        return min_len if min_len != float('inf') else 0
```

# 模拟

## 5.旋转数组

[leetcode-master/problems/0059.螺旋矩阵II.md at master · zihao-cpu/leetcode-master](https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0059.%E8%9E%BA%E6%97%8B%E7%9F%A9%E9%98%B5II.md)

定义四个边界来模拟

top=0 bottom=n-1 left=0 right=n-1

```python
class Solution(object):
    def generateMatrix(self, n):
        if n <= 0:
            return []
        
        # 初始化 n x n 矩阵
        matrix = [[0]*n for _ in range(n)]

        # 初始化边界和起始值
        top, bottom, left, right = 0, n-1, 0, n-1
        num = 1

        while top <= bottom and left <= right:
            # 从左到右填充上边界
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1

            # 从上到下填充右边界
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1

            # 从右到左填充下边界

            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

            # 从下到上填充左边界

            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

        return matrix
```

