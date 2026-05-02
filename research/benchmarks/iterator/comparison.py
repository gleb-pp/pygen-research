from time import perf_counter
import matplotlib.pyplot as plt

N = 10**5

class MyIterator:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        val = self.i
        self.i += 1
        return val

def gen(n):
    for i in range(n):
        yield i

number_of_iterations = []
execution_times = []

i = 1

for cnt in range(1, N + 1):
    if i // (N // 100) != cnt // (N // 100):
        print(f"Выполнено {cnt // (N // 100)}%")

    start = perf_counter()
    iter_res = sum(MyIterator(cnt))
    iter_time = perf_counter() - start

    start = perf_counter()
    gen_res = sum(gen(cnt))
    gen_time = perf_counter() - start

    number_of_iterations.append(cnt)
    execution_times.append((iter_time, gen_time))
    i = cnt

# удаление выбросов
def del_outlier(ind):
    del number_of_iterations[ind]
    del execution_times[ind]

for i in range(N // 100):
    for j in range(2):
        del_outlier(execution_times.index(min(execution_times, key=lambda x: x[j])))
        del_outlier(execution_times.index(max(execution_times, key=lambda x: x[j])))

# графики
plt.figure(figsize=(10, 6))
plt.title('Execution Time')
plt.xlabel('Number of iterations')
plt.ylabel('Time (seconds)')
plt.plot(number_of_iterations, [t[0] for t in execution_times], label='Iterator Execution Time')
plt.plot(number_of_iterations, [t[1] for t in execution_times], label='Generator Execution Time')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('comparison_execution_time.png', dpi=300, bbox_inches='tight')
plt.close()

print("График сохранен: comparison_execution_time.png")
