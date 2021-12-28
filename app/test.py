from dependency import *

include("../../python-lib")

from fileHandle import *
from argsHandle import *
from os import system

args = getArgs(["file"])

def test(tmp,file):
    print(tmp)
    if(file.lower() in tmp.lower()):
        #print(tmp)
        system('"start '+tmp+'"')
        exit()

x = lambda a,b=args.file : test(a,b)


for n in getLines(".config"):
    getAllFiles(n,x)
