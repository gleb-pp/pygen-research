import matplotlib.pyplot as plt

with open('python_async.txt', 'r') as f:
    results = [f.strip().split() for f in f.readlines()]
    number_of_parallel_tasks = [int(result[0]) for result in results]
    python_throughput = [float(result[1]) for result in results]
    python_latency = [float(result[2]) for result in results]

with open('go_async.txt', 'r') as f:
    results = [f.strip().split() for f in f.readlines()]
    go_number_of_goroutines = [int(result[0]) for result in results]
    go_throughput = [float(result[1]) for result in results]
    go_latency = [float(result[2]) for result in results]

# графики
plt.figure(figsize=(10, 6))
plt.title('Throughput')
plt.xlabel('Number of Parallel Tasks')
plt.ylabel('Throughput (tasks/sec)')
plt.plot(number_of_parallel_tasks, python_throughput, label='Python async', marker='o', markersize=3)
plt.plot(go_number_of_goroutines, go_throughput, label='Go async', marker='o', markersize=3)
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('comparison_throughput.png', dpi=300, bbox_inches='tight')
plt.close()

plt.figure(figsize=(10, 6))
plt.title('Latency')
plt.xlabel('Number of Parallel Tasks')
plt.ylabel('Latency (ns)')
plt.plot(number_of_parallel_tasks, python_latency, label='Python async', marker='o', markersize=3)
plt.plot(go_number_of_goroutines, go_latency, label='Go async', marker='o', markersize=3)
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('comparison_latency.png', dpi=300, bbox_inches='tight')
plt.close()

print("Графики сохранены: comparison_throughput.png, comparison_latency.png")
