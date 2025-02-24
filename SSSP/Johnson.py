import heapq


# Bellman-Ford算法，用于计算每个节点到源节点的最短路径
def bellman_ford(graph, start, V):
    dist = [float('inf')] * V
    dist[start] = 0
    for _ in range(V - 1):
        for u in range(V):
            for v, w in graph[u]:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
    return dist


# Dijkstra算法，用于计算单源最短路径
def dijkstra(graph, start, V):
    dist = [float('inf')] * V
    dist[start] = 0
    pq = [(0, start)]  # (distance, node)
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist


# Johnson算法
def johnson(graph, V):
    # Step 1: Add a new node q to the graph
    new_node = V
    new_graph = [edges[:] for edges in graph] + [[]]

    # Add zero-weight edges from the new node q to all other nodes
    for i in range(V):
        new_graph[new_node].append((i, 0))

    # Step 2: Run Bellman-Ford from the new node q
    h = bellman_ford(new_graph, new_node, V + 1)

    # If there is a negative-weight cycle
    if any(d == float('inf') for d in h):
        return None

    # Step 3: Reweight the graph
    reweighted_graph = [[] for _ in range(V)]
    for u in range(V):
        for v, w in graph[u]:
            reweighted_weight = w + h[u] - h[v]
            reweighted_graph[u].append((v, reweighted_weight))

    # Step 4: Run Dijkstra for each node
    all_pairs_shortest_paths = []
    for s in range(V):
        dist = dijkstra(reweighted_graph, s, V)
        # Step 5: Restore the original distances
        result = [d + h[v] - h[s] for v, d in enumerate(dist)]
        all_pairs_shortest_paths.append(result)

    return all_pairs_shortest_paths


# 示例图
graph = [
    [(1, 2), (2, 4)],  # Node 0 has edges to 1 (weight 2) and 2 (weight 4)
    [(2, 1)],  # Node 1 has an edge to 2 (weight 1)
    [(3, 1)],  # Node 2 has an edge to 3 (weight 1)
    []  # Node 3 has no outgoing edges
]

V = len(graph)  # Number of nodes in the graph

shortest_paths = johnson(graph, V)
print(shortest_paths)
