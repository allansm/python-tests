import sys
sys.path.append("../functions")

from fileHandle import *
from yt import *

def play():
    lines = getLines("persistence.txt")
    
    for line in lines:
        system("youtube-dl -x --audio-format mp3 "+line)
        mp3 = ls(".","*.mp3")[0]
        system("ffplay -nodisp -autoexit \""+mp3+"\"")
        
def console():
    remove("persistence.txt")
    link = input("playlist link:")
    
    if(not link.startswith("https://www.youtube.com/playlist?list=")):
        list = getListLink(link)
    else:
        list = link

    getLinksFromList(list)
    
    play()

console()
