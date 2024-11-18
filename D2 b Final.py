import random
import matplotlib.pyplot as plt
from D1v2 import knapsack_bottom_up, knapsack_top_down

random.seed(42)
n = 50
W_values = sorted([random.randrange(100, 1001, 100) for _ in range(10)])  # Generate a sorted list of random values for W

bottom_up_times_W = []
top_down_times_W = []

for W in W_values:
    weights = [random.randint(1, W) for _ in range(n)]
    values = [random.randint(1, 100) for _ in range(n)]

    _, time_bottom_up = knapsack_bottom_up(weights, values, W)
    _, time_top_down = knapsack_top_down(weights, values, W, len(weights))

    bottom_up_times_W.append(time_bottom_up)
    top_down_times_W.append(time_top_down)

# Plotting the results for varying W
plt.figure(figsize=(10, 5))
plt.plot(W_values, bottom_up_times_W, label='Bottom-Up', marker='o')
plt.plot(W_values, top_down_times_W, label='Top-Down', marker='x')
plt.xlabel('Knapsack Capacity (W)')
plt.ylabel('Execution Time (seconds)')
plt.title('Comparison of Knapsack Algorithm Execution Times for Varying W')
plt.legend()
plt.show()