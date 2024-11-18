import random
import time
import matplotlib.pyplot as plt
import sys
from archive.Deliverable1 import knapsack_bottom_up, knapsack_top_down

# Increase the recursion limit
sys.setrecursionlimit(2000)

def generate_random_input(n, W):
    weights = [random.randint(1, W) for _ in range(n)]
    values = [random.randint(1, 100) for _ in range(n)]
    return weights, values

def measure_runtime(algorithm, weights, values, capacity):
    start_time = time.time()
    result = algorithm(weights, values, capacity)
    end_time = time.time()
    return end_time - start_time, result

def plot_performance():
    n_values = [10, 50, 100, 500, 1000]
    W = 100
    bottom_up_times_n = []
    top_down_times_n = []

    for n in n_values:
        weights, values = generate_random_input(n, W)
        bottom_up_time, _ = measure_runtime(knapsack_bottom_up, weights, values, W)
        top_down_time, _ = measure_runtime(knapsack_top_down, weights, values, W)
        bottom_up_times_n.append(bottom_up_time)
        top_down_times_n.append(top_down_time)

    W_values = [50, 100, 500, 1000]
    n = 100
    bottom_up_times_W = []
    top_down_times_W = []

    for W in W_values:
        weights, values = generate_random_input(n, W)
        bottom_up_time, _ = measure_runtime(knapsack_bottom_up, weights, values, W)
        top_down_time, _ = measure_runtime(knapsack_top_down, weights, values, W)
        bottom_up_times_W.append(bottom_up_time)
        top_down_times_W.append(top_down_time)

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.plot(n_values, bottom_up_times_n, label='Bottom-Up', marker='o')
    plt.plot(n_values, top_down_times_n, label='Top-Down', marker='x')
    plt.xlabel('Number of Items (n)')
    plt.ylabel('Runtime (seconds)')
    plt.title('Runtime vs Number of Items (Fixed W)')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(W_values, bottom_up_times_W, label='Bottom-Up', marker='o')
    plt.plot(W_values, top_down_times_W, label='Top-Down', marker='x')
    plt.xlabel('Capacity (W)')
    plt.ylabel('Runtime (seconds)')
    plt.title('Runtime vs Capacity (Fixed n)')
    plt.legend()

    plt.suptitle('Knapsack Problem: Performance Comparison')
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

# Example usage
plot_performance()