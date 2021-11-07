import dependency

from os import mkdir,chdir,symlink
from fileHandle import *
from argsHandle import *
from shutil import rmtree

args = getArgs(["dir","--out"])
files = getAllFilesPath(args.dir)

def build(dn):
    try:
        rmtree(dn)
    except:
        dummy = ""

    try:
        mkdir(dn)
    except:
        dummy = ""
odir = ""
if(args.out != None): 
    build(args.out)
    chdir(args.out)
    odir=args.out
else: 
    build("links")
    chdir("links")
    odir="links"


for f in files:
    fn = getFileName(f)
    tmp = f
    if(":\\" in tmp):
        tmp = tmp.split(":\\")[1]
    elif(":/" in tmp):
        tmp = tmp.split(":/")[1]

    tmp = tmp.replace(args.dir,odir)
    filepath = tmp
    folder = tmp.replace(fn,"")
    print(folder)
    try:
        mkdir(folder)
    except:
        dummy=""
    #os.symlink(f,filepath)
