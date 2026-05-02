import tracemalloc

N = 100_000

def gen():
    yield 1

tracemalloc.start()

gens = [gen() for _ in range(N)]

current, peak = tracemalloc.get_traced_memory()

print(f"Peak: {peak / 1024 / 1024:.2f} MB")