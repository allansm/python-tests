import sys
sys.path.append("../functions")

from fileHandle import *
from re import search
from os import system
from youtube import *

#deprecated
'''
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
'''
def console():
    info = getInfo(input("playlist link:"))

    links = getLinks(info)

    for link in links:
        print("downloading : "+link+"...")
        downloadMp3(link)        

console()

