import sys

sys.path.append("../functions")

from fileHandle import *
from argsHandle import *

from os import chdir
from os import system


def run():
    command = getArgs(["command"],"").command
    paths = getLines(".config")
    
    if(command == None or command == ""):
        command = input("command:")

    for path in paths:
        if(path != ""):
            chdir(path)
            print("")
            print("-------------------------------------------------------------------------")
            print("")
            print("     PATH:"+path+"")
            print("")
            system(command)
           
run()
