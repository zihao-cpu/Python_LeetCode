## 反转字符串

### 使用双指针

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        
        # 该方法已经不需要判断奇偶数，经测试后时间空间复杂度比用 for i in range(len(s)//2)更低
        # 因为while每次循环需要进行条件判断，而range函数不需要，直接生成数字，因此时间复杂度更低。推荐使用range
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
```

### 使用range

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n // 2):
            s[i], s[n - i - 1] = s[n - i - 1], s[i]
```

### 使用切片

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
```

## 翻转字符串里面的单词

# 制造字母异位词的最小步骤数

输出：s = "leetcode", t = "practice"

输出：5

提示：用合适的字符替换 t 中的 'p', 'r', 'a', 'i' 和 'c'，使 t 变成 s 的字母异位词。

这题说的是改变最少的字母，让两个字符串成为字母异位词，所谓的字母异位词就是两个字符串中的字母相同，且每个字母出现的次数也是相同的，只不过是排序不同。

**这题我们可以先统计两个字符串中每个字符个数的差，最后累加差值，那么最小操作次数就是这个差值的一半。比如字符串abb和aab，第一个字符串比第二个字符串少了一个a但多了一个b，差值是 2 ，我们只需要把第一个字符串中的b变成a，它俩就是字母异位词了。**



```python
def minSteps(s: str, t: str) -> int:
    n = len(s)
    mp = [0] * 128  # 创建一个长度为 128 的列表，用于存储字符的频次
    for i in range(n):
        mp[ord(s[i])] += 1  # 增加 s 中字符的频次
        mp[ord(t[i])] -= 1  # 减少 t 中字符的频次
    
    cnt = 0
    for num in mp:
        cnt += abs(num)  # 计算字符的绝对差值
    return cnt // 2  # 因为每个字符被计算了两次，除以 2 即为最小步骤数
```

