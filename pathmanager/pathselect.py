import sys

sys.path.append("../functions")

from fileHandle import *

from os import chdir
from os import system
from os import getcwd

from argsHandle import *

def select(loc):
    chdir(loc)

    paths = getLines(".config")
    i=0
    for path in paths:
        print(str(i)+" : "+path)
        i = i+1

    index = input("index :")

    chdir(paths[int(index)])

def infinite(loc):
    command = input("command:")
    if(command == "select" and not loop):
        i = 0
        paths2 = ls(".","*")
        for path in paths2:
            print(str(i)+" : "+path)
            i = i+1

        index = input("index :")

        chdir(paths2[int(index)])
        
        command = input("command:")
    
    if(command == "exit"):
        select(loc)

    if(command == "bye"):
        exit()

    system(command)

    infinite(loc)

def run():
    args = getArgs(["?loop"])
    loop = args.loop
    
    loc = getcwd()

    select(loc)

    if(loop):
        infinite(loc)
    else: 
        command = input("command:")
        if(command == "select" and not loop):
            i = 0
            paths2 = ls(".","*")
            for path in paths2:
                print(str(i)+" : "+path)
                i = i+1

            index = input("index :")

            chdir(paths2[int(index)])
            
            command = input("command:")
         
        system(command)
run()
