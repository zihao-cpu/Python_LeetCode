def longestConsecutive(self, nums: List[int]) -> int:
    mySet = set(nums)
    maxLen = 0
    for num in nums:
        if num - 1 not in mySet:  # 判断是否是起始位置
            curNum = num  # 从起始位置开始查找连续序列的长度
            len = 1
            while curNum + 1 in mySet:
                curNum += 1
                len += 1
            maxLen = max(maxLen, len)
    return maxLen
