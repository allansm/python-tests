import sys
sys.path.append("../functions")

from fileHandle import *
from yt import *
from random import shuffle

def play():
    lines = getLines(getTemp()+"persistence.txt")
    
    shuffle(lines)

    for line in lines:
        system("youtube-dl -x --audio-format mp3 "+line)
        mp3 = ls(".","*.mp3")[0]
        system("ffplay -nodisp -autoexit \""+mp3+"\"")
        remove(mp3)

def useFile(fname):
    if(not fname.startswith("http")):
        if(exists(fname)):
            lines = getLines(fname)
            
            shuffle(lines)
            
            for line in lines:
                if(not line.startswith("https://www.youtube.com/playlist?list=")):
                    print(line)
                    list = getListLink(line)
                else:
                    list = line


                getLinksFromList(list)
                try:
                    play()

                except:
                    print("erro on play!!!")
            exit()

def deleteMp3():
    files = ls(".","*.mp3")

    for f in files:
        remove(f)

def console():
    deleteMp3()
    remove(getTemp()+"persistence.txt")
    link = input("playlist link or txt path:")

    useFile(link)

    if(not link.startswith("https://www.youtube.com/playlist?list=")):
        list = getListLink(link)
    else:
        list = link

    getLinksFromList(list)
    
    play()

console()
