from collections import deque

#Kahn 算法利用图的 入度（即指向某个节点的边数）来实现拓扑排序
def topological_sort_kahn(graph):
    # Step 1: 计算每个节点的入度
    in_degree = {node: 0 for node in graph}
    #语法是{key:value for key in iterable} 得到的是一个字典
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # Step 2: 入度为 0 的节点入队列
    queue = deque([node for node in graph if in_degree[node] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        # Step 3: 更新邻居的入度
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 4: 检查是否存在环
    if len(result) == len(graph):
        return result  # 返回拓扑排序结果
    else:
        return "图中存在环，无法进行拓扑排序"


# 示例图
graph = {
    "A": ["C", "D"],
    "B": ["D"],
    "C": ["E"],
    "D": ["E"],
    "E": []
}

print(topological_sort_kahn(graph))
