import sys
sys.path.append("../../python-lib")

from argsHandle import *
from fileHandle import *

args = getArgs(["file","txt"])

def filter(pattern,txt):
    i = 0
    for n in pattern.split(";"):
        if(not n in txt):
            i+=1
    
    if(i == 0):
        return True
    else:
        return False

for n in getLines(args.file):
    if(filter(args.txt,n)):
        print(n)

