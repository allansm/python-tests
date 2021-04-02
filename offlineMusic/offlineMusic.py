from os import system

import sys
sys.path.append("../functions")

from fileHandle import *
from timeHandle import * 

fname = getTemp()+"\\music.txt"
path = input("music path:")

def getMusic(folder):
    log = getTemp()+"\\offlinemusic.log";
    writeFile(log,getDate()+" - "+getTime()+" refill \n")

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
        getMusic(path)

    if exists(fname):
        system("ffplay -autoexit -nodisp \""+consumeLineAndShuffle(fname,0)+"\"")

