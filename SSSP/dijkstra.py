import heapq


def dijkstra(graph, start, V):
    distances = {node: float('inf') for node in range(V)}
    distances[start] = 0
    priority_queue = [(0, start)]  # (距离, 节点)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.get(current_node, []):
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def all_pairs_shortest_paths(graph, V):
    all_distances = {}
    for node in range(V):
        all_distances[node] = dijkstra(graph, node, V)
    return all_distances


# 示例图：图的邻接表表示 (u, [(v, weight), (v2, weight2)])
graph = {
    0: [(1, 3), (2, 5)],
    1: [(2, 1), (3, 7)],
    2: [(3, 2)],
    3: []
}

V = 4  # 图中的节点数
distances = all_pairs_shortest_paths(graph, V)

# 输出所有节点对的最短路径
for i in range(V):
    for j in range(V):
        if distances[i][j] == float('inf'):
            print(f"从节点 {i} 到节点 {j} 没有路径")
        else:
            print(f"从节点 {i} 到节点 {j} 的最短路径长度是 {distances[i][j]}")
