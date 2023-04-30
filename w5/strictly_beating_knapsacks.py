from typing import List

def solve(values, weights, weight_limit):
    n = len(values)
    dp = [[0] * (int(weight_limit) + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(int(weight_limit) + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - int(weights[i - 1])])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][int(weight_limit)]

# Example
values = [200, 300, 400]
weights = [2, 4, 5]
weight_limit = 6
print(solve(values, weights, weight_limit))  # Output: 500