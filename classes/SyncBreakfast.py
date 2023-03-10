import time
from const import TimeConstants

class SyncBreakfast:
    def __init__(self):
        print("SYNC TEST")
        
    def make(self):
        self.make_pbj()
        self.pour_oj()

    def sleep(self, secs):
        time.sleep(secs)

    def toast_bread(self):
        print("Toasting bread...", end='')
        self.sleep(TimeConstants.SECS_TOAST)
        print("done.")
      
    def apply_spread(self, spread):
        print(f'Applying {spread}...', end='')
        self.sleep(TimeConstants.SECS_APPLY_SPREAD)
        print('done.')
        
    def toast_bread_and_apply_spread(self, spread):
        self.toast_bread()
        self.apply_spread(spread)
    
    def assemble_pbj(self):
        print("Assembling peanut butter & jelly sandwich...", end='')
        self.sleep(TimeConstants.SECS_ASSEMBLE_SANDWICH)
        print("done.")
      
    def make_pbj(self):
        print("Making a peanut butter & jelly sandwich:")
        self.toast_bread_and_apply_spread("peanut butter")
        self.toast_bread_and_apply_spread("jelly")
        self.assemble_pbj()
        
    def pour_oj(self):
        print("Pouring orange juice...", end='')
        self.sleep(TimeConstants.SECS_POUR_OJ)
        print("done.")
