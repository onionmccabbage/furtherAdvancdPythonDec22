# modern Python lets us manage asynchronous code using 'async'
# e.g. accessing long running or slow microservices, APIs etc.
import asyncio
import time
# we can declare any function to be asynchronous
async def square(n): # async makes this a co-routine (i.e. run on a thread)
    await asyncio.sleep(2)
    return n*n

# CAREFUL - coroutine may well be deprecated so it may not exist in recent/future Python
@asyncio.coroutine # make the decorated function into a co-routine (i.e. run it asynchronously)
def cube(n):
    return n*n*n

if __name__ == '__main__':
    # by calling an async co-routine we are NOT blocking the main thread
    r = asyncio.run(square(3)) # we call our async co-routine
    # other code will not be blocked
    print(123)
    print(r) # 9
    s = asyncio.run(cube(3))
    print(s) # 27