import os
from glob import glob
import random

def removeBreakLine(string):
    return string.replace("\n","").replace("\r","")


def createFile(fname):
    open(fname,"x")

def writeFile(fname,txt):
    f = open(fname,"a")
    f.write(txt)
    f.close()

def writeLines(fname,lines):
    for line in lines:
        line = removeBreakLine(line)
        writeFile(fname,line+"\n")

def readFile(fname):
    f = open(fname,"r")
    return f.read()
    
def remove(fname):
    if os.path.exists(fname):
        os.remove(fname)
        
def getLines(fname):
    return readFile(fname).split("\n")
        
def shuffleLines(lines,shuffled):
    random.shuffle(lines)

    remove(shuffled)

    createFile(shuffled)

    for n in lines:
        writeFile(shuffled,n+"\n")

def getTemp():
    return os.environ.get("TEMP")

def consumeLine(fname,i):
    lines = getLines(fname)
    index = 0
    remove(fname)
    for line in lines:
        if index != i:
            if line != "":
                writeFile(fname,line+"\n")
        index+=1
    return lines[i]

def isEmpty(fname):
    if os.path.exists(fname):
        if os.path.getsize(fname) == 0:
            return True
        else:
            return False
    else:
        return False

def ls(path,extension):
    return glob(path+"/"+extension)

