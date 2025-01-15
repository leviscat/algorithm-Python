def knapsack_complete(weights, values, W):
    n = len(weights)
    dp = [0] * (W + 1)
    for w in range(1, W + 1):
        for i in range(n):
            if weights[i] <= w:
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[W]
weights = [1, 2, 3]
values = [6, 10, 12]
W = 5
print(knapsack_complete(weights, values, W))
def knapsack_complete_2(weights, values, W):
    n = len(weights)
    dp = [0] * (W + 1)

    for i in range(n):
        for w in range(weights[i], W + 1):  # 从小到大更新
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[W]

# 示例
weights = [1, 2, 3]
values = [6, 10, 12]
W = 5
print(knapsack_complete_2(weights, values, W))
