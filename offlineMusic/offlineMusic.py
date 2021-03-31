from os import system

import sys
sys.path.append("../functions")

from fileHandle import *

fname = getTemp()+"\\music.txt"
path = input("music path:")

def getMusic(folder):
    fname = getTemp()+"\\music.txt"
    remove(fname)   

    ltos = ls(folder,"*.mp3")    

    writeLines(fname,ltos)

    lines = getLines(fname)

    shuffleLines(lines,fname)

    for line in lines:
        print(line)

if isEmpty(fname):
    getMusic(path)

while True:
    if isEmpty(fname):
        getMusic(path+"\\*.mp3")
    system("ffplay -autoexit -nodisp \""+consumeLine(fname,0)+"\"")

