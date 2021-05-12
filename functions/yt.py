import sys
sys.path.append("../functions")

from fileHandle import *
from re import search

from subprocess import call
from os import getcwd

def getListLink(link):
    if "list=" not in link:
        return link

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
    call("youtube-dl --get-id "+list+" > persistence.txt",shell=True)
    
    lines = getLines("persistence.txt")
    del lines[-1]

    for line in lines:
        line = "https://www.youtube.com/watch?v="+line+"\n"
        writeFile("play.txt",line)

def downloadAsMusic():
    call("youtube-dl -x --audio-format mp3 -o \""+getcwd()+"/%(title)s-%(id)s.%(ext)s\" -a "+getTemp()+"persistence.txt",shell=True)
    
    remove(getTemp()+"persistence.txt")


def downloadMp4(url):
   call("youtube-dl --format best "+url)
