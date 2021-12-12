import dependency
from fileHandle import *
from util import clear
import os

tmp = 0

def lamb(f): 
    global tmp

    tmp += size(f)
    print(str(tmp/1000000)+" mb")

def getSize():
    files = getAllFilesPath(".",lamb)

getSize()
