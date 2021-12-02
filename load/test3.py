import sys
sys.path.append("../../python-lib")

from fileHandle import *
from random import shuffle

lines = getLines("test.txt")

tmp = []
for n in range(0,len(lines)):
    tmp.append(n)

for n in range(0,9):
    shuffle(tmp)

print(tmp)

for n in tmp:
    print(lines[n])

