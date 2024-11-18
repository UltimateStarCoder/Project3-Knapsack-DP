from tabulate import tabulate
import time

# Bottom-up DP Table
def knapsack_bottom_up(weights, values, capacity):
    start_time = time.time()  # Start time
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    end_time = time.time()  # End time
    elapsed_time = end_time - start_time  # Calculate elapsed time

    if __name__ == "__main__":
        print("Bottom-Up DP Table:")
        print(tabulate(dp, tablefmt="fancy_grid"))
    return dp[n][capacity], elapsed_time

# Top-Down DP Table
def knapsack_top_down(weights, values, capacity, n):
    start_time = time.time()  # Start time
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
    end_time = time.time()  # End time
    elapsed_time = end_time - start_time  # Calculate elapsed time

    if __name__ == "__main__":
        print("Top-Down DP Table:")
        print(tabulate(memo, tablefmt="fancy_grid"))
    return max_value, elapsed_time

if __name__ == "__main__":
    Weights = [2, 1, 3, 2]
    Values = [12, 10, 20, 15]
    Capacity = 5

    answer, elapsed_time = knapsack_bottom_up(Weights, Values, Capacity)
    print("Maximum value (Bottom-Up):", answer)
    # print("Elapsed time (Bottom-Up):", elapsed_time, "seconds")

    print()
    print()

    answer1, elapsed_time1 = knapsack_top_down(Weights, Values, Capacity, len(Weights))
    print("Maximum value (Top-Down):", answer1)
    # print("Elapsed time (Top-Down):", elapsed_time1, "seconds")