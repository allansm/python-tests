import sys

sys.path.append("../functions")

from fileHandle import *
from os import chdir
from os import rename
from argsHandle import *

def run():
    args = getArgs(["folder","currentname","newname"])

    folder = args.folder
    cname = args.currentname
    nname = args.newname

    chdir(folder)
    files = getAllFiles(".")

    for tmp in files:
        newname = tmp.replace(cname,nname)
        
        rename(tmp,newname)

        print(tmp+" > "+newname)


run()
