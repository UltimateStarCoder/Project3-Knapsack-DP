import random
import time
import matplotlib.pyplot as plt
from D1v2 import knapsack_bottom_up, knapsack_top_down

random.seed(42)
N = sorted([random.randrange(10, 101, 10) for _ in range(10)])  # Generate a sorted list of random values for N

W = 1000

bottom_up_times = []
top_down_times = []

for n in N:
    weights = []
    values = [] 
    for i in range(n):
        weights.append(random.randint(1, 11))  # for D3 between 1 and 10
        values.append(random.randint(1, 100))

    _, time_bottom_up = knapsack_bottom_up(weights, values, W)
    _, time_top_down = knapsack_top_down(weights, values, W, len(weights))

    bottom_up_times.append(time_bottom_up)
    top_down_times.append(time_top_down)

# Plotting the results
plt.figure(figsize=(10, 5))
plt.plot(N, bottom_up_times, label='Bottom-Up', marker='o')
plt.plot(N, top_down_times, label='Top-Down', marker='x')
plt.xlabel('Number of Items (n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Comparison of Knapsack Algorithm Execution Times')
plt.legend()
plt.show()