from time import perf_counter
import matplotlib.pyplot as plt

N = 10 ** 5
MAX_DEPTH = 100

def base_gen(n):
    for i in range(n):
        yield i

def make_yield_from_chain(depth):
    def gen(n, d):
        if d == 0:
            yield from base_gen(n)
        else:
            yield from gen(n, d - 1)
    return lambda n: gen(n, depth)

def make_manual_chain(depth):
    def gen(n, d):
        if d == 0:
            for x in base_gen(n):
                yield x
        else:
            for x in gen(n, d - 1):
                yield x
    return lambda n: gen(n, depth)

depths = []
execution_times = []

for depth in range(1, MAX_DEPTH + 1):
    print(f"Выполнено {depth}%")

    yield_from_gen = make_yield_from_chain(depth)
    manual_gen = make_manual_chain(depth)

    start = perf_counter()
    sum(yield_from_gen(N))
    yield_from_time = perf_counter() - start

    start = perf_counter()
    sum(manual_gen(N))
    manual_time = perf_counter() - start

    depths.append(depth)
    execution_times.append((yield_from_time, manual_time))

# удаление выбросов
def del_outlier(ind):
    del depths[ind]
    del execution_times[ind]

for i in range(MAX_DEPTH // 100):
    for j in range(2):
        del_outlier(execution_times.index(min(execution_times, key=lambda x: x[j])))
        del_outlier(execution_times.index(max(execution_times, key=lambda x: x[j])))

# графики
plt.figure(figsize=(10, 6))
plt.title('Execution Time')
plt.xlabel('Chain Depth')
plt.ylabel('Time (seconds)')
plt.plot(depths, [t[0] for t in execution_times], label='Yield From Execution Time')
plt.plot(depths, [t[1] for t in execution_times], label='Manual Execution Time')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('comparison_execution_time.png', dpi=300, bbox_inches='tight')
plt.close()

print("График сохранен: comparison_execution_time.png")
