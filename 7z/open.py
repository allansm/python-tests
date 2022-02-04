from dependency import *
include("../../python-lib")

from allansm.fileHandle import *
from os import chdir
from zip import *
from allansm.argsHandle import *
from os import system
from allansm.elapse import *
from allansm.util import exec,echo

args = getArgs(["zip"])

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
    
    while(True):
        op = input(getFileName(path).replace(".7z","")+">")
        
        tmp = "" 
        if("$" in op):
            for n in op.split(" "):
                if("$" in n):
                    tmp = n.replace("$","")
        
            for n in getAllFiles(realpath(".")):
                flag = True
                y = getFileName(n)
                for x in tmp.split(";"):
                    if(not x.lower() in y.lower()):
                        flag = False
                
                if(flag):
                    op = op.replace("$"+tmp,"\""+n+"\"")

        if(op == "exit"):
            break
        else:
            system(op)
             
    chdir(getTemp())
    
    print("cleaning up...")
    remove("7z")

