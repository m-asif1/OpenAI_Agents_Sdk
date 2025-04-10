# import time

# def task1():
#     print("Task 1 Starting")
#     time.sleep(3)  # Simulating entire program for 3 seconds.
#     print("Task 1 completed")

# def task2():
#     print("Task 2 Starting")
#     # time.sleep(2)  # Simulating entire program for 2 seconds.
#     print("Task 2 completed")

# def main():
#     task1()   # program waits until task1 finishes.
#     task2()     # starts after task1 is complete.

# if __name__ == "__main__":
#     main()

# ---------------------------------------****************-------------------------------------
import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(3)  # sleeping for 3 seconds.
    print("Task 1 completed")

async def task2():
    print("Task 2 started")
    # await asyncio.sleep(2)  # sleeping for 2 seconds.
    print("Task 2 completed")

async def main():
    # Schedule both tasks concurrently.
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())
    await asyncio.gather(t1, t2)

if __name__ == "__main__":
    asyncio.run(main())
