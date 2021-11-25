import dependency
from fileHandle import *
from util import clear

size = 0

def lamb(f): 
    global size

    size += os.path.getsize(f)
    print(str(size/1000000)+" mb")

def getSize():
    files = getAllFilesPath(".",lamb)

getSize()
