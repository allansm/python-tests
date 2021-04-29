import sys

sys.path.append("../functions")

from fileHandle import *
from subprocess import call
from os import chdir
from os import mkdir
from util import *

def redirect():
    chdir(getTemp())

    try:
        mkdir("ytplaymp4")
    except:
        print("...")

    chdir("ytplaymp4")

def createList(fn):
    remove("last")
    writeFile("last",fn)

    lines = getLines(fn)

    shuffled = fakeshuffle(lines)
    
    for line in shuffled:
        print(line)

    writeLines("persistence.txt",shuffled)
    print("persistence created...")

def play(fn,miniature):
    while True:
        if(exists("last")):
            if(fn != getLines("last")[0]):
                remove("persistence.txt")

        if(not exists("persistence.txt")):
            createList(fn)
        else:
            call("youtube-dl --get-url --format best "+consumeLine("persistence.txt",0)+" > current",shell=True)
            
            consumed = consumeLine("current",0)
            print("consumed:"+consumed)
            
            if(miniature == "y"):
                call("ffplay -an -x 300 -y 200 -top 28 -left 1000 -alwaysontop -noborder -framedrop -autoexit \""+consumed+"\"",shell=True)
            else:
                call("ffplay -an -x 1366 -y 768 -noborder -framedrop -autoexit \""+consumed+"\"",shell=True)

redirect()

play(input("links file url:"),input("miniature(y/n):"))

