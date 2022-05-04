import time
import asyncio
iteration_times = [1, 3, 2, 4]


async def sleeper(seconds, i=-1):
    start = time.time()
    if i != -1:
        print(f"{i}\t{seconds}s")
    await asyncio.sleep(seconds)
    return float(round(time.time() - start, 6))


run_time = 0
total_compute_runtime = 0


async def main():  # coroutine object
    global run_time, total_compute_runtime
    tasks = [
        asyncio.create_task(sleeper(second, i=i))
        for i, second in enumerate(iteration_times)
    ]

    results = await asyncio.gather(*tasks)
    print(results)
    for run_time_result in results:
        total_compute_runtime += run_time_result
        if run_time_result > run_time:
            run_time = run_time_result

asyncio.run(main())
print(f"Ran for {run_time} seconds\nWith a total of {total_compute_runtime} and {round(run_time/total_compute_runtime,4)}")
