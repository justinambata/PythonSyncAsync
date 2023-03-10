import time

def sleep(secs):
    #print(f'Time: {time.time() - start:.2f}')
    time.sleep(secs)

def toast_bread():
    print("Toasting bread...")
    sleep(1)
    print("Toasting bread done.")
  
def apply_spread(spread):
    print(f'Applying {spread}...')
    sleep(1)
    print(f'Applying {spread} done.')
    
def toast_bread_and_apply_spread(spread):
    toast_bread()
    apply_spread(spread)

def assemble_pbj():
    print("Assembling peanut butter & jelly sandwich...")
    sleep(1)
    print("Assembling peanut butter & jelly sandwich done.")
  
def make_pbj():
    print("Making peanut butter & jelly sandwich.")
    toast_bread_and_apply_spread("peanut butter")
    toast_bread_and_apply_spread("jelly")
    assemble_pbj()
    
def pour_oj():
    print("Pouring orange juice...")
    sleep(3)
    print("Pouring orange juice done.")

print("SYNC TEST")
start = time.time()
make_pbj()
pour_oj()
end = time.time()
print(f'Time: {end-start:.2f} sec')