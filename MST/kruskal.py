class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    #查找元素所在集合的根节点
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            self.parent[rootY] = rootX
            return True
        return False
   #合并两个集合
#unionfind是一个类，这个类有两个方法，一个是find，一个是union，find方法是查找元素所在集合的根节点，union方法是合并两个集合
def kruskal(n, edges):
    # 按照边的权重进行排序
    edges.sort(key=lambda x: x[2])

    uf = UnionFind(n)
    mst = []
    total_weight = 0

    # 遍历所有边
    for u, v, weight in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight


# 示例：图的边 (u, v, weight)
edges = [
    (0, 1, 1),
    (0, 2, 3),
    (1, 2, 1),
    (1, 3, 6),
    (2, 3, 2)
]
n = 4  # 图中的节点数
# 输出的结果是将所有的边按照权重进行排序，然后从小到大进行遍历，如果两个节点不在同一个集合中，那么就将这两个节点合并到一个集合中，然后将这条边加入到最小生成树中
# edge是图的边，n是图的节点数 通过kruskal算法找出这五个边中的可以构成最小生成树的边，其实就是挑选出来的边的权重和是最小的 通过并查集来实现
mst, total_weight = kruskal(n, edges)

print("最小生成树的边:", mst)
print("最小生成树的权重和:", total_weight)
