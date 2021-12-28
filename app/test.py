from dependency import *

include("../../python-lib")

from fileHandle import *
from argsHandle import *
from os import system

args = getArgs(["file"])

def test(tmp,file):
    print(tmp)
    if(file.lower() in tmp.lower()):
        system('"start '+tmp+'"')
        exit()

file = args.file
for n in getLines(".config"):
    if(args.file in n):
        file = n.split("::")[1]

x = lambda a,b=file : test(a,b)

for n in getLines(".config"):
    if(not "::" in n):
        getAllFiles(n,x)
