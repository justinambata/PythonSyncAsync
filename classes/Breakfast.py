from abc import ABC, abstractmethod
import asyncio
from const import TimeConstants

class Breakfast(ABC):
    def __init__(self, type):
        print(f"{type} TEST")

    @abstractmethod
    def make(self):
        pass

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
    
    @abstractmethod
    async def make_pbj(self):
        pass
    
    async def pour_oj(self):
        print("Pouring orange juice...")
        await self.sleep(TimeConstants.SECS_POUR_OJ)
        print("Pouring orange juice done.")