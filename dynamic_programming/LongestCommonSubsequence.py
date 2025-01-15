def longest_common_subsequence(X, Y):
    m, n = len(X), len(Y)
    # 使用一个数组来存储当前和上一行
    dp = [0] * (n + 1)
    for i in range(1, m + 1):
        prev = 0  # 表示 dp[i-1][j-1]
        for j in range(1, n + 1):
            temp = dp[j]  # 保存当前 dp[j] 的值（即 dp[i-1][j]）
            if X[i - 1] == Y[j - 1]:
                dp[j] = prev + 1
            else:
                dp[j] = max(dp[j], dp[j - 1])
            prev = temp  # 更新 prev 为下一步的 dp[i-1][j-1]
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])  # 这个字符是 LCS 的一部分
            i -= 1
            j -= 1
        elif dp[j] == dp[j - 1]:  # 如果上一个字符是 LCS 的一部分，往上一行走
            j -= 1
        else:  # 否则，往上一列走
            i -= 1
    #返回两个参数
    return dp[n], "".join(reversed(lcs))
X = "AGGTAB"
Y = "GXTXAYB"
result, lcs = longest_common_subsequence(X, Y)
#为什么输出的是数组，但是结果是一个数字呢？
#print函数
print(result)  # 输出 4
print(lcs)  # 输出 "GTAB"