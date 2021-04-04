import sys
sys.path.append("../functions")

from fileHandle import *
from re import search
from os import system
from yt import *

'''def getListLink(link):
    result = search('list=(.*)&', link)
    list = result.group(1).split("&")[0]
    list = "https://www.youtube.com/playlist?list="+list
    
    print(list)

    return list

def getLinksFromList(list):
    system("youtube-dl --get-id "+list+" > persistence.txt")

    lines = getLines("persistence.txt")
    del lines[-1]

    remove("persistence.txt")
    createFile("persistence.txt")

    for line in lines:
        line = "https://www.youtube.com/watch?v="+line+"\n"
        writeFile("persistence.txt",line)

def downloadAsMusic():
    system("youtube-dl -x --audio-format mp3 -a persistence.txt")
    remove("persistence.txt")
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

console()

