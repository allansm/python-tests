from os import system
from os import chdir
from os import mkdir
from random import shuffle

import sys
sys.path.append("../functions")

from fileHandle import *
from timeHandle import *

def createList():
    files = ls("e:\music","*.mp3")

    shuffle(files)

    remove("music.txt")
    writeLines("music.txt",files)


chdir(getTemp())

try:
    mkdir("offmusic")

except:
    print("folder exists..\n")

chdir("offmusic")

while(True):
    if isEmpty("music.txt"):
        createList()

    system("ffplay -autoexit -nodisp \""+consumeLine("music.txt",0)+"\"")

