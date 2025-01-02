class Edge():
    def __init__(self,l,r,val):
        self.left=l
        self.right=r
        self.value=val
'''
并查集
class  UnionFind:
    def __init__(self,size):
        self.parent=list(range(size+1))
    def find(self,u):
        if self.parent[u]!=u:
            self.parent[u]=self.find(self.parent[u])
        return self.parent[u]

    def union(self,u,v):
        root_u=self.find(u)
        root_v=self.find(v)
        if root_u!=root_v:
            self.parent[root_u]=root_v 

    def is_same(self,u,v):
        return self.find(u)==self.find(v)
'''
n=10001
parent=list(n)


def init():
    global parent
    parent=list(range(n))
def find(u):
    if parent[u]!=u:
        parent[u]=find(parent[u])
    return parent[u]

def union(u,v):
    root_u=find(u)
    root_v=find(v)
    if root_u!=root_v:
        parent[root_u]=root_v 

def is_same(u,v):
    return find(u)==find(v)
#先对边排序， 然后依据判断：边的两个节点在不在同一个集合中（并查集），如果不在则加入 否则不加入
def kruskal(v,edges):
    edges.sort(key=lambda edge:edge.val)
    init()
    result_val=0
    for edge in edges:
        x=find(edge.l)
        y=find(edge.r)
        if x!=y:
            result_val+=edge.val
            union(x,y)
    return result_val

