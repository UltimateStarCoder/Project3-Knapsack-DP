import random
import time
import matplotlib.pyplot as plt

def generate_random_input(n, W, low_weight=False):
    if low_weight:
        weights = [random.randint(1, 10) for _ in range(n)]
    else:
        weights = [random.randint(1, W) for _ in range(n)]
    values = [random.randint(1, 100) for _ in range(n)]
    return weights, values

def measure_runtime(algorithm, weights, values, capacity):
    start_time = time.time()
    result = algorithm(weights, values, capacity)
    end_time = time.time()
    return end_time - start_time, result

def knapsack_bottom_up(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]

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
    return knapsack_recursive(n, capacity)

def plot_performance():
    n_values = [10, 20, 30, 40, 50]
    W = 50
    bottom_up_times_low_weight = []
    top_down_times_low_weight = []

    for n in n_values:
        weights, values = generate_random_input(n, W, low_weight=True)
        bottom_up_time, _ = measure_runtime(knapsack_bottom_up, weights, values, W)
        top_down_time, _ = measure_runtime(knapsack_top_down, weights, values, W)
        bottom_up_times_low_weight.append(bottom_up_time)
        top_down_times_low_weight.append(top_down_time)

    plt.figure(figsize=(10, 5))
    plt.plot(n_values, bottom_up_times_low_weight, label='Bottom-Up (Low Weight)', marker='o')
    plt.plot(n_values, top_down_times_low_weight, label='Top-Down (Low Weight)', marker='x')
    plt.xlabel('Number of Items (n)')
    plt.ylabel('Runtime (seconds)')
    plt.title('Knapsack Problem: Runtime vs Number of Items (Low Weight)')
    plt.legend()
    plt.show()

    W_values = [10, 20, 30, 40, 50]
    n = 30
    bottom_up_times_low_weight = []
    top_down_times_low_weight = []

    for W in W_values:
        weights, values = generate_random_input(n, W, low_weight=True)
        bottom_up_time, _ = measure_runtime(knapsack_bottom_up, weights, values, W)
        top_down_time, _ = measure_runtime(knapsack_top_down, weights, values, W)
        bottom_up_times_low_weight.append(bottom_up_time)
        top_down_times_low_weight.append(top_down_time)

    plt.figure(figsize=(10, 5))
    plt.plot(W_values, bottom_up_times_low_weight, label='Bottom-Up (Low Weight)', marker='o')
    plt.plot(W_values, top_down_times_low_weight, label='Top-Down (Low Weight)', marker='x')
    plt.xlabel('Capacity (W)')
    plt.ylabel('Runtime (seconds)')
    plt.title('Knapsack Problem: Runtime vs Capacity (Low Weight)')
    plt.legend()
    plt.show()

# Example usage
plot_performance()