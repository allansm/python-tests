import sys
sys.path.append("../functions")

from fileHandle import *
from re import search
from os import system

def getListLink(link):
    if "&" in link.split("list=")[1]:
        result = search('list=(.*)&', link)
        list = result.group(1).split("&")[0]
        list = "https://www.youtube.com/playlist?list="+list
        
        print(list)

        return list

    list = "https://www.youtube.com/playlist?list="+link.split("list=")[1];
    print(list)
    return list;

def getLinksFromList(list):
    system("youtube-dl --get-id "+list+" > "+getTemp()+"persistence.txt")

    lines = getLines(getTemp()+"persistence.txt")
    del lines[-1]

    remove(getTemp()+"persistence.txt")
    createFile(getTemp()+"persistence.txt")

    for line in lines:
        line = "https://www.youtube.com/watch?v="+line+"\n"
        writeFile(getTemp()+"persistence.txt",line)

def downloadAsMusic():
    system("youtube-dl -x --audio-format mp3 -a "+getTemp()+"persistence.txt")
    remove(getTemp()+"persistence.txt")

