import asyncio
import time

def sync_function(test_param: str) -> str:
    print("This is a Synchronous Function")

    time.sleep(1)

    return f'Sync Result, {test_param}'

#this is a coroutine function
async def async_function(test_param: str) -> str:
    print("This is a Asynchronous Function")

    await asyncio.sleep(0.1)
    return f'Async Result, {test_param}'

async def main():
    # sync_result = sync_function("Test")
    # print(sync_result)

    # loop = asyncio.get_event_loop()
    # future = loop.create_future()
    # print(f"Empty future: {future}")
    #
    # future.set_result("Future Result: Test")
    # future_result = await future
    # print(f"Future result: {future_result}")

    # coroutine_object = async_function('Test')
    # print(coroutine_object)
    #
    # coroutine_result = await coroutine_object
    # print(coroutine_result)

    task =asyncio.create_task(sync_function('test'))
    print(task)

    task_result = await task
    print(task_result)


if __name__ == '__main__':
    asyncio.run(main())