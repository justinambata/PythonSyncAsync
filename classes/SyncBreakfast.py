import asyncio
from classes.Breakfast import Breakfast

class SyncBreakfast(Breakfast):
    def __init__(self):
        super().__init__("SYNC")
        
    def make(self):
        self.make_pbj()
        asyncio.run(self.pour_oj())

    def make_pbj(self):
        print("Making a peanut butter & jelly sandwich:")
        asyncio.run(self.toast_bread_and_apply_spread("peanut butter"))
        asyncio.run(self.toast_bread_and_apply_spread("jelly"))
        asyncio.run(self.assemble_pbj())