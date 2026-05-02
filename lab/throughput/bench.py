import asyncio
from time import perf_counter

N = 5 * 10 ** 6

async def worker():
    return 1

async def main():
    start = perf_counter()
    await asyncio.gather(*[worker() for _ in range(N)])
    t = perf_counter() - start
    print(f"Python: {t}")

asyncio.run(main())


