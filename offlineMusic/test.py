from os import system

import sys
sys.path.append("../functions")

from fileHandle import *

fname = getTemp()+"\\music.txt"

system("dir /B \"e:/music\" > "+fname)

lines = getLines(fname)

shuffleLines(lines,fname)

for line in lines:
    print(line)

system("ffplay -nodisp \"e:/music/"+consumeLine(fname,0)+"\"")
