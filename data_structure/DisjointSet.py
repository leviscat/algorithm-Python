class DisjointSet:
    def __init__(self, n):
        # 初始化每个元素的父节点为自己，且秩（树的高度）为0
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    # 查找元素所在集合的根节点
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 路径压缩
        return self.parent[x]

    # 合并两个集合
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # 按秩合并
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

# 使用例子
ds = DisjointSet(5)
ds.union(0, 1)
ds.union(1, 2)
ds.union(3, 4)

print(ds.find(0))  # 输出 0, 0 和 1, 2 是同一个集合
print(ds.find(2))  # 输出 0
print(ds.find(4))
ds.union(2, 4)
print(ds.find(4))  # 输出 0, 4 和 2 现在是同一个集合
