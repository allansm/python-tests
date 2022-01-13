from dependency import *
include("../../python-lib")

from allansm.fileHandle import *
from os import chdir
from zip import *
from allansm.argsHandle import *
from os import system
from allansm.elapse import *
from allansm.util import exec,echo

args = getArgs(["zip","action","?find","--command"])

path = realpath(args.zip)

if(exists(path)):
    chdir(getTemp())
    remove("7z")
    mkdir("7z")
    chdir("7z")

    e = Elapse()
    exec('7z x "'+path+'"')
    echo("elapsed:")
    e.show(0.001)
    
    if(not args.find):
        system(args.action)
    else:
        for n in ls():
            n = realpath(n)
            print(n)
            flag = True
            for x in args.action.split(";"):
                if(not x.lower() in n.lower()):
                    flag = False

            if(flag):
                if(args.command == None):
                    system('"'+n+'"')
                else:
                    system(args.command+" \""+n+"\"")

    chdir(getTemp())
    
    print("cleaning up...")
    remove("7z")

