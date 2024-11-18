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

def plot_pseudopolynomial_nature():
    W_values = [10, 50, 100, 500, 1000]
    n = 30
    bottom_up_times = []
    top_down_times = []

    for W in W_values:
        weights, values = generate_random_input(n, W, low_weight=True)
        bottom_up_time, _ = measure_runtime(knapsack_bottom_up, weights, values, W)
        top_down_time, _ = measure_runtime(knapsack_top_down, weights, values, W)
        bottom_up_times.append(bottom_up_time)
        top_down_times.append(top_down_time)

    W_representation_sizes = [len(bin(W)[2:]) for W in W_values]

    plt.figure(figsize=(10, 5))
    plt.plot(W_representation_sizes, bottom_up_times, label='Bottom-Up (Low Weight)', marker='o')
    plt.plot(W_representation_sizes, top_down_times, label='Top-Down (Low Weight)', marker='x')
    plt.xlabel('Size of W Representation')
    plt.ylabel('Runtime (seconds)')
    plt.title('Knapsack Problem: Runtime vs Size of W Representation (Low Weight)')
    plt.legend()
    plt.show()

# Example usage
plot_pseudopolynomial_nature()