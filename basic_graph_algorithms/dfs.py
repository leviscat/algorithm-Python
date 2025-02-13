def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    # 访问当前节点
    print(start, end=' ')
    visited.add(start)

    # 递归访问未访问的邻居节点
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# 调用 DFS，起始节点为 0
graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1],
    3: [0, 2]
}

dfs(graph, 0)
#先访问0，然后访问0的邻居1，然后访问1的邻居2，然后访问0的邻居3，然后访问3的邻居2，是向下递归的