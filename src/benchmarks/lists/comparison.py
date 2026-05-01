from time import perf_counter
import sys
import matplotlib.pyplot as plt

N = 10**5

def list_version(cnt):
    return [i * i for i in range(cnt)]

def generator_version(cnt):
    return (i * i for i in range(cnt))

number_of_items = []
creation_times = []
memory_usages = []
iteration_times = []

i = 1

for cnt in range(1, N + 1):
    if i // 10 **3 != cnt // 10 ** 3:
        print(cnt // 10 ** 3)
    start = perf_counter()
    lst = list_version(cnt)
    list_time = perf_counter() - start

    start = perf_counter()
    gen = generator_version(cnt)
    gen_time = perf_counter() - start

    start = perf_counter()
    sum(lst)
    list_iter_time = perf_counter() - start

    start = perf_counter()
    sum(gen)
    gen_iter_time = perf_counter() - start

    number_of_items.append(cnt)
    creation_times.append((list_time, gen_time))
    memory_usages.append((sys.getsizeof(lst), sys.getsizeof(gen)))
    iteration_times.append((list_iter_time, gen_iter_time))
    i = cnt

# удаление выбросов
def del_outlier(ind):
    del number_of_items[ind]
    del creation_times[ind]
    del memory_usages[ind]
    del iteration_times[ind]

for i in range(N // 100):
    for j in range(2):
        del_outlier(creation_times.index(min(creation_times, key=lambda x: x[j])))
        del_outlier(creation_times.index(max(creation_times, key=lambda x: x[j])))
        del_outlier(memory_usages.index(min(memory_usages, key=lambda x: x[j])))
        del_outlier(memory_usages.index(max(memory_usages, key=lambda x: x[j])))
        del_outlier(iteration_times.index(min(iteration_times, key=lambda x: x[j])))
        del_outlier(iteration_times.index(max(iteration_times, key=lambda x: x[j])))

# графики
plt.figure(figsize=(10, 6))
plt.title('Creation Time')
plt.xlabel('Number of Items')
plt.ylabel('Time (seconds)')
plt.plot(number_of_items, [t[0] for t in creation_times], label='List Creation Time')
plt.plot(number_of_items, [t[1] for t in creation_times], label='Generator Creation Time')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('comparison_creation_time.png', dpi=300, bbox_inches='tight')
plt.close()

plt.figure(figsize=(10, 6))
plt.title('Memory Usage')
plt.xlabel('Number of Items')
plt.ylabel('Memory (bytes)')
plt.plot(number_of_items, [m[0] for m in memory_usages], label='List Memory Usage')
plt.plot(number_of_items, [m[1] for m in memory_usages], label='Generator Memory Usage')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('comparison_memory_usage.png', dpi=300, bbox_inches='tight')
plt.close()

plt.figure(figsize=(10, 6))
plt.title('Iteration Time')
plt.xlabel('Number of Items')
plt.ylabel('Time (seconds)')
plt.plot(number_of_items, [t[0] for t in iteration_times], label='List Iteration Time')
plt.plot(number_of_items, [t[1] for t in iteration_times], label='Generator Iteration Time')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('comparison_iteration_time.png', dpi=300, bbox_inches='tight')
plt.close()

print("Графики сохранены: comparison_creation_time.png, comparison_memory_usage.png, comparison_iteration_time.png")
