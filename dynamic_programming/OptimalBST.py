def optimal_bst(p):
    n = len(p)

    # e[i][j] 表示从 k_i 到 k_j 的最小搜索代价
    e = [[0] * (n + 1) for _ in range(n + 1)]

    # w[i][j] 表示从 k_i 到 k_j 的访问频率总和
    w = [[0] * (n + 1) for _ in range(n + 1)]

    # root[i][j] 用来存储构建最优二叉搜索树时根的索引
    root = [[0] * (n + 1) for _ in range(n + 1)]

    # 初始化 w[i][i] 为 p[i]，表示一个单节点的子树
    for i in range(n):
        w[i][i] = p[i]

    # 填充 e 和 w 数组
    for length in range(2, n + 1):  # 子树的长度从2到n
        for i in range(n - length + 1):
            j = i + length - 1
            w[i][j] = w[i][j - 1] + p[j]
            # 计算 e[i][j]
            e[i][j] = float('inf')
            for r in range(i, j + 1):
                cost = e[i][r - 1] + e[r + 1][j] + w[i][j]
                if cost < e[i][j]:
                    e[i][j] = cost
                    root[i][j] = r  # 更新根节点

    # 返回最小搜索代价和最优根节点
    return e[0][n - 1], root


# 示例：访问频率 p = [3, 1, 5, 2]
p = [3, 1, 5, 2]
min_cost, root = optimal_bst(p)
print(f"最小搜索代价: {min_cost}")
print(f"根节点信息: {root}")
