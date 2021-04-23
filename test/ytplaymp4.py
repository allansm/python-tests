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
    lines = getLines(fn)

    shuffled = fakeshuffle(lines)

    writeLines("persistence.txt",shuffled)

def play(fn):
    while True:
        if(not exists("persistence.txt")):
            createList(fn)
        else:
            call("youtube-dl --get-url --format best "+consumeLine("persistence.txt",0)+" > current",shell=True)
            call("ffplay -an -noborder -x 300 -y 200 -top 0 -left 0 "+consumeLine("current",0))
                
redirect()

play(input("links file url:"))
