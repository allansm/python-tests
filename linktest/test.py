import dependency

from os import mkdir,chdir,symlink
from fileHandle import *
from argsHandle import *
from shutil import rmtree

args = getArgs(["dir","--out"])
files = getAllFilesPath(args.dir)

def rm(dn):
    try:
        rmtree(dn)
    except:
        dummy = ""

    try:
        mkdir(dn)
    except:
        dummy = ""

if(args.out != None): 
    rm(args.out)
    chdir(args.out)
else: 
    rm("links")
    chdir("links")


for f in files:
    fn = getFileName(f)
    print(fn)

    os.symlink(f,fn)
