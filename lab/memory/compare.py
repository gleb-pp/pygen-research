import matplotlib.pyplot as plt

with open('python_memory.txt', 'r') as f:
    results = [f.strip().split() for f in f.readlines()]
    python_number_of_generators = [int(result[0]) for result in results]
    python_memory_usage = [float(result[1]) for result in results]

with open('go_memory.txt', 'r') as f:
    results = [f.strip().split() for f in f.readlines()]
    go_number_of_goroutines = [int(result[0]) for result in results]
    go_memory_usage = [float(result[1]) for result in results]

# графики
plt.figure(figsize=(10, 6))
plt.title('Memory Usage')
plt.xlabel('Number of Generators/Goroutines')
plt.ylabel('Memory Usage (bytes)')
plt.plot(python_number_of_generators, python_memory_usage, label='Python generators', marker='o', markersize=3)
plt.plot(go_number_of_goroutines, go_memory_usage, label='Go goroutines', marker='o', markersize=3)
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('comparison_memory_usage.png', dpi=300, bbox_inches='tight')
plt.close()

print("График сохранен: comparison_memory_usage.png")
