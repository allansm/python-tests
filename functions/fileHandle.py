import os
from glob import glob
import random
from tempfile import gettempdir
from urllib.parse import urlparse
from os.path import dirname
from os.path import realpath

#use __file__
def selfLocation(f=__file__):
    return dirname(realpath(f))

def selfFileLocation(f=__file__):
    return os.path.realpath(f)

def removeBreakLine(string):
    return string.replace("\n","").replace("\r","")


def createFile(fname):
    try:
        open(fname,"w")
    except:
        print("...")

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

def exists(fname):
    if os.path.exists(fname):
        return True
    else : 
        return False

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
    return gettempdir()+"/"

def consumeLine(fname,i):
    lines = getLines(fname)
    index = 0
    
    txt = ""
    for line in lines:
        if index != i:
            if line != "":
                
                txt = txt+line+"\n"
        index+=1
    
    remove(fname)
    writeFile(fname,txt)

    return lines[i]

def consumeLineAndShuffle(fname,i):
   line = consumeLine(fname,i)
   lines = getLines(fname)
   shuffleLines(lines,fname)
   return line

def isEmpty(fname):
    if os.path.exists(fname):
        if os.path.getsize(fname) == 0:
            return True
        else:
            return False
    else:
        return True

def ls(path,extension):
    return glob(path+"/"+extension)

def getAllFiles(path):
    fold = os.walk(path)
    ret = []
    for root, dirs, files in fold:
        for name in files:
            ret.append(os.path.join(root, name))

    return ret

def getAllFilesPath(path):
    fold = os.walk(path)
    ret = []
    for root, dirs, files in fold:
        for name in files:
            ret.append(os.path.realpath(os.path.join(root, name)))

    return ret

def getAllPaths(path):
    fold = os.walk(path)
    ret = []
    for root, dirs, files in fold:
        for name in dirs:
            ret.append(os.path.realpath(os.path.join(root, name)))

    return ret


def getFileName(path):
    name = urlparse(path)
    return os.path.basename(name.path)

