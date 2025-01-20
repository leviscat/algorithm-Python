import heapq  # 使用堆来加速算法
#像病毒一样，一直找最薄弱的地方，然后找这个地方的邻居，然后找邻居的邻居，是一种贪心算法
def dijkstra(graph, start):
    """
    :param graph: 图的邻接表表示 {node: [(neighbor, weight), ...]}
    :param start: 起始节点
    :return: 最短路径长度字典 {node: shortest_distance}
    """
    # Step 1: 初始化距离和堆
    dist = {node: float('inf') for node in graph}  # 距离初始化为无穷大
    dist[start] = 0  # 起点到自己的距离是 0
    priority_queue = [(0, start)]  # 堆，存储 (当前最短路径长度, 当前节点)

    while priority_queue:
        # Step 2: 取出堆顶元素，最短路径长度最小的节点
        current_dist, current_node = heapq.heappop(priority_queue)

        # 如果当前节点的距离已经大于已知最短距离，则跳过
        if current_dist > dist[current_node]:
            continue

        # Step 3: 遍历当前节点的邻居，更新邻居的最短距离
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight

            # 如果通过当前节点到邻居的路径更短，则更新距离
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))  # 将更新后的节点加入堆中

    return dist

# 示例图：邻接表表示
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# 从节点 'A' 出发计算最短路径
start_node = 'A'
shortest_paths = dijkstra(graph, start_node)

print(f"从 {start_node} 出发到其他节点的最短路径：")
for node, dist in shortest_paths.items():
    print(f"到 {node} 的最短路径长度: {dist}")
