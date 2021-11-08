import dependency

from os import mkdir,chdir,symlink,getcwd
from fileHandle import *
from argsHandle import *
from shutil import rmtree

#print(getcwd())
#exit()

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
    #build(args.out)
    #chdir(args.out)
    #odir=args.out
    print(":O")
    exit()
else: 
    build("links")
    chdir("links")
    odir="links"


for f in files:
    if(not ":" in args.dir):
        fn = getFileName(f)
        tmp = "" 
        if(args.dir+"/" in f):
            tmp = f.split(args.dir+"/")[1]
        elif(args.dir+"\\" in f):
            tmp = f.split(args.dir+"\\")[1]
        
        tmp2 = tmp
        tmp = tmp.replace(fn,"")
        
        try:
            if(not tmp == "\\" and not tmp == "/" and not tmp == ""): 
                print(tmp)
                mkdir(tmp)
        except:
            dummy=""
        
        try:
            os.symlink(f,tmp2)
        except:
            dummy=""
