from time import perf_counter

N = 10**7

def gen():
    while True:
        yield

g = gen()

# прогрев
for _ in range(1000):
    next(g)

start = perf_counter()
for _ in range(N):
    next(g)
gen_time = perf_counter() - start

print(f"Python: {gen_time / N * 1_000_000_000:.2f} ns")