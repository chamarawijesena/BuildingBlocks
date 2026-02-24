import asyncio

async def fetch_data(param):
    print(f'Fetching data from {param}')
    await asyncio.sleep(param)
    print(f"Done fetching data from {param}")
    return f"Result from {param}"

async def main():
    task1 = fetch_data(param=1)
    task2 = fetch_data(param=2)
    result1 = await task1
    print("Task 1 fully completed")

    result2 = await task2
    print("Task 2 fully completed")

    return [result1, result2]

results = asyncio.run(main())
print(results)