def floyd_warshall(graph, V):
    # 初始化最短路径矩阵
    dist = [[float('inf')] * V for _ in range(V)]

    # 设置自己到自己的距离为 0
    for i in range(V):
        dist[i][i] = 0

    # 初始化边的权重
    for u in range(V):
        for v, weight in graph.get(u, []):
            dist[u][v] = weight

    # 动态规划更新最短路径
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


# 示例：图的邻接表表示 (u, [(v, weight), (v2, weight2)])
graph = {
    0: [(1, 3), (2, 5)],
    1: [(2, 1), (3, 7)],
    2: [(3, 2)],
    3: []
}

V = 4  # 图中的节点数
dist = floyd_warshall(graph, V)

# 输出所有节点对的最短路径
for i in range(V):
    for j in range(V):
        if dist[i][j] == float('inf'):
            print(f"从节点 {i} 到节点 {j} 没有路径")
        else:
            print(f"从节点 {i} 到节点 {j} 的最短路径长度是 {dist[i][j]}")
