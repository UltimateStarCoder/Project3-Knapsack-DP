import random
import time
import matplotlib.pyplot as plt
from archive.Deliverable1 import knapsack_bottom_up, knapsack_top_down

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

def plot_performance():
    n_values = [10, 20, 30, 40, 50]
    W_values = [10, 50, 100, 500, 1000]
    
    bottom_up_times_unique = []
    top_down_times_unique = []
    bottom_up_times_low_weight = []
    top_down_times_low_weight = []

    for W in W_values:
        weights, values = generate_random_input(30, W)
        bottom_up_time, _ = measure_runtime(knapsack_bottom_up, weights, values, W)
        top_down_time, _ = measure_runtime(knapsack_top_down, weights, values, W)
        bottom_up_times_unique.append(bottom_up_time)
        top_down_times_unique.append(top_down_time)

        weights, values = generate_random_input(30, W, low_weight=True)
        bottom_up_time, _ = measure_runtime(knapsack_bottom_up, weights, values, W)
        top_down_time, _ = measure_runtime(knapsack_top_down, weights, values, W)
        bottom_up_times_low_weight.append(bottom_up_time)
        top_down_times_low_weight.append(top_down_time)

    plt.figure(figsize=(12, 6))
    plt.plot(W_values, bottom_up_times_unique, label='Bottom-Up (Unique)', marker='o')
    plt.plot(W_values, top_down_times_unique, label='Top-Down (Unique)', marker='x')
    plt.plot(W_values, bottom_up_times_low_weight, label='Bottom-Up (Low Weight)', marker='o', linestyle='--')
    plt.plot(W_values, top_down_times_low_weight, label='Top-Down (Low Weight)', marker='x', linestyle='--')
    plt.xlabel('Capacity (W)')
    plt.ylabel('Runtime (seconds)')
    plt.title('Knapsack Problem: Runtime vs Capacity (Unique vs Low Weight)')
    plt.legend()
    plt.show()

# Example usage
plot_performance()