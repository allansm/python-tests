import sys
sys.path.append("../functions")

from fileHandle import *
from re import search
from os import system
from yt import *

def console():
    print("starting..\n")
    remove("persistence.txt")

    link = input("playlist link:")
    
    if(not link.startswith("https://www.youtube.com/playlist?list=")):
        list = getListLink(link)
    else:
        list = link

    getLinksFromList(list)

    downloadAsMusic()

console()

