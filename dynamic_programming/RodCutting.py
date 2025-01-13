#给定一根长度为 n 的钢条，以及一个长度与价格的映射数组 p[]，其中 p[i] 表示长度为 i 的钢条的单价。
#你需要通过切割钢条，将其分割成若干段（可以不切割），使得钢条的总销售价值最大。
#例如，长度为 8 的钢条，单价数组为 p = [0, 1, 5, 8, 9, 10, 17, 17, 20]，最大价值为 22，分割方案为 2, 6。
#请实现函数 max_value(n, p)，输入一个整数 n 和一个整数数组 p，返回一个整数，表示最大价值。
#提示：可以使用动态规划，设 dp[i] 表示长度为 i 的钢条的最大价值。
#动态规划的状态转移方程为：dp[i] = max(dp[i], dp[j] + dp[i - j])，其中 1 <= j <= i。
#动态规划的边界条件为：dp[0] = 0。
def rod_cutting(prices, n):
    dp = [0] * (n + 1)  # dp[i] 表示长度为 i 的钢条的最大价值
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if dp[i] < prices[j - 1] + dp[i - j]:
                dp[i] = prices[j - 1] + dp[i - j]  # 更新最大收益
    return dp[n]
#写一个9*9乘法表函数
def multiplication_table():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f"{j} * {i} = {i * j}", end="  ")
        print()
prices = [1, 5, 8, 9, 10, 17, 17, 20]
n = 8
print(rod_cutting(prices, n))  # 22

