# 链表

## 1.移除链表元素

[代码随想录](https://programmercarl.com/0203.%E7%A7%BB%E9%99%A4%E9%93%BE%E8%A1%A8%E5%85%83%E7%B4%A0.html)

可以设置虚拟头结点，原链表的所有的节点都可以按照统一的方式进行移除.return 头结点的时候，别忘了 return  dummyNode->next

![203_链表删除元素6](https://camo.githubusercontent.com/ebe1cad971e1e217bbc5f120d36fd28114108b0f94caacf4a29f6eb0a4914d44/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303231303331363039353631393232312e706e67)

```
版本一）虚拟头节点法
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 创建虚拟头部节点以简化删除过程
        dummy_head = ListNode(next = head)
        
        # 遍历列表并删除值为val的节点
        current = dummy_head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        
        return dummy_head.next
    
```

## 2.设计链表

```
（版本一）单链表法
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class MyLinkedList:
    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        current = self.dummy_head.next
        for i in range(index):
            current = current.next
            
        return current.val

    def addAtHead(self, val: int) -> None:
        self.dummy_head.next = ListNode(val, self.dummy_head.next)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        current = self.dummy_head
        while current.next:
            current = current.next
        current.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        
        current = self.dummy_head
        for i in range(index):
            current = current.next
        current.next = ListNode(val, current.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        current = self.dummy_head
        for i in range(index):
            current = current.next
        current.next = current.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
```

## 3.两两交换节点

[leetcode-master/problems/0024.两两交换链表中的节点.md at master · zihao-cpu/leetcode-master](https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0024.%E4%B8%A4%E4%B8%A4%E4%BA%A4%E6%8D%A2%E9%93%BE%E8%A1%A8%E4%B8%AD%E7%9A%84%E8%8A%82%E7%82%B9.md)

![24.两两交换链表中的节点1](https://camo.githubusercontent.com/5d91c44c49f123047a51a63b2d36c271e225ec7f0110ed623c93bcf94d17ee98/68747470733a2f2f636f64652d7468696e6b696e672e63646e2e626365626f732e636f6d2f706963732f32342e254534254238254134254534254238254134254534254241254134254536253844254132254539253933254245254538254131254138254534254238254144254537253941253834254538253841253832254537253832254239312e706e67)

递归版本

```
#伪代码
funcion(head)
	pre=head
  	cur=head.next
    next=head.next.next
    cur.next=pre
    pre.next=function(next)
    return cur
```

```python
# 递归版本
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        # 待翻转的两个node分别是pre和cur
        pre = head
        cur = head.next
        next = head.next.next
        
        cur.next = pre  # 交换
        pre.next = self.swapPairs(next) # 将以next为head的后续链表两两交换
         
        return cur

```

```python
#模拟版本
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(next=head)
        current = dummy_head
        
        # 必须有cur的下一个和下下个才能交换，否则说明已经交换结束了
        while current.next and current.next.next:
            temp = current.next # 防止节点修改
            temp1 = current.next.next.next
            
            current.next = current.next.next
            current.next.next = temp
            temp.next = temp1
            current = current.next.next
        return dummy_head.next
```



## 4.删除链表的倒数第N个节点

双指针的经典应用，如果要删除倒数第n个节点，让fast移动n步，然后让fast和slow同时移动，直到fast指向链表末尾。删掉slow所指向的节点就可以了

![img](https://camo.githubusercontent.com/951b1807964b821d0ecdc600937a050bff11e8d287adf8ee208aca8430dbf1a4/68747470733a2f2f636f64652d7468696e6b696e672e63646e2e626365626f732e636f6d2f706963732f31392e2545352538382541302545392539392541342545392539332542452545382541312541382545372539412538342545352538302539322545362539352542302545372541432541434e2545342542382541412545382538412538322545372538322542392e706e67)

![img](https://camo.githubusercontent.com/c72f3d8e7dc02f6458aa3bef1199f984c294a3ebc10c7099fde60720adef853f/68747470733a2f2f636f64652d7468696e6b696e672e63646e2e626365626f732e636f6d2f706963732f31392e2545352538382541302545392539392541342545392539332542452545382541312541382545372539412538342545352538302539322545362539352542302545372541432541434e254534254238254141254538253841253832254537253832254239322e706e67)

slow的位置就是链表倒数N的位置。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 创建一个虚拟节点，并将其下一个指针设置为链表的头部
        dummy_head = ListNode(0, head)
        
        # 创建两个指针，慢指针和快指针，并将它们初始化为虚拟节点
        slow = fast = dummy_head
        
        # 快指针比慢指针快 n+1 步
        for i in range(n+1):
            fast = fast.next
        
        # 移动两个指针，直到快速指针到达链表的末尾
        while fast:
            slow = slow.next
            fast = fast.next
        
        # 通过更新第 (n-1) 个节点的 next 指针删除第 n 个节点
        slow.next = slow.next.next
        
```

## 5.链表相交

[leetcode-master/problems/面试题02.07.链表相交.md at master · zihao-cpu/leetcode-master](https://github.com/zihao-cpu/leetcode-master/blob/master/problems/%E9%9D%A2%E8%AF%95%E9%A2%9802.07.%E9%93%BE%E8%A1%A8%E7%9B%B8%E4%BA%A4.md)

简单来说，就是求两个链表交点节点的**指针**。 这里同学们要注意，交点不是数值相等，而是指针相等。

为了方便举例，假设节点元素数值相等，则节点指针相等。

看如下两个链表，目前curA指向链表A的头结点，curB指向链表B的头结点：



![面试题02.07.链表相交_1](https://camo.githubusercontent.com/71d352988b0ffaa52b25fad679200ba83fcb305037b8990d6e87b766d29aed05/68747470733a2f2f636f64652d7468696e6b696e672e63646e2e626365626f732e636f6d2f706963732f25453925394425413225453825414625393525453925413225393830322e30372e2545392539332542452545382541312541382545372539422542382545342542412541345f312e706e67)



![面试题02.07.链表相交_2](https://camo.githubusercontent.com/9011b5336369e3e3ca6139ce672cc272104557eebdd700dbcdd5d105bc0c8cd5/68747470733a2f2f636f64652d7468696e6b696e672e63646e2e626365626f732e636f6d2f706963732f25453925394425413225453825414625393525453925413225393830322e30372e2545392539332542452545382541312541382545372539422542382545342542412541345f322e706e67)

此时我们就可以比较curA和curB是否相同，如果不相同，同时向后移动curA和curB，如果遇到curA == curB，则找到交点。

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB = 0, 0
        cur = headA
        while cur:         # 求链表A的长度
            cur = cur.next 
            lenA += 1
        cur = headB 
        while cur:         # 求链表B的长度
            cur = cur.next 
            lenB += 1
        curA, curB = headA, headB
        if lenA > lenB:     # 让curB为最长链表的头，lenB为其长度
            curA, curB = curB, curA
            lenA, lenB = lenB, lenA 
        for _ in range(lenB - lenA):  # 让curA和curB在同一起点上（末尾位置对齐）
            curB = curB.next 
        while curA:         #  遍历curA 和 curB，遇到相同则直接返回
            if curA == curB:
                return curA
            else:
                curA = curA.next 
                curB = curB.next
        return None 
```

## 6.重排链表

[leetcode-master/problems/0143.重排链表.md at master · zihao-cpu/leetcode-master](https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0143.%E9%87%8D%E6%8E%92%E9%93%BE%E8%A1%A8.md)

双向队列

加入双向队列后 一后一前弹出

```python
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        d=collections.deque()
        tmp=head
        while tmp.next:
            d.append(tmp.next)
            tmp=tmp.next
        tmp=head
        while d:
            tmp.next=d.pop()
            tmp=tmp.next
            if len(d):
                tmp.next=d.popleft()
                tmp=tmp.next
        tmp.next=None
```



分割链表

![img](https://camo.githubusercontent.com/f0286d83bfb1310344a73e02a8e6e8fa72eef9f0a7453bf3cbfd579f74112b77/68747470733a2f2f636f64652d7468696e6b696e672e63646e2e626365626f732e636f6d2f706963732f3134332ee9878de68e92e993bee8a1a82e706e67)

```python
# 方法三 反转链表
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head == None or head.next == None:
            return True
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right = slow.next # 分割右半边
        slow.next = None # 切断
        right = self.reverseList(right) #反转右半边
        left = head
        # 左半边一定比右半边长, 因此判断右半边即可
        while right:
            curLeft = left.next
            left.next = right
            left = curLeft

            curRight = right.next
            right.next = left
            right = curRight


    def reverseList(self, head: ListNode) -> ListNode:
            if not head or not head.next:
                return head
            pre=None
            cur=head
            while cur:
                nxt=cur.next
                cur.next=pre
                pre=cur
                cur=nxt
            return pre
```

```
涉及到的细节:首先吧cur.next存出来，因为原始的cur的next会发生变化的 :nxt=cur.next curLeft = left.next都是有体现的。
```

## 7.环形链表

[leetcode-master/problems/0141.环形链表.md at master · zihao-cpu/leetcode-master](https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0141.%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A8.md)

快慢指针

```python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head: return False
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
```

## 8.环形链表2

[leetcode-master/problems/0142.环形链表II.md at master · zihao-cpu/leetcode-master](https://github.com/zihao-cpu/leetcode-master/blob/master/problems/0142.%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A8II.md)

![142环形链表5](https://camo.githubusercontent.com/caad5d92f6a26b7cca39c8bfec5a7ddc40ca10073291cbf46e45fcc335bb63bf/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303231303331383136353132333538312e706e67)

(x + y) * 2 = x + y + n (y + z)

x=(n-1)(y+z)+z

```python
（版本一）快慢指针法
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If there is a cycle, the slow and fast pointers will eventually meet
            if slow == fast:
                # Move one of the pointers back to the start of the list
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        # If there is no cycle, return None
        return None
```

集合法 把看过的节点放入集合中

```python
（版本二）集合法
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()
        
        while head:
            if head in visited:
                return head
            visited.add(head)
            head = head.next
        return None
```

