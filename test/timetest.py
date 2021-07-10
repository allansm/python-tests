import sys
sys.path.append("../functions")

from timeHandle import *

#print(getTime())

import time

cl1 = getTime()

start = time.time()
i = 0
while(i < 10000):
    i = i + 1
    print(i)
end = time.time()
print("end")
cl2 = getTime()

print(cl1)
print(cl2)

print(int((end - start)/60))
