import sys

sys.path.append("../functions")

from fileHandle import *

from os import chdir
from os import system


def run():
    paths = getLines(".config")

    command = input("command:")

    for path in paths:
        if(path != ""):
            chdir(path)
            print("")
            print("     PATH:"+path)
            print("")
            system(command)

run()
