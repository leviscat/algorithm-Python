from collections import deque


def bfs(graph, start):
    # 初始化队列和访问集合
    queue = deque([start])
    visited = set([start])

    while queue:
        node = queue.popleft()  # 从队列中取出一个节点
        print(node)  # 访问该节点

        # 遍历邻居节点
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# 图的表示（邻接表）
graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2]
}

# 从节点 0 开始执行 BFS
bfs(graph, 0)
#先访问0，然后访问1，然后访问3，然后访问2 是向外扩展的，先访问的是距离起点最近的节点 不是向下扩展的