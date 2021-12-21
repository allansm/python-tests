from dependency import include

include("../../python-lib")

from fileHandle import *
from util import removeEmpty 
from os import chdir

files = []
dirs = []
for n in getAllFiles("ref"):
    for x in getAllFiles("target"):
        if n.replace("ref/","") in x:
            files.append(x.replace("target/",""))
            dirs.append(basename(dirname(x).replace("target/","").replace("target","")))

dirs = removeEmpty(dirs)
files = removeEmpty(files)

#print(files)
#print(dirs)

remove("backup")
mkdir("backup")
chdir("backup")

for n in dirs:
    mkdir(n)

for n in files:
    copy("../target/"+n,n)
