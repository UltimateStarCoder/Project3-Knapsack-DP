from tabulate import tabulate

# m = 2 # rows
# n = 7 # columns

# item = [1, 2, 3, 4]
# weight = [2, 1, 3, 2]
# value = [12, 10, 20, 15]
# capacity = 5

# memo = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
# print(tabulate(memo, tablefmt="fancy_grid"))

# Botton-up DP Table
def knapsack_bottom_up(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    print("Bottom-Up DP Table:")
    print(tabulate(dp, tablefmt="fancy_grid"))
    return dp[n][capacity]

# Example usage
# weights = [2, 1, 3, 2]
# values = [12, 10, 20, 15]
# capacity = 5

weights = [7, 3, 4, 10]
values = [100, 12, 40, 25]
capacity = 7
print("Maximum value (Bottom-Up):", knapsack_bottom_up(weights, values, capacity))

print()
print()

# Top-Down DP Table
def knapsack_top_down(weights, values, capacity):
    n = len(weights)
    memo = [[-1 for _ in range(capacity + 1)] for _ in range(n + 1)]

    def knapsack_recursive(n, capacity):
        if n == 0 or capacity == 0:
            return 0
        if memo[n][capacity] != -1:
            return memo[n][capacity]
        if weights[n - 1] > capacity:
            memo[n][capacity] = knapsack_recursive(n - 1, capacity)
        else:
            memo[n][capacity] = max(knapsack_recursive(n - 1, capacity),
                                    knapsack_recursive(n - 1, capacity - weights[n - 1]) + values[n - 1])
        return memo[n][capacity]

    max_value = knapsack_recursive(n, capacity)
    print("Top-Down DP Table:")
    print(tabulate(memo, tablefmt="fancy_grid"))
    return max_value

# Example usage
# weights = [2, 1, 3, 2]
# values = [12, 10, 20, 15]
# capacity = 5

weights = [7, 3, 4, 10]
values = [100, 12, 40, 25]
capacity = 7
print("Maximum value (Top-Down):", knapsack_top_down(weights, values, capacity))