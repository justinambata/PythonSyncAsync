import time
from classes.AsyncBreakfast import AsyncBreakfast
from classes.SyncBreakfast import SyncBreakfast

def MakeAsyncBreakfast():       
    breakfast = AsyncBreakfast()
    breakfast.make()

def MakeSyncBreakfast():        
    breakfast = SyncBreakfast()
    breakfast.make()

def Run(method):
    start = time.time()
    method()
    end = time.time()
    print(f'Time: {end-start:.2f} sec')

Run(MakeSyncBreakfast)
Run(MakeAsyncBreakfast)