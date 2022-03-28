from allansm.fileHandle import *
from os import system

path = ""
for n in ls():
    if(n != ".\\apps.py"):
        path+=";"+realpath(n)
    
    for x in ls(n):
        if("bat" in x and not ".bat" in x):
            path+=";"+realpath(x)

writeFile(".bat","setx apps "+path)
system(".bat")
remove(".bat")
