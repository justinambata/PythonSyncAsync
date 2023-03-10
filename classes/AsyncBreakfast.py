import asyncio
from classes.Breakfast import Breakfast

class AsyncBreakfast(Breakfast):
    def __init__(self):
        super().__init__("ASYNC")
        #self.loop = asyncio.get_event_loop()
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
    
    def make(self):
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
        
    async def make_pbj(self):
        print("Making a peanut butter & jelly sandwich:")
        task_pb = self.loop.create_task(self.toast_bread_and_apply_spread("peanut butter"))
        task_jelly = self.loop.create_task(self.toast_bread_and_apply_spread("jelly"))
        self.tasks.append(task_pb)
        self.tasks.append(task_jelly)
        if task_pb.done() and task_jelly.done():
            await self.assemble_pbj()
