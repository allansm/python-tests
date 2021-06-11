import sys

sys.path.append("../functions")

from fileHandle import *
from argsHandle import *
from os.path import realpath
from os import chdir
from os import mkdir
from os import system

path = getArgs(["path"],"").path
#fn = input("filename:")

print("getting files..")
files = getAllFilesPath(path)
'''
fullpath = []
for f in files:
    f = realpath(f)
    fullpath.append(f)
    #writeFile(".test",f+"\n")

'''
#system("dir")
print("files stored")
print("matching..")

chdir(getTemp())

try:
    mkdir("search")
except:
    dummy = ""


chdir("search")

found = getLines(".found")

for f in files:
    #f = realpath(f)
    exist = False
    for fo in found:
        if(fo == f):
            exist = True
            #print("path exist...")
            break
    if(not exist):
        #print("add "+f)
        writeFile(".found",f+"\n")

