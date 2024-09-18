# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。

# 示例：

# 输入：s = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   minSubArrayLen.py
@Time    :   2024/09/18 20:21:08
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
from typing import List
class Solution():
    def minSubArrayLen(self,nums:List[int],s:int)->int:
        left,right,l=0,0,len(nums)
        currentNum=0
        min_len=float('inf')
        while right<l:
            currentNum+=nums[right]
            #################################
            while currentNum>=s:
                currentNum-=nums[left]
                min_len=min(min_len,right-left+1)
                left+=1
            #这段代码是关键，首先 right规定了一个滑动窗的结尾 然后去判断 这个滑动窗内是否还有更小的字串
            ################################
            right+=1
        return min_len
newSolution=Solution()
print(newSolution.minSubArrayLen([2,3,1,2,4,3],7))


###########对应LeetCode NO.904 以下是我的解法 但是超时
from typing import List
class Solution():
    def minSubArrayLen2(self,nums:List[int])->int:
        left,right,l=0,0,len(nums)
        min_len=0
        while right<l:
            currentSet=set(nums[left:right+1])
            #################################
            if len(currentSet)>2:
                currentSet=set(nums[left:right+1])
                min_len=max(min_len,right-left)
                left+=1
            right+=1
        min_len=max(min_len,right-left)
        return min_len
newSolution=Solution()
print(newSolution.minSubArrayLen2([3,3,3,1,2,1,1,2,3,3,4]))

from collections import Counter
cnt = Counter() #用哈希表来完成
fruits=[3,3,3,1,2,1,1,2,3,3,4]
left = ans = 0
for right, x in enumerate(fruits):
    cnt[x] += 1
    while len(cnt) > 2:
        cnt[fruits[left]] -= 1
        if cnt[fruits[left]] == 0:
            cnt.pop(fruits[left])
        left += 1
    ans = max(ans, right - left + 1)

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/fruit-into-baskets/solutions/1893352/shui-guo-cheng-lan-by-leetcode-solution-1uyu/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。








