import random
import time
import matplotlib.pyplot as plt
from D1v2 import knapsack_bottom_up, knapsack_top_down

random.seed(42)
W_values = [10, 50, 100, 500, 1000]  # Different capacities to test
n = 30  # Fixed number of items

bottom_up_times = []
top_down_times = []

for W in W_values:
    weights = []
    values = []
    for i in range(n):
        weights.append(random.randint(1, 11))  # for D3 between 1 and 10
        values.append(random.randint(1, 100))

    _, time_bottom_up = knapsack_bottom_up(weights, values, W)
    _, time_top_down = knapsack_top_down(weights, values, W, len(weights))

    bottom_up_times.append(time_bottom_up)
    top_down_times.append(time_top_down)

# Convert W to the size of its representation (number of bits)
W_representation_sizes = [len(bin(W)[2:]) for W in W_values]

# Plotting the results
plt.figure(figsize=(10, 5))
plt.plot(W_representation_sizes, bottom_up_times, label='Bottom-Up', marker='o')
plt.plot(W_representation_sizes, top_down_times, label='Top-Down', marker='x')
plt.xlabel('Size of W Representation (bits)')
plt.ylabel('Runtime (seconds)')
plt.title('Knapsack Problem: Runtime vs Size of W Representation')
plt.legend()
plt.show()