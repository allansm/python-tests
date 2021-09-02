import dependency
from fileHandle import *

def getSize():
    size = 0

    files = getAllFilesPath(".")

    for f in files:
        size += os.path.getsize(f)

    print(str(size/1000000)+" mb")

getSize()
