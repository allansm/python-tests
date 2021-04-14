import sys

sys.path.append("../functions")

from os import system
from fileHandle import *

system("echo . > .ram")
system("wmic os get freephysicalmemory >> .ram")

file = readFile(".ram")

try:
    lines = getLines(".ram")
except:
    print("error!!!")

remove(".ram")

print(file)
#print(lines[1])
