import time
import asyncio

async def function1():
    await asyncio.sleep(1)
    print("fun1")
    return "daksh"

async def function2():
    await asyncio.sleep(1)
    print("fun2")
    return "bhai"

async def function3():
    await asyncio.sleep(3)
    print("fun3")
    return "bdiya"

async def main():
    L = await asyncio.gather(
        function1(), function2(), function3()
    )
    print(L)
    # task = asyncio.create_task(function1())
    # await function2
    # await function3

asyncio.run(main())    