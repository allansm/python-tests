from os import system
from os import chdir
from os import mkdir
from random import shuffle

import sys
sys.path.append("../functions")

from fileHandle import *
from timeHandle import *

def createList(mpath):
    files = ls(mpath,"*.mp3")

    shuffle(files)
    shuffle(files)
    shuffle(files)

    remove("music.txt")
    writeLines("music.txt",files)
    writeFile("music.log","new list created\n")


mpath = input("music path:")

chdir(getTemp())

try:
    mkdir("offmusic")

except:
    print("folder exists..\n")

chdir("offmusic")

while(True):
    if isEmpty("music.txt"):
        createList(mpath)

    mp3 = consumeLine("music.txt",0)
    
    writeFile("music.log",removeBreakLine(mp3)+"\n")
    
    system("ffplay -autoexit -nodisp \""+mp3+"\"")
