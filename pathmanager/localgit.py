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
totcom = 0

quiet = getArgs(["--quiet"]).quiet

print("")

for path in paths:
    if(path != ""):
        chdir(path)
        if(quiet == "no"):
            print(" "+path)
        output = subprocess.check_output("git status", shell=True)

        if("Changes not staged for commit" in str(output) or "Untracked files" in str(output)):
            if(quiet == "no"):
                print("     need update\n")
            totup = totup+1

        else:
            if(quiet == "no"):
                print("     all up to date\n")

        if("Your branch is ahead of" in str(output) and "by" in str(output) and "(use \"git push\" to publish your local commits)" in str(output)):
            tmp = str(output).split("by")[1].split(" ")[1]
            tmp = int(tmp)
            totcom += tmp 

print("total projects to be updated:"+str(totup))
print("total updates:"+str(totcom))
