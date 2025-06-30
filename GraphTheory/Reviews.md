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

