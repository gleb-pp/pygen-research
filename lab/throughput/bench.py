import asyncio
from time import perf_counter

MAX_N = 100000
STEP = 1000

async def worker():
    await asyncio.sleep(0.001)

async def run(n):
    start = perf_counter()
    await asyncio.gather(*[worker() for _ in range(n)])
    total = perf_counter() - start

    throughput = n / total
    latency = total / n * 1e9

    return throughput, latency

async def main():
    with open("python_async.txt", "w") as f:
        for n in range(1, MAX_N + 1, STEP):
            print(f"Running with {n} workers...")
            t, l = await run(n)
            f.write(f"{n} {t} {l}\n")

asyncio.run(main())

