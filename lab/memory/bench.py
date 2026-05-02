import tracemalloc

MAX_N = 100000
STEP = 1000

def gen():
    yield 1

sizes = []
memory = []

tracemalloc.start()

for n in range(1, MAX_N + 1, STEP):
    gens = [gen() for _ in range(n)]
    current, peak = tracemalloc.get_traced_memory()

    sizes.append(n)
    memory.append(peak)

    del gens

with open("python_memory.txt", "w") as f:
    for s, m in zip(sizes, memory):
        f.write(f"{s} {m}\n")

