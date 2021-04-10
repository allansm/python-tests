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

i=0

while True:
    if isEmpty(fname):
        getMusic(path)
        i=0

    if exists(fname):
        try:
            system("ffplay -autoexit -nodisp \""+consumeLineAndShuffle(fname,0)+"\"")
            writeFile(getTemp()+"\\offlinemusic.log",i+"\n")
        
        except:
            print("file not found!!")
