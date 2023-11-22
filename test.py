import asyncio
import sys

async def wait_test():
    try:
        #Fake Async Server Call
        await asyncio.wait_for(asyncio.sleep(10000), timeout=1)
    except asyncio.TimeoutError:
        print("TimeoutError")
        sys.exit(1)
    return



if __name__ == "__main__":
    #You'll need to figure out how to get your functionality in here.
    asyncio.run(wait_test()) 