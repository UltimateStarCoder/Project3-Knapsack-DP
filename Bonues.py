from tabulate import tabulate
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    print("DP Table:")
    print(tabulate(dp, tablefmt="fancy_grid"))
    return dp[n][capacity]

# Example usage:
weights = [2, 1, 3, 2]
values =  [12, 10, 20, 15]
capacity = 5
print(knapsack(weights, values, capacity)) 