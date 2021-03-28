# Reference: https://docs.python.org/3.9/library/asyncio-task.html

import asyncio, time

async def say_after(delay, what):
    while True:
        await asyncio.sleep(delay)
        print(what)

async def main():
    task1 = asyncio.create_task(say_after(1, 'hello'))

    task2 = asyncio.create_task(say_after(5, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 6 seconds.)
    await task1
    await task2
    
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())