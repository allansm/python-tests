import sys
sys.path.append("../../python-lib")

from imageHandle import *
from elapse import *

e = Elapse()

i = 0
while(e.elapsed() < 1000):
    screenshot()
    i+=1

print(i)

e = Elapse()

i = 0
while(e.elapsed() < 1000):
    screenshot(bbox =(0, 0, 640, 480))
    i+=1

print(i)

e = Elapse()

i = 0
while(e.elapsed() < 1000):
    screenshot(bbox =(0, 0, 400, 300))
    i+=1

print(i)

e = Elapse()

i = 0
while(e.elapsed() < 1000):
    screenshot(bbox =(0, 0, 10, 10))
    i+=1

print(i)

