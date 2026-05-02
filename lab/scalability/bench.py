from time import perf_counter

MAX_D = 100
N = 10**6

def base():
    yield 1

def make_chain(d):
    def gen():
        yield 1

    for _ in range(d):
        prev = gen
        def gen(prev=prev):
            yield from prev()
    return gen

depths = []
times = []

for d in range(1, MAX_D + 1):
    print(f"Testing depth {d}...")
    g = make_chain(d)()

    start = perf_counter()
    for _ in range(N):
        try:
            next(g)
        except StopIteration:
            g = make_chain(d)()
    t = perf_counter() - start

    depths.append(d)
    times.append(t)

with open("python_chain.txt", "w") as f:
    for d, t in zip(depths, times):
        f.write(f"{d} {t}\n")
