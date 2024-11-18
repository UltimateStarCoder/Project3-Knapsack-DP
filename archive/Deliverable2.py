import random
import time
import matplotlib.pyplot as plt
from tabulate import tabulate
from archive.Deliverable1 import knapsack_bottom_up, knapsack_top_down

# Input Generation
def generate_random_input(n, W):
    weights = [random.randint(1, W) for _ in range(n)]
    values = [random.randint(1, 100) for _ in range(n)]
    return weights, values

# Example usage
n = 10
W = 50
weights, values = generate_random_input(n, W)
print("Weights:", weights)
print("Values:", values)


# Algorithm Performance Measurement
def measure_runtime(algorithm, weights, values, capacity):
    start_time = time.time()
    result = algorithm(weights, values, capacity)
    end_time = time.time()
    return end_time - start_time, result

# Example usage
weights, values = generate_random_input(10, 50)
capacity = 50
runtime, result = measure_runtime(knapsack_bottom_up, weights, values, capacity)
print("Runtime (Bottom-Up):", runtime, "Result:", result)
runtime, result = measure_runtime(knapsack_top_down, weights, values, capacity)
print("Runtime (Top-Down):", runtime, "Result:", result)


# Plot Creation
def plot_performance():
    n_values = [10, 20, 30, 40, 50]
    W = 50
    bottom_up_times = []
    top_down_times = []

    for n in n_values:
        weights, values = generate_random_input(n, W)
        bottom_up_time, _ = measure_runtime(knapsack_bottom_up, weights, values, W)
        top_down_time, _ = measure_runtime(knapsack_top_down, weights, values, W)
        bottom_up_times.append(bottom_up_time)
        top_down_times.append(top_down_time)

    plt.figure(figsize=(10, 5))
    plt.plot(n_values, bottom_up_times, label='Bottom-Up', marker='o')
    plt.plot(n_values, top_down_times, label='Top-Down', marker='x')
    plt.xlabel('Number of Items (n)')
    plt.ylabel('Runtime (seconds)')
    plt.title('Knapsack Problem: Runtime vs Number of Items')
    plt.legend()
    plt.show()

    W_values = [10, 20, 30, 40, 50]
    n = 30
    bottom_up_times = []
    top_down_times = []

    for W in W_values:
        weights, values = generate_random_input(n, W)
        bottom_up_time, _ = measure_runtime(knapsack_bottom_up, weights, values, W)
        top_down_time, _ = measure_runtime(knapsack_top_down, weights, values, W)
        bottom_up_times.append(bottom_up_time)
        top_down_times.append(top_down_time)

    plt.figure(figsize=(10, 5))
    plt.plot(W_values, bottom_up_times, label='Bottom-Up', marker='o')
    plt.plot(W_values, top_down_times, label='Top-Down', marker='x')
    plt.xlabel('Capacity (W)')
    plt.ylabel('Runtime (seconds)')
    plt.title('Knapsack Problem: Runtime vs Capacity')
    plt.legend()
    plt.show()

# Example usage
plot_performance()