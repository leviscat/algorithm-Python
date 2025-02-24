from collections import deque


# 广度优先搜索(BFS)寻找增广路径
def bfs(capacity, source, sink, parent):
    visited = [False] * len(capacity)
    queue = deque([source])
    visited[source] = True

    while queue:
        u = queue.popleft()

        for v in range(len(capacity)):
            # 如果节点v没有被访问且容量大于0
            if not visited[v] and capacity[u][v] > 0:
                # 记录父节点，用于追溯路径
                parent[v] = u
                if v == sink:
                    return True
                queue.append(v)
                visited[v] = True
    return False


# Edmonds-Karp实现最大流
def edmonds_karp(capacity, source, sink):
    parent = [-1] * len(capacity)
    max_flow = 0

    # 不断寻找增广路径
    while bfs(capacity, source, sink, parent):
        # 找到路径中的瓶颈容量
        path_flow = float('Inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s])
            s = parent[s]

        # 更新残余图
        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow  # 减少正向边的容量
            capacity[v][u] += path_flow  # 增加反向边的容量
            v = parent[v]

        max_flow += path_flow

    return max_flow


# 示例图：容量矩阵
#  0 -> 1 (容量10)
#  0 -> 2 (容量10)
#  1 -> 2 (容量2)
#  1 -> 3 (容量4)
#  2 -> 3 (容量9)
#  3 -> 4 (容量10)

capacity = [
    [0, 10, 10, 0, 0],  # 0到其他节点的容量
    [0, 0, 2, 4, 0],  # 1到其他节点的容量
    [0, 0, 0, 9, 0],  # 2到其他节点的容量
    [0, 0, 0, 0, 10],  # 3到其他节点的容量
    [0, 0, 0, 0, 0]  # 4到其他节点的容量
]

source = 0
sink = 4

max_flow = edmonds_karp(capacity, source, sink)
print(f"最大流量是: {max_flow}")
