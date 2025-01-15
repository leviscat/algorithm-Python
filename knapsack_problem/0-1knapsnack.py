#动态规划解决
#转移方程是dp[w]=max(dp[w],dp[w-wt[i]]+val[i])
def knapsack_01_optimized(W, weights, val):
    n = len(weights)
    dp = [0] * (W + 1)
    #前i个物品，背包容量为w时的最大价值
    for i in range(1, n + 1):
        for w in range(W, weights[i - 1] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i - 1]] + val[i - 1])
    return dp[W]

def knapsack_01(weights, values, W):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
#前i个物品，背包容量为w时的最大价值
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] > w:  # 当前物品无法装入
                dp[i][w] = dp[i - 1][w]
            else:  # 选择是否装入
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])

    return dp[n][W]
