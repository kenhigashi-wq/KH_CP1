# KH while loops

import time
import random

num =1 
break_point = random.randint(1,50)
while num <= 20:
    print(num)
    time.sleep(.10)
    if num == 20:
        break
    elif num == 5:
        continue
    num += 1 # fixed the loop
else:
    print("L")
print("za loop eez ovah")