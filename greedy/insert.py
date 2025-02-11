#LeetCode第57题
#https://mp.weixin.qq.com/s/n7anja2CQJeYCFgt9TRLKg
def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    ans = []
    for interval in intervals:
        if not newInterval or interval[1] < newInterval[0]:
            # 前面单独的添加进来，或者已经合并完了，把后面的添加进来
            ans.append(interval)
        elif interval[0] > newInterval[1]:
            ans.append(newInterval[:])  # 后面单独的区间。
            ans.append(interval)
            newInterval.clear()
        else:  # 合并区间
            newInterval[0] = min(newInterval[0], interval[0])
            newInterval[1] = max(newInterval[1], interval[1])
    # 如果合并之后的区间没有保存下来，要保存下来
    if newInterval:
        ans.append(newInterval)
    return ans
