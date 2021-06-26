from subprocess import call

from os import chdir
from os import mkdir
from random import shuffle
from shutil import copyfile


import sys
sys.path.append("../functions")

from fileHandle import *
from timeHandle import *
from util import *

def createList(mpath):
    if(exists("persistence.txt")):
        lines = getLines("persistence.txt")
        shuffled = fakeshuffle(lines)
        writeLines("music.txt",shuffled)
    else:
        files = ls(mpath,"*.mp3")

        shuffle(files)
        shuffle(files)
        shuffle(files)

        remove("music.txt")
        writeLines("music.txt",files)
        writeFile("music.log","new list created\n")
        copyfile("music.txt","persistence.txt")


mpath = input("music path:")

chdir(getTemp())



try:
    mkdir("offmusic")

except:
    print("folder exists..\n")

chdir("offmusic")

try:
    if(mpath != getLines("last.txt")[0]):
        remove("music.txt")
        remove("persistence.txt")
except:
    print("error!!")

remove("last.txt")
writeFile("last.txt",mpath)



while(True):
    if isEmpty("music.txt"):
        createList(mpath)

    mp3 = consumeLine("music.txt",0)
    
    writeFile("music.log",removeBreakLine(mp3)+"\n")
    
    print("listening:"+mp3)

    call("ffplay -autoexit -nodisp -loglevel 0  \""+mp3+"\"",shell=True)


