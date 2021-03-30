import os
import random

def createFile(fname):
    open(fname,"x")

def writeFile(fname,txt):
    f = open(fname,"a")
    f.write(txt)
    f.close()

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
    for line in lines:
        if index != i:
            writeFile(fname,line+"\n")
        index+=1
    return lines[i]

