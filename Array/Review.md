# 双指针



###1.移除元素：
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



###2.移除0值： 
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

