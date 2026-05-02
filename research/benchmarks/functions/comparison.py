from time import perf_counter
import matplotlib.pyplot as plt

N = 10**5

def sum_with_loop(n):
    total = 0
    for i in range(n):
        total += i
    return total

def sum_with_generator(n):
    return sum(i for i in range(n))

def gen(n):
    for i in range(n):
        yield i

def sum_with_yield(n):
    return sum(gen(n))

number_of_iterations = []
execution_times = []

i = 1

for cnt in range(1, N + 1):
    if i // (N // 100) != cnt // (N // 100):
        print(f"Выполнено {cnt // (N // 100)}%")

    start = perf_counter()
    function_res = sum_with_loop(cnt)
    function_time = perf_counter() - start

    start = perf_counter()
    gen_res = sum_with_generator(cnt)
    gen_time = perf_counter() - start

    start = perf_counter()
    yield_res = sum_with_yield(cnt)
    yield_time = perf_counter() - start

    number_of_iterations.append(cnt)
    execution_times.append((function_time, gen_time, yield_time))
    i = cnt

# удаление выбросов
def del_outlier(ind):
    del number_of_iterations[ind]
    del execution_times[ind]

for i in range(N // 100):
    for j in range(3):
        del_outlier(execution_times.index(min(execution_times, key=lambda x: x[j])))
        del_outlier(execution_times.index(max(execution_times, key=lambda x: x[j])))

# графики
plt.figure(figsize=(10, 6))
plt.title('Execution Time')
plt.xlabel('Number of iterations')
plt.ylabel('Time (seconds)')
plt.plot(number_of_iterations, [t[0] for t in execution_times], label='Function Execution Time')
plt.plot(number_of_iterations, [t[1] for t in execution_times], label='Generator Execution Time')
plt.plot(number_of_iterations, [t[2] for t in execution_times], label='Yield Execution Time')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('comparison_execution_time.png', dpi=300, bbox_inches='tight')
plt.close()

print("График сохранен: comparison_execution_time.png")
