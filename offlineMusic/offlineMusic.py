from os import system

import sys
sys.path.append("../functions")

from fileHandle import *

fname = getTemp()+"\\music.txt"
path = input("music path:")

def getMusic(folder):
    system("dir /B \""+folder+"\" > "+fname)

    lines = getLines(fname)

    shuffleLines(lines,fname)

    for line in lines:
        print(line)

getMusic(path)

while True:
    if isEmpty(fname):
        getMusic(path)
    system("ffplay -autoexit -nodisp \"e:/music/"+consumeLine(fname,0)+"\"")

