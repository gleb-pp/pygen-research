import asyncio
from time import perf_counter

N = 1000000

async def worker():
    await asyncio.sleep(0.001)

async def main():
    start = perf_counter()
    await asyncio.gather(*[worker() for _ in range(N)])
    t = perf_counter() - start
    print(f"Python latency: {t}")

asyncio.run(main())

