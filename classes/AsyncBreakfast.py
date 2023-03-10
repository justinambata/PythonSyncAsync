import asyncio
from const import TimeConstants

class AsyncBreakfast:
    def __init__(self):
        print("ASYNC TEST")
    
    def make(self):
        self.loop = asyncio.get_event_loop()
        self.tasks = [
            self.loop.create_task(self.make_pbj()),
            self.loop.create_task(self.pour_oj()),
        ]
        self.loop.run_until_complete(asyncio.wait(self.tasks))
        #self.loop.close()
        self.loop.stop()

        try:
            # run_forever() returns after calling loop.stop()
            self.loop.run_forever()
            for t in [t for t in self.tasks if not (t.done() or t.cancelled())]:
                # give canceled tasks the last chance to run
                self.loop.run_until_complete(t)
        finally:
            self.loop.close()
    
    async def sleep(self, secs):
        await asyncio.sleep(secs)
        
    async def toast_bread(self):
        print("Toasting bread...")
        await self.sleep(TimeConstants.SECS_TOAST)
        print("Toasting bread done.")
      
    async def apply_spread(self, spread):
        print(f'Applying {spread}...')
        await self.sleep(TimeConstants.SECS_APPLY_SPREAD)
        print(f'Applying {spread} done.')
        
    async def toast_bread_and_apply_spread(self, spread):
        await self.toast_bread()
        await self.apply_spread(spread)
    
    async def assemble_pbj(self):
        print("Assembling peanut butter & jelly sandwich...")
        await self.sleep(TimeConstants.SECS_ASSEMBLE_SANDWICH)
        print("Assembling peanut butter & jelly sandwich done.")
        
    async def make_pbj(self):
        print("Making a peanut butter & jelly sandwich:")
        task1 = self.loop.create_task(self.toast_bread_and_apply_spread("peanut butter"))
        task2 = self.loop.create_task(self.toast_bread_and_apply_spread("jelly"))
        self.tasks.append(task1)
        self.tasks.append(task2)
        if task1.done() and task2.done():
            await self.assemble_pbj()
            #self.loop.create_task(self.assemble_pbj())
    
    async def pour_oj(self):
        print("Pouring orange juice...")
        await self.sleep(TimeConstants.SECS_POUR_OJ)
        print("Pouring orange juice done.")
