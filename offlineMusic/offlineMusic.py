from os import system
from os import chdir
from os import mkdir
from random import shuffle
from shutil import copyfile


import sys
sys.path.append("../functions")

from fileHandle import *
from timeHandle import *

def createList(mpath):
    if(exists("persistence.txt")):
        copyfile("persistence.txt","music.txt")
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

writeFile("last.txt",mpath)



while(True):
    if isEmpty("music.txt"):
        createList(mpath)

    mp3 = consumeLine("music.txt",0)
    
    writeFile("music.log",removeBreakLine(mp3)+"\n")
    
    system("ffplay -autoexit -nodisp \""+mp3+"\"")

