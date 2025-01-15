def matrix_chain_order(p):
    n = len(p) - 1  # 矩阵链的数量
    dp = [[0] * n for _ in range(n)]  # dp[i][j] 表示从矩阵 i 到矩阵 j 的最小标量乘法次数

    # l 是链的长度
    for l in range(2, n + 1):  # l 为链的长度，从2到n
        for i in range(n - l + 1):
            j = i + l - 1
            dp[i][j] = float('inf')  # 初始化为一个非常大的数
            # k 从 i 到 j-1 遍历，找到最优分割点
            for k in range(i, j):
                #标量乘法次数=p×q×r p为第一个矩阵的行数，q为第一个矩阵的列数，r为第二个矩阵的列数
                q = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                dp[i][j] = min(dp[i][j], q)

    return dp[0][n - 1]  # 返回从矩阵 1 到 矩阵 n 的最小标量乘法次数


# 示例使用
p = [30, 35, 15, 5, 10, 20, 25]
# p 表示矩阵的维度链：30x35, 35x15, 15x5, 5x10, 10x20, 20x25
print("最小标量乘法次数:", matrix_chain_order(p))
