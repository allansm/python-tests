import sys

sys.path.append("../functions")

from fileHandle import *
from argsHandle import *
from timeHandle import *
from os.path import realpath
from os import chdir
from os import mkdir
from os import system

path = getArgs(["path"]).path

print("getting files..")
files = getAllFilesPath(path)


chdir(getTemp())

try:
    mkdir("search")
except:
    dummy = ""


chdir("search")

found = getLines(".found")

print("making paths persistent...")
for f in files:
    
    exist = False
    
    for fo in found:
        if(fo == f):
            exist = True
            break

    if(not exist):
        writeFile(".found",f+"\n")

writeFile(".paths",path+" "+getDate()+" "+getTime()+"\n")
