import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=6)

async def sleep(secs):
    #print(f'Time: {time.time() - start:.2f}')
    await asyncio.sleep(secs)
    
async def toast_bread():
    print("Toasting bread...")
    await sleep(1)
    print("Toasting bread done.")
  
async def apply_spread(spread):
    print(f'Applying {spread}...')
    await sleep(1)
    print(f'Applying {spread} done.')
    
async def toast_bread_and_apply_spread(spread):
    await toast_bread()
    await apply_spread(spread)

async def assemble_pbj():
    print("Assembling peanut butter & jelly sandwich...")
    await sleep(1)
    print("Assembling peanut butter & jelly sandwich done.")
    
async def make_pbj():
    print("Making peanut butter & jelly sandwich.")
    task1 = loop.create_task(toast_bread_and_apply_spread("peanut butter"))
    task2 = loop.create_task(toast_bread_and_apply_spread("jelly"))
    if task1.done() and task2.done():
        await assemble_pbj()

async def pour_oj():
    print("Pouring orange juice...")
    await sleep(3)
    print("Pouring orange juice done.")

print("ASYNC TEST")
start = time.time()

loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(make_pbj()),
    loop.create_task(pour_oj()),
]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

end = time.time()
print(f'Time: {end-start:.2f} sec')