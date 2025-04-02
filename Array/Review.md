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

## 三数之和

[leetcode-master/problems/0015.三数之和.md at master · zihao-cpu/leetcode-master](https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0015.%E4%B8%89%E6%95%B0%E4%B9%8B%E5%92%8C.md)

首先将数组排序，然后有一层for循环，i从下标0的地方开始，同时定一个下标left 定义在i+1的位置上，定义下标right 在数组结尾的位置上。依然还是在数组中找到 abc 使得a + b +c =0，我们这里相当于 a = nums[i]，b = nums[left]，c = nums[right]。

接下来如何移动left 和right呢，

 如果nums[i] + nums[left] + nums[right] > 0 就说明 此时三数之和大了，因为数组是排序后了，所以right下标就应该向左移动，这样才能让三数之和小一些。

如果 nums[i] + nums[left] + nums[right] < 0 说明 此时 三数之和小了，left 就向右移动，才能让三数之和大一些，直到left与right相遇为止。

```python
    def threeSum(self,nums:list[int])->list[list[int]]:
        result=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]: #a 去重   注意
                continue 
             '''
             不能写成这样
             if (nums[i] == nums[i + 1])
    			continue
					
             
             '''   
                
            left=i+1
            right=len(nums)-1

            while right>left:
                sum_=nums[i]+nums[left]+nums[right]
                if sum_<0:
                    left+=1
                elif sum_>0:
                    right-=1
                else:
                    result.append[nums[i],nums[left],nums[right]]
                    while right>left and nums[right]==nums[right-1]:
                        right-=1
                    while right>left and nums[left]==nums[left+1]:
                        left+=1
                    right-=1
                    left+=1
        return result
```

## 四数之和

三数之和的基础上再套一层循环

```
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n):
            if nums[i] > target and nums[i] > 0 and target > 0:# 剪枝（可省）
                break
            if i > 0 and nums[i] == nums[i-1]:# 去重
                continue
            for j in range(i+1, n):
                if nums[i] + nums[j] > target and target > 0: #剪枝（可省）
                    break
                if j > i+1 and nums[j] == nums[j-1]: # 去重
                    continue
                left, right = j+1, n-1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1
        return result
```









# 前缀和

## 区间和

[leetcode-master/problems/kamacoder/0058.区间和.md at master · zihao-cpu/leetcode-master](https://github.com/zihao-cpu/leetcode-master/blob/master/problems/kamacoder/0058.%E5%8C%BA%E9%97%B4%E5%92%8C.md)

**前缀和 在涉及计算区间和的问题时非常有用**！

![img](https://camo.githubusercontent.com/c5e8f80aaf6dfb30b68f350755cf96736b2a8b86d1108932ca9131e752fb524b/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303234303632373131313331392e706e67)

p里面存的是累加和

如果，我们想统计，在vec数组上 下标 2 到下标 5 之间的累加和，那是不是就用 p[5] - p[1] 就可以了。

为什么呢？

p[1] = vec[0] + vec[1];

p[5] = vec[0] + vec[1] + vec[2] + vec[3] + vec[4] + vec[5]

p[5] - p[1] = vec[2] + vec[3] + vec[4] + vec[5];

```
    p = [0] * n
    presum = 0
    for i in range(n):
        presum += vec[i]
        p[i] = presum
        
        
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

## 5.多少小于当前数字的数字

[leetcode-master/problems/1365.有多少小于当前数字的数字.md at master · zihao-cpu/leetcode-master](https://github.com/zihao-cpu/leetcode-master/blob/master/problems/1365.%E6%9C%89%E5%A4%9A%E5%B0%91%E5%B0%8F%E4%BA%8E%E5%BD%93%E5%89%8D%E6%95%B0%E5%AD%97%E7%9A%84%E6%95%B0%E5%AD%97.md)

排序结合hash表

数组从小到大排序，排序后的下标就是小于当前数字的个数。存入hash 表中，避免重复的数字。

```python
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = nums[:]
        hash = dict()
        res.sort() # 从小到大排序之后，元素下标就是小于当前数字的数字
        for i, num in enumerate(res):
            if num  not in hash.keys(): # 遇到了相同的数字，那么不需要更新该 number 的情况
                hash[num] = i       
        for i, num in enumerate(nums):
            res[i] = hash[num]
        return res
```



## 6.两数之和

[leetcode-master/problems/0001.两数之和.md at master · zihao-cpu/leetcode-master](https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0001.%E4%B8%A4%E6%95%B0%E4%B9%8B%E5%92%8C.md)

利用hash表 把看过的数字放入 hash 表中

```
class Solution():
    def twoSum(self,nums:list[int],target:int)->list[int]:
        record=dict()
        for index,value in enumerate(nums):
            if target-value in record:
                return [record[target-value],index]
            record[value]=index  #把查看过的数据放入字典
        return []
    
    def twoSum(self,nums:list[int],target:int)->list[int]:
        record=set()
        for index,value in enumerate(nums):
            if target-value in record:
                return [nums.index[target-value],index]
            record.add(value)   #把查看过的数据放入集合
```

## 7.独一无二的数字

[leetcode-master/problems/1207.独一无二的出现次数.md at master · zihao-cpu/leetcode-master](https://github.com/zihao-cpu/leetcode-master/blob/master/problems/1207.%E7%8B%AC%E4%B8%80%E6%97%A0%E4%BA%8C%E7%9A%84%E5%87%BA%E7%8E%B0%E6%AC%A1%E6%95%B0.md)

```python
class Solution:
    def unique(self, nums) -> bool:
        record=dict()
        for num in nums:
            if num in record:   
                record[num]+=1
            else:
                record[num]=1
        values=list(record.values())
        return len(values)==len(set(values))
    
```

## 8.旋转数组

```python
class Solution:
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[-k:] + nums[:-k]
        return nums
    
    def reverse(self, nums, start, end) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    def rotate2(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        self.reverse(nums, 0, n-1) #先整体翻转
        self.reverse(nums, 0, k-1)#再翻转前k个元素
        self.reverse(nums, k, n-1)#再翻转后n-k个元素

if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    k = 3
    Solution().rotate(nums, k)  
```



# 大小为 K 且平均值大于等于阈值的子数组数目

\# 思路：

\# 1. 遍历数组，每次滑动窗口大小为 k ，计算窗口内元素的和，如果和大于等于 k*threshold ，则计数器加 1 。

\# 2. 优化：

\#    由于窗口大小为 k ，因此可以将窗口内元素的和保存到变量 sum 中，每次滑动窗口时，只需要更新 sum 即可。

\#    由于窗口大小为 k ，因此可以将窗口左边界 left 保存到变量中，每次滑动窗口时，只需要更新 left 即可。

\#    由于窗口大小为 k ，因此可以将窗口右边界 right 保存到变量中，每次滑动窗口时，只需要更新 right 即可。

```python
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   numOfSubarrays.py
@Time    :   2025/04/02 10:23:15
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
# 给你一个整数数组 arr 和两个整数 k 和 threshold 。请你返回长度为 k 且平均值大于等于 threshold 的子数组数目。
class Solution:
    def numOfSubarrays(self, arr, k: int, threshold: int) -> int:
        n = len(arr)
        left = 0
        right = k - 1
        count = 0
        while right < n:
            if sum(arr[left:right+1]) / k >= threshold:
                count += 1
            left += 1
            right += 1
        return count
    

    def numOfSubarrays2(self, arr, k: int, threshold: int) -> int:
        sum=0
        ans=0
        target=k*threshold
        for i in range(len(arr)):
            sum+=arr[i]
            if i>=k-1:
                if sum>=target:
                    ans+=1
                sum-=arr[i-k+1]
        return ans
    
# 思路：
# 1. 遍历数组，每次滑动窗口大小为 k ，计算窗口内元素的和，如果和大于等于 k*threshold ，则计数器加 1 。
# 2. 优化：
#    由于窗口大小为 k ，因此可以将窗口内元素的和保存到变量 sum 中，每次滑动窗口时，只需要更新 sum 即可。
#    由于窗口大小为 k ，因此可以将窗口左边界 left 保存到变量中，每次滑动窗口时，只需要更新 left 即可。
#    由于窗口大小为 k ，因此可以将窗口右边界 right 保存到变量中，每次滑动窗口时，只需要更新 right 即可。
if __name__ == '__main__':
    arr = [2, 2, 2, 2, 5, 5, 5, 8]
    k = 3
    threshold = 4
    print(Solution().numOfSubarrays(arr, k, threshold)) # 3
```







