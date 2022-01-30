import dependency

from allansm.fileHandle import *
from allansm.argsHandle import *

args = getArgs(["folder","bin","--ignore"])
ignore = args.ignore

if(ignore == None):
    ignore = ""

folders =  getAllPaths(args.folder)
bin = args.bin

res = ""

for f in folders:
    if(bin == f.split("\\")[-1]):
        if(not ignore in f or ignore == ""):
            print(f)
            res+=f+";"

print()
print(res)
