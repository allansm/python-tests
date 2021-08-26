import sys
sys.path.append("../functions")

from fileHandle import ls
from argsHandle import *
from util import showOptions as show
from os import chdir
from os import system
from os import getcwd
from os.path import isdir

def slow(path,before,tmp):
    chdir(path)
    while(True):
        print("")
        print("-------------------------------------------------------------------------")

        if(before != None and before != ""):
            system(before)

        print("")
        print("     PATH:"+path)
        print("")

        command = input("command:")
        
        if(command == "exit"):
            chdir(tmp)
            break;

        system(command)

def fast(path,command,tmp):
    chdir(path)
    print("")
    print("-------------------------------------------------------------------------")
    print("")
    print("     PATH:"+path+"")
    print("")
    system(command)
    chdir(tmp)

def run():
    args = getArgs(["path","--command","?slow"])
    path = args.path
    before = args.command
    slo = args.slow
    
    if(not slo and before == None):
        before = input("command:")

    tmp = getcwd()

    paths = ls(path,"*")
    
    for path in paths:
        if(path != "" and isdir(path)):
            if(slo):
                slow(path,before,tmp)
            else:
                fast(path,before,tmp) 
run()
