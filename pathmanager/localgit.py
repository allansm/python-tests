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

args = getArgs(["?show","?who"])
show = args.show
who = args.who

modified = []

print("")

for path in paths:
    if(path != ""):
        chdir(path)
        
        if(show):
            print(" "+path)

        output = subprocess.check_output("git status", shell=True)

        if("Changes not staged for commit" in str(output) or "Untracked files" in str(output)):
            if(show):
                print("     need update\n")
            totup = totup+1
            modified.append(path)
        else:
            if(show):
                print("     all up to date\n")

        if("Your branch is ahead of" in str(output) and "by" in str(output) and "(use \"git push\" to publish your local commits)" in str(output)):
            tmp = str(output).split("by")[1].split(" ")[1]
            tmp = int(tmp)
            totcom += tmp
            modified.append(path)
if(who):
    for mod in modified:
        if "\\" in mod:
            proj = mod.split("\\")[-1]
        elif "/" in mod:
            proj = mod.split("/")[-1]
        else:
            proj = mod

        print(proj)
    exit()

print("total projects to be updated:"+str(totup))
print("total updates:"+str(totcom))
