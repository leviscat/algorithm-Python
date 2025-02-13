import heapq

def prim(n, graph):
    mst = []
    total_weight = 0
    visited = [False] * n
    min_heap = [(0, 0)]  # (权重, 节点)

    while min_heap:
        weight, u = heapq.heappop(min_heap)

        if visited[u]:
            continue

        visited[u] = True
        total_weight += weight

        # 将当前节点的所有邻接边加入优先队列
        for v, edge_weight in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (edge_weight, v))
                mst.append((u, v, edge_weight))

    return mst, total_weight

# 示例：图的邻接表表示 (u, [(v, weight), (v2, weight2)])
graph = {
    0: [(1, 1), (2, 3)],
    1: [(0, 1), (2, 1), (3, 6)],
    2: [(0, 3), (1, 1), (3, 2)],
    3: [(1, 6), (2, 2)]
}
n = 4  # 图中的节点数

mst, total_weight = prim(n, graph)

print("最小生成树的边:", mst)
print("最小生成树的权重和:", total_weight)
