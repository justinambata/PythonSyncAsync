import time
from classes.AsyncBreakfast import AsyncBreakfast
from classes.SyncBreakfast import SyncBreakfast

def RunAsyncBreakfast():        
    start = time.time()
    breakfast = AsyncBreakfast()
    breakfast.make()
    end = time.time()
    print(f'Time: {end-start:.2f} sec')

def RunSyncBreakfast():        
    start = time.time()
    breakfast = SyncBreakfast()
    breakfast.make()
    end = time.time()
    print(f'Time: {end-start:.2f} sec')

RunSyncBreakfast()
RunAsyncBreakfast()
