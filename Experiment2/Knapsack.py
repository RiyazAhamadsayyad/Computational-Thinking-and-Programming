#Exp 2
def knapsack(w, v, W):
    n = len(w)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(W + 1):
            if w[i - 1] <= j:
                dp[i][j] = max(
                    v[i - 1] + dp[i - 1][j - w[i - 1]],
                    dp[i - 1][j]
                )
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][W]


weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

print("Maximum Profit:", knapsack(weights, values, capacity))
