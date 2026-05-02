import matplotlib.pyplot as plt

with open('python_chain.txt', 'r') as f:
    results = [f.strip().split() for f in f.readlines()]
    python_depths = [int(result[0]) for result in results]
    python_execution_times = [float(result[1]) for result in results]

with open('go_chain.txt', 'r') as f:
    results = [f.strip().split() for f in f.readlines()]
    go_depths = [int(result[0]) for result in results]
    go_execution_times = [float(result[1]) for result in results]

# графики
plt.figure(figsize=(10, 6))
plt.title('Execution Time')
plt.xlabel('Chain Depth')
plt.ylabel('Time (nanoseconds)')
plt.plot(python_depths, python_execution_times, label='Python generators with yield from', marker='o', markersize=3)
plt.plot(go_depths, go_execution_times, label='Go goroutines with channels', marker='o', markersize=3)
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('comparison_execution_time.png', dpi=300, bbox_inches='tight')
plt.close()

print("График сохранен: comparison_execution_time.png")
