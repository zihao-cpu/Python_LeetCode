# 深搜

```
void dfs(参数) {
    if (终止条件) {
        存放结果;
        return;
    }

    for (选择：本节点所连接的其他节点) {
        处理节点;
        dfs(图，选择的节点); // 递归
        回溯，撤销处理结果
    }
}
```

# 图的存储

## 邻接矩阵

邻接矩阵 使用 二维数组来表示图结构。 邻接矩阵是从节点的角度来表示图，有多少节点就申请多大的二维数组。

本题我们会有n 个节点，因为节点标号是从1开始的，为了节点标号和下标对齐，我们申请 n + 1 * n + 1 这么大的二维数组

## 邻接表

邻接表 使用 数组 + 链表的方式来表示。 邻接表是从边的数量来表示图，有多少边 才会申请对应大小的链表。

## 所有可达路径

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/kamacoder/0098.%E6%89%80%E6%9C%89%E5%8F%AF%E8%BE%BE%E8%B7%AF%E5%BE%84.md

1.确定递归函数

首先我们dfs函数一定要存一个图，用来遍历的，需要存一个目前我们遍历的节点，定义为x。还需要存一个n，表示终点，我们遍历的时候，用来判断当 x==n 时候 标明找到了终点。

```
vector<vector<int>> result; // 收集符合条件的路径
vector<int> path; // 0节点到终点的路径
// x：目前遍历的节点
// graph：存当前的图
// n：终点
void dfs (const vector<vector<int>>& graph, int x, int n) {
```

2.确认终止条件

什么时候我们就找到一条路径了？

当目前遍历的节点 为 最后一个节点 n 的时候 就找到了一条 从出发点到终止点的路径。

```
// 当前遍历的节点x 到达节点n 
if (x == n) { // 找到符合条件的一条路径
    result.push_back(path);
    return;
}
```

3.单层递归逻辑

```
for (int i = 1; i <= n; i++) { // 遍历节点x链接的所有节点
    if (graph[x][i] == 1) { // 找到 x链接的节点
        path.push_back(i); // 遍历到的节点加入到路径中来
        dfs(graph, i, n); // 进入下一层递归
        path.pop_back(); // 回溯，撤销本节点
    }
}
```

```python
def dfs(graph, x, n, path, result):
    if x == n:
        result.append(path.copy())
        return
    for i in range(1, n + 1):
        if graph[x][i] == 1:
            path.append(i)
            dfs(graph, i, n, path, result)
            path.pop()

def main():
    n, m = map(int, input().split())
    graph = [[0] * (n + 1) for _ in range(n + 1)]

    for _ in range(m):
        s, t = map(int, input().split())
        graph[s][t] = 1

    result = []
    dfs(graph, 1, n, [1], result)

    if not result:
        print(-1)
    else:
        for path in result:
            print(' '.join(map(str, path)))

if __name__ == "__main__":
    main()
```

# 广搜

需要一个容器来存储 遍历的元素

a .首先选择一个顶点作为起始结点，并将其染成灰色，其余结点为白色。
b. 将起始结点放入队列中。
c. 从队列首部选出一个顶点，并找出所有与之邻接的结点，将找到的邻接结点放入队列尾部，将已访问过结点涂成黑色，没访问过的结点是白色。如果顶点的颜色是灰色，表示已经发现并且放入了队列，如果顶点的颜色是白色，表示还没有发现。
d. 按照同样的方法处理队列中的下一个结点。基本就是出队的顶点变成黑色，在队列里的是灰色，还没入队的是白色

from https://www.cnblogs.com/aiguona/p/7268667.html



**这里无向图求最短路，广搜最为合适，广搜只要搜到了终点，那么一定是最短的路径**。因为广搜就是以起点中心向四周扩散的搜索

# 岛屿数量-深搜版

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/kamacoder/0099.%E5%B2%9B%E5%B1%BF%E7%9A%84%E6%95%B0%E9%87%8F%E6%B7%B1%E6%90%9C.md

```python
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 四个方向：上、右、下、左


def dfs(grid, visited, x, y):
    """
    对一块陆地进行深度优先遍历并标记
    """
    for i, j in direction:
        next_x = x + i
        next_y = y + j
        # 下标越界，跳过
        if next_x < 0 or next_x >= len(grid) or next_y < 0 or next_y >= len(grid[0]):
            continue
        # 未访问的陆地，标记并调用深度优先搜索
        if not visited[next_x][next_y] and grid[next_x][next_y] == 1:
            visited[next_x][next_y] = True
            dfs(grid, visited, next_x, next_y)


if __name__ == '__main__':  
    # 版本一
    n, m = map(int, input().split())
    
    # 邻接矩阵
    grid = []
    for i in range(n):
        grid.append(list(map(int, input().split())))
    
    # 访问表
    visited = [[False] * m for _ in range(n)]
    
    res = 0
    for i in range(n):
        for j in range(m):
            # 判断：如果当前节点是陆地，res+1并标记访问该节点，使用深度搜索标记相邻陆地。
            if grid[i][j] == 1 and not visited[i][j]:
                res += 1
                visited[i][j] = True
                dfs(grid, visited, i, j)
    
    print(res)
```

# 岛屿数量-广搜版

```python

from collections import deque
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def bfs(grid, visited, x, y):
    que = deque([])
    que.append([x,y])
    while que:
        cur_x, cur_y = que.popleft()
        for i, j in directions:
            next_x = cur_x + i
            next_y = cur_y + j#有连接
            if next_y < 0 or next_x < 0 or next_x >= len(grid) or next_y >= len(grid[0]):
                continue
            if not visited[next_x][next_y] and grid[next_x][next_y] == 1: 
                visited[next_x][next_y] = True
                que.append([next_x, next_y])


def main():
    n, m = map(int, input().split())
    grid = []
    for i in range(n):
        grid.append(list(map(int, input().split())))
    visited = [[False] * m for _ in range(n)]
    res = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                res += 1
                bfs(grid, visited, i, j)
    print(res)

if __name__ == "__main__":
    main()



```

#岛屿最大面积-深搜版

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/kamacoder/0100.%E5%B2%9B%E5%B1%BF%E7%9A%84%E6%9C%80%E5%A4%A7%E9%9D%A2%E7%A7%AF.md

```python
# 四个方向
position = [[0, 1], [1, 0], [0, -1], [-1, 0]]
count = 0


def dfs(grid, visited, x, y):
    """
    深度优先搜索，对一整块陆地进行标记
    """
    global count  # 定义全局变量，便于传递count值
    for i, j in position:
        cur_x = x + i
        cur_y = y + j
        # 下标越界，跳过
        if cur_x < 0 or cur_x >= len(grid) or cur_y < 0 or cur_y >= len(grid[0]):
            continue
        if not visited[cur_x][cur_y] and grid[cur_x][cur_y] == 1:
            visited[cur_x][cur_y] = True
            count += 1
            dfs(grid, visited, cur_x, cur_y)


n, m = map(int, input().split())
# 邻接矩阵
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))
# 访问表
visited = [[False] * m for _ in range(n)]

result = 0  # 记录最终结果
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1 and not visited[i][j]:
            count = 1
            visited[i][j] = True
            dfs(grid, visited, i, j)
            result = max(count, result)

print(result)
```

# 岛屿最大面积-广搜版

```python
from collections import deque

position = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 四个方向
count = 0


def bfs(grid, visited, x, y):
    """
    广度优先搜索对陆地进行标记
    """
    global count  # 声明全局变量
    que = deque()
    que.append([x, y])
    while que:
        cur_x, cur_y = que.popleft()
        for i, j in position:
            next_x = cur_x + i
            next_y = cur_y + j
            # 下标越界，跳过
            if next_x < 0 or next_x >= len(grid) or next_y < 0 or next_y >= len(grid[0]):
                continue
            if grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
                visited[next_x][next_y] = True
                count += 1
                que.append([next_x, next_y])


n, m = map(int, input().split())
# 邻接矩阵
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]  # 访问表

result = 0  # 记录最终结果
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1 and not visited[i][j]:
            count = 1
            visited[i][j] = True
            bfs(grid, visited, i, j)
            res = max(result, count)

print(result)
```

# 孤岛的总面积

本题要求找到不靠边的陆地面积，那么我们只要从周边找到陆地然后 通过 dfs或者bfs 将周边靠陆地且相邻的陆地都变成海洋，然后再去重新遍历地图 统计此时还剩下的陆地就可以了。

```python
from collections import deque

# 处理输入
n, m = list(map(int, input().strip()))
g = []
for _ in range(n):
    row = list(map(int, input().strip()))
    g.append(row)

# 定义四个方向、孤岛面积（遍历完边缘后会被重置）
directions = [[0,1], [1,0], [-1,0], [0,-1]]
count = 0

# 广搜
def bfs(r, c):
    global count
    q = deque()
    q.append((r, c))
    g[r][c] = 0
    count += 1

    while q:
        r, c = q.popleft()
        for di in directions:
            next_r = r + di[0]
            next_c = c + di[1]
            if next_c < 0 or next_c >= m or next_r < 0 or next_r >= n:
                continue
            if g[next_r][next_c] == 1:
                q.append((next_r, next_c))
                g[next_r][next_c] = 0
                count += 1


for i in range(n):
    if g[i][0] == 1: bfs(i, 0)
    if g[i][m-1] == 1: bfs(i, m-1)

for i in range(m):
    if g[0][i] == 1: bfs(0, i)
    if g[n-1][i] == 1: bfs(n-1, i)

count = 0
for i in range(n):
    for j in range(m):
        if g[i][j] == 1: bfs(i, j)

print(count)
```

# 沉默孤岛

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/kamacoder/0102.%E6%B2%89%E6%B2%A1%E5%AD%A4%E5%B2%9B.md

思路依然是从地图周边出发，将周边空格相邻的陆地都做上标记，然后在遍历一遍地图，遇到 陆地 且没做过标记的，那么都是地图中间的 陆地 ，全部改成水域就行。

有的录友可能想，我在定义一个 visited 二维数组，单独标记周边的陆地，然后遍历地图的时候同时对 数组board 和 数组visited 进行判断，决定 陆地是否变成水域。

步骤一：深搜或者广搜将地图周边的 1 （陆地）全部改成 2 （特殊标记）

步骤二：将水域中间 1 （陆地）全部改成 水域（0）

步骤三：将之前标记的 2 改为 1 （陆地）

```python

def dfs(grid, x, y):
    grid[x][y] = 2
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # 四个方向
    for dx, dy in directions:
        nextx, nexty = x + dx, y + dy
        # 超过边界
        if nextx < 0 or nextx >= len(grid) or nexty < 0 or nexty >= len(grid[0]):
            continue
        # 不符合条件，不继续遍历
        if grid[nextx][nexty] == 0 or grid[nextx][nexty] == 2:
            continue
        dfs(grid, nextx, nexty)

def main():
    n, m = map(int, input().split())
    grid = [[int(x) for x in input().split()] for _ in range(n)]

    # 步骤一：
    # 从左侧边，和右侧边 向中间遍历
    for i in range(n):
        if grid[i][0] == 1:
            dfs(grid, i, 0)
        if grid[i][m - 1] == 1:
            dfs(grid, i, m - 1)

    # 从上边和下边 向中间遍历
    for j in range(m):
        if grid[0][j] == 1:
            dfs(grid, 0, j)
        if grid[n - 1][j] == 1:
            dfs(grid, n - 1, j)

    # 步骤二、步骤三
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                grid[i][j] = 0
            if grid[i][j] == 2:
                grid[i][j] = 1

    # 打印结果
    for row in grid:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()
```

```python
from collections import deque

n, m = list(map(int, input().split()))
g = []
for _ in range(n):
    row = list(map(int,input().split()))
    g.append(row)
    
directions = [(1,0),(-1,0),(0,1),(0,-1)]
count = 0

def bfs(r,c,mode):
    global count 
    q = deque()
    q.append((r,c))
    count += 1
    
    while q:
        r, c = q.popleft()
        if mode:
            g[r][c] = 2
            
        for di in directions:
            next_r = r + di[0]
            next_c = c + di[1]
            if next_c < 0 or next_c >= m or next_r < 0 or next_r >= n:
                continue
            if g[next_r][next_c] == 1:
                q.append((next_r,next_c))
                if mode:
                    g[r][c] = 2
                    
                count += 1
    

for i in range(n):
    if g[i][0] == 1: bfs(i,0,True)
    if g[i][m-1] == 1: bfs(i, m-1,True)
    
for j in range(m):
    if g[0][j] == 1: bfs(0,j,1)
    if g[n-1][j] == 1: bfs(n-1,j,1)

for i in range(n):
    for j in range(m):
        if g[i][j] == 2:
            g[i][j] = 1
        else:
            g[i][j] = 0
            
for row in g:
    print(" ".join(map(str, row)))

```

# 水流问题

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/kamacoder/0103.%E6%B0%B4%E6%B5%81%E9%97%AE%E9%A2%98.md

```python
def dfs(grid, visited, x, y, n, m):
    if visited[x][y]:
        return

    visited[x][y] = True

    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    for dx, dy in directions:
        next_x = x + dx
        next_y = y + dy

        if not (0 <= next_x < n and 0 <= next_y < m):
            continue
        if grid[x][y] < grid[next_x][next_y]:
            continue

        dfs(grid, visited, next_x, next_y, n, m)


def is_result(grid, x, y, n, m):
    visited = [[False] * m for _ in range(n)]

    dfs(grid, visited, x, y, n, m)

    is_first = any(visited[0][j] for j in range(m)) or any(visited[i][0] for i in range(n))
    is_second = any(visited[n - 1][j] for j in range(m)) or any(visited[i][m - 1] for i in range(n))

    return is_first and is_second


def main():
    n, m = map(int, input().split())

    grid = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if is_result(grid, i, j, n, m):
                print(i, j)


if __name__ == "__main__":
    main()

```

# 建造最大岛屿

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/kamacoder/0104.%E5%BB%BA%E9%80%A0%E6%9C%80%E5%A4%A7%E5%B2%9B%E5%B1%BF.md

第一步：一次遍历地图，得出各个岛屿的面积，并做编号记录。可以使用map记录，key为岛屿编号，value为岛屿面积

第二步：再遍历地图，遍历0的方格（因为要将0变成1），并统计该1（由0变成的1）周边岛屿面积，将其相邻面积相加在一起，遍历所有 0 之后，就可以得出 选一个0变成1 之后的最大面积。

```python
import collections

directions = [[-1, 0], [0, 1], [0, -1], [1, 0]]
area = 0

def dfs(i, j, grid, visited, num):
    global area
    
    if visited[i][j]:
        return

    visited[i][j] = True
    grid[i][j] = num  # 标记岛屿号码
    area += 1
    
    for x, y in directions:
        new_x = i + x
        new_y = j + y
        if (
            0 <= new_x < len(grid)
            and 0 <= new_y < len(grid[0])
            and grid[new_x][new_y] == "1"
        ):
            dfs(new_x, new_y, grid, visited, num)
    

def main():
    global area
    
    N, M = map(int, input().strip().split())
    grid = []
    for i in range(N):
        grid.append(input().strip().split())
    visited = [[False] * M for _ in range(N)]
    rec = collections.defaultdict(int)
    #第一步
    cnt = 2
    for i in range(N):
        for j in range(M):
            if grid[i][j] == "1":
                area = 0
                dfs(i, j, grid, visited, cnt)
                rec[cnt] = area  # 纪录岛屿面积
                cnt += 1
    #第二步
    res = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == "0":
                max_island = 1  # 将水变为陆地，故从1开始计数
                v = set()
                for x, y in directions:
                    new_x = i + x
                    new_y = j + y
                    if (
                        0 <= new_x < len(grid)
                        and 0 <= new_y < len(grid[0])
                        and grid[new_x][new_y] != "0"
                        and grid[new_x][new_y] not in v  # 岛屿不可重复
                    ):
                        max_island += rec[grid[new_x][new_y]]
                        v.add(grid[new_x][new_y])
                res = max(res, max_island)

    if res == 0:
        return max(rec.values())  # 无水的情况
    return res
    
if __name__ == "__main__":
    print(main())
    
############################################################################################    
import collections
directions = [[-1, 0], [0, 1], [0, -1], [1, 0]]

def bfs(i, j, grid, visited, num):
    queue = collections.deque([(i, j)])
    visited[i][j] = True
    grid[i][j] = num
    area = 1

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if (
                0 <= new_x < len(grid)
                and 0 <= new_y < len(grid[0])
                and grid[new_x][new_y] == "1"
                and not visited[new_x][new_y]
            ):
                visited[new_x][new_y] = True
                grid[new_x][new_y] = num
                area += 1
                queue.append((new_x, new_y))

    return area


def main():
    N, M = map(int, input().strip().split())
    grid = [input().strip().split() for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    rec = collections.defaultdict(int)

    cnt = 2
    for i in range(N):
        for j in range(M):
            if grid[i][j] == "1" and not visited[i][j]:
                area = bfs(i, j, grid, visited, cnt)
                rec[cnt] = area
                cnt += 1

    res = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == "0":
                max_island = 1
                v = set()
                for dx, dy in directions:
                    new_x, new_y = i + dx, j + dy
                    if (
                        0 <= new_x < len(grid)
                        and 0 <= new_y < len(grid[0])
                        and grid[new_x][new_y] != "0"
                        and grid[new_x][new_y] not in v
                    ):
                        max_island += rec[grid[new_x][new_y]]
                        v.add(grid[new_x][new_y])
                res = max(res, max_island)

    if res == 0:
        return max(rec.values())
    return res


if __name__ == "__main__":
    print(main())
```

# 字符串接龙

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/kamacoder/0110.%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%8E%A5%E9%BE%99.md

**这里无向图求最短路，广搜最为合适，广搜只要搜到了终点，那么一定是最短的路径**。因为广搜就是以起点中心向四周扩散的搜索。

**本题如果用深搜，会比较麻烦，要在到达终点的不同路径中选则一条最短路**。 而广搜只要达到终点，一定是最短路。

首先题目中并没有给出点与点之间的连线，而是要我们自己去连，条件是字符只能差一个。

所以判断点与点之间的关系，需要判断是不是差一个字符，**如果差一个字符，那就是有链接**。

```python
def judge(s1,s2):
    count=0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            count+=1
    return count==1

if __name__=='__main__':
    n=int(input())
    beginstr,endstr=map(str,input().split())
    if beginstr==endstr:
        print(0)
        exit()
    strlist=[]
    for i in range(n):
        strlist.append(input())
    
    # use bfs
    visit=[False for i in range(n)]
    queue=[[beginstr,1]]
    while queue:
        str,step=queue.pop(0)
        if judge(str,endstr):
            print(step+1)
            exit()
        for i in range(n):   #代表方向 接下来是哪一个
            if visit[i]==False and judge(strlist[i],str):
                visit[i]=True
                queue.append([strlist[i],step+1])
    print(0)
```

关于图，**要知道 怎么构成图 不一定是矩阵的**，要抽象化 如本题。

# 有向图的完全可达

https://github.com/zihao-cpu/leetcode-master/blob/master/problems/kamacoder/0105.%E6%9C%89%E5%90%91%E5%9B%BE%E7%9A%84%E5%AE%8C%E5%85%A8%E5%8F%AF%E8%BE%BE%E6%80%A7.md

```python 
import collections

path = set()  # 纪录 BFS 所经过之节点

def bfs(root, graph):
    global path
    
    que = collections.deque([root])
    while que:
        cur = que.popleft()
        path.add(cur)
        
        for nei in graph[cur]:
            que.append(nei)
        graph[cur] = []
    return

def main():
    N, K = map(int, input().strip().split())
    graph = collections.defaultdict(list)
    for _ in range(K):
        src, dest = map(int, input().strip().split())
        graph[src].append(dest)
    
    bfs(1, graph)
    if path == {i for i in range(1, N + 1)}:
        return 1
    return -1
        

if __name__ == "__main__":
    print(main())

```

```python

def dfs(graph, key, visited):
    for neighbor in graph[key]:
        if not visited[neighbor]:  # Check if the next node is not visited
            visited[neighbor] = True
            dfs(graph, neighbor, visited)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    m = int(data[1])
    
    graph = [[] for _ in range(n + 1)]
    index = 2
    for _ in range(m):
        s = int(data[index])
        t = int(data[index + 1])
        graph[s].append(t)
        index += 2

    visited = [False] * (n + 1)
    visited[1] = True  # Process node 1 beforehand
    dfs(graph, 1, visited)

    for i in range(1, n + 1):
        if not visited[i]:
            print(-1)
            return
    
    print(1)

if __name__ == "__main__":
    main()


def dfs(graph, key, visited):
    for neighbor in graph[key]:
        if not visited[neighbor]:  # Check if the next node is not visited
            visited[neighbor] = True
            dfs(graph, neighbor, visited)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    m = int(data[1])
    
    graph = [[] for _ in range(n + 1)]
    index = 2
    for _ in range(m):
        s = int(data[index])
        t = int(data[index + 1])
        graph[s].append(t)
        index += 2

    visited = [False] * (n + 1)
    visited[1] = True  # Process node 1 beforehand
    dfs(graph, 1, visited)

    for i in range(1, n + 1):
        if not visited[i]:
            print(-1)
            return
    
    print(1)

if __name__ == "__main__":
    main()

```

