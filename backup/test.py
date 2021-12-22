from dependency import include

include("../../python-lib")

from fileHandle import *
from util import removeEmpty 
from os import chdir
from argsHandle import *

args = getArgs(["ref","target"])

ref = args.ref
target = args.target

files = []
dirs = []
for n in getAllFiles(ref):
    for x in getAllFiles("target"):
        if n.replace(ref+"/","") in x:
            files.append(x.replace(target+"/",""))
            dirs.append(basename(dirname(x).replace(target+"/","").replace(target,"")))

dirs = removeEmpty(dirs)
files = removeEmpty(files)

remove("backup")
mkdir("backup")
chdir("backup")

for n in dirs:
    print(n)
    mkdir(n)

print("")
for n in files:
    print(n)
    copy("../"+target+"/"+n,n)
