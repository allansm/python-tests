from dependency import *
include("../../python-lib")

from allansm.fileHandle import *
from os import chdir
from zip import *
from allansm.argsHandle import *
from os import system
from allansm.elapse import *
from allansm.util import exec,echo

args = getArgs(["zip","action"])

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
    if("$" in args.action):
        tmp = ""
        for n in args.action.split(" "):
            if("$" in n):
                tmp = n.replace("$","")

        for n in ls():
            n = getFileName(n)

            flag = True
            for x in tmp.split(";"):
                if(not x.lower() in n.lower()):
                    flag = False

            if(flag):
                n = realpath(n)
                action = args.action
                action = action.replace("$"+tmp,"\""+n+"\"")

                system(action)
    else:
        system(args.action)
             
    chdir(getTemp())
    
    print("cleaning up...")
    remove("7z")

