# 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

# 示例 1：

# 输入：nums = [-4,-1,0,3,10]
# 输出：[0,1,9,16,100]
# 解释：平方后，数组变为 [16,1,0,9,100]，排序后，数组变为 [0,1,9,16,100]
# 示例 2：

# 输入：nums = [-7,-3,2,3,11]
# 输出：[4,9,9,49,121]


# 采用双指针
from typing import List
class Solution():
    def sortedSquares(self,nums:List[int])->List[int]:
        res=[float('inf')]*len(nums)
        l,r,i=0,len(nums)-1,len(nums)-1
        while l<=r:
            if nums[l]**2<nums[r]**2:
                res[i]=nums[r]**2
                r-=1
            else:
                res[i]=nums[l]**2
                l+=1
            i-=1
        return res
    

newSolution=Solution()
print(newSolution.sortedSquares([0,1,9,16,100]))