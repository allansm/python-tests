from dependency import *

include("../../python-lib")

from fileHandle import *
from argsHandle import *
from os import system

args = getArgs(["file","--detail"])

def test(tmp,file,detail):
    print(tmp)
    print(dirname(tmp))
    if(file.lower() in tmp.lower()):
        if(detail != None):
            if(detail in tmp.lower()):
                system('"start '+tmp+'"')
                exit()
        else:
            system('"start '+tmp+'"')
            exit()

file = args.file
for n in getLines(".config"):
    if(args.file in n):
        file = n.split("::")[1]

x = lambda a,b=file,c=args.detail : test(a,b,c)

for n in getLines(".config"):
    if(not "::" in n):
        getAllFiles(n,x)
