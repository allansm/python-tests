import sys

from os import chdir
from os.path import realpath
from os.path import dirname
chdir(dirname(realpath(__file__)))

sys.path.append("../functions")

from fileHandle import *
from argsHandle import *

import subprocess

paths = getLines(".config")

totup = 0

quiet = getArgs(["quiet"],"").quiet

for path in paths:
    if(path != ""):
        chdir(path)
        if(quiet == "no"):
            print(path)
        output = subprocess.check_output("git status", shell=True)

        if("Changes not staged for commit" in str(output) or "Untracked files" in str(output)):
            if(quiet == "no"):
                print(" need update\n")
            totup = totup+1

        else:
            if(quiet == "no"):
                print(" all up to date\n")

print("total projects to be updated:"+str(totup))
