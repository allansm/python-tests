import sys
sys.path.append("../functions")

from fileHandle import *
from yt import *
from random import shuffle
from os import chdir
from subprocess import call

def play():
    lines = getLines(getTemp()+"play.txt")

    remove(getTemp()+"play.txt")
    
    shuffle(lines)

    for line in lines:
    
        call("youtube-dl -x --audio-format mp3 -o \""+getTemp()+"%(title)s-%(id)s.%(ext)s\" "+line,shell=True)
        mp3 = ls(".","*.mp3")[0]
        
        call("ffplay -nodisp -autoexit \""+mp3+"\"",shell=True)
        
        remove(mp3)

def useFile(fname):
    if(not fname.startswith("http")):
        if(exists(fname)):
            print("file exists : ok")
            lines = getLines(fname)
            
            shuffle(lines)
            
            for line in lines:
                if(not line.startswith("https://www.youtube.com/playlist?list=")):
                    print(line)
                    list = getListLink(line)
                else:
                    list = line

                print("getting links from list...")
                print(list)
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
    chdir(getTemp())
    
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
