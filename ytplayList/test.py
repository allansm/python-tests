import sys
sys.path.append("../functions")
sys.path.append("../yt.py")

from fileHandle import *
from yt import *

def play():
    remove("playme")
    lines = getLines("persistence.txt")
    
    for line in lines:
        system("youtube-dl -x --audio-format mp3 -g "+line+" > playme")
        playme = getLines("playme")[0]
        system("ffplay -nodisp \""+playme+"\"")

def run():
    remove("persistence.txt")
    link = input("playlist link:")
    
    if(not link.startswith("https://www.youtube.com/playlist?list=")):
        list = getListLink(link)
    else:
        list = link

    getLinksFromList(list)
   
run()
play()
