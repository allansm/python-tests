import sys

sys.path.append("../functions")

from fileHandle import *
from argsHandle import *

from os import chdir
from os import system


def run():
    paths = getLines(".config")
    before = getArgs(["--command"]).command

    for path in paths:
        if(path != ""):
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
                    break;

                system(command)

run()
