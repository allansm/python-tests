import sys
sys.path.append("../functions")

from fileHandle import *
from yt import *
from random import shuffle
from os import chdir
from subprocess import call
from os import mkdir
from os import system
from util import *
from random import randrange
from ff import *

import argparse

#headless functions
def log(msg,f):
    writeFile(f,msg)

def storeCurrent(cur):
    remove("current.txt")
    writeFile("current.txt",cur)


def ignore(fname,link):
    if(fname != ""):
        lines = getLines(fname)
        for line in lines:
            if(line == link):
                return True

    return False


def build():
    chdir(getTemp())

    try:
       mkdir("ytplaylist")
    except:
        print("folder exists...")

    chdir("ytplaylist")
    
    try:
        mkdir("playlists")
    except:
        dummy = ""


    deleteMp3()
    deleteWebm()
    
    remove("persistence.txt")
    remove("ignore.txt")

def shuffleLines(lines):
    for x in range(randrange(5,11)):
        shuffle(lines)

    for x in range(randrange(5,11)):
        lines = fakeshuffle(lines)
    
    return lines

def eqMerge(mat):
    big = 0

    for m in mat:
        if(len(m) > big):
            big = len(m)

    print(big)

    arr = []

    for i in range(big):
        for m in mat:
            try:
                arr.append(m[i])
            except:
                error = ""

    return arr


def getMp3():
    mp3 = ls(".","*.mp3")[0]
    mp3msg = mp3.replace(".\\","")
    mp3msg = mp3msg.replace(".mp3","")

    arr = []
    arr.append(mp3)
    arr.append(mp3msg)

    return arr

def getPlaylistsLines(playlists):
    mat = []
    playlists = shuffleLines(playlists)
    for pl in playlists:
        print("getting lines..")
        try:
            lines = []
            print(pl)
            lines = shuffleLines(getLines(pl)) 
            mat.append(lines)
        except:
            print("erro on:"+pl)
    
    return eqMerge(mat)

def deleteMp3():
    files = ls(".","*.mp3")

    for f in files:
        remove(f)

def deleteWebm():
    files = ls(".","*.webm")

    for f in files:
        remove(f)

def playFolder(link):
    quit = False
    try:
        if os.path.isdir(link):
            quit = True
            files = getAllFiles(link)
            files = shuffleLines(files)

            for f in files:
                if "mp3" in f:
                    fn = getFileName(f)
                    if(f.replace(fn,"").replace("/","\\") == link.replace("/","\\")+"\\"):
                        print(f)
                        playSound(f)

        exit()
    except:
        dummy = ""
    
    if(quit):
        exit()

#main functions
def play(ig,playlists):
    lines = getPlaylistsLines(playlists)
    
    for line in lines:
        print("checking...")
        if(not ignore(ig,line) and not line == ""):
            if "mp3" in line:
                playSound(line)
            else:
               
                downloadMp3(line,getTemp()+"ytPlaylist")

                try:
                    mp3 = getMp3()

                    print("\nlistening:"+line+"\nmp3:"+mp3[1])
                    
                    toast(mp3[1],"Listening",selfLocation(__file__)+"\\bin\\notifu")
                    
                    #test
                    
                    storeCurrent(line)

                    log(line+" "+mp3[1]+"\n",".log")
                    #

                    playSound(mp3[0])


                except:
                    writeFile(".log","file not found.\n")
                    print("file not found.")

                try:        
                    remove(mp3[0])
                except:
                    dummy = ""

        else:
            print("ignored:"+line)

def useFile(fname,ignore): 
    playlists = []

    if(not fname.startswith("http")):
        if(exists(fname)):
            print("file exists : ok")
            lines = getLines(fname)
                       
            for line in lines:
                if(not line.startswith("#")):
                    if(not line.startswith("https://www.youtube.com/playlist?list=")):
                        list = getListLink(line)
                    else:
                        list = line

                    print("getting links from list...")
                    
                    playlists.append("playlists/"+generatePlaylists(list))
                    
            try:
                play(ignore,playlists)

            except:
                print("erro on play!!!")

            exit()

def console():
    build()
     
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--link",required=False)
    parser.add_argument("--ignore",required=False)
    
    args = parser.parse_args()
    
    link = args.link if args.link != None else input("playlist link or txt path:")
    ignore = args.ignore if args.ignore != None else iinput("ignore link?\npath to txt(blank=none):")
    
    playFolder(link)
    
    writeFile("ignore.txt",ignore)

    useFile(link,ignore)

    if(not link.startswith("https://www.youtube.com/playlist?list=")):
        list = getListLink(link)
    else:
        list = link

    playlists = []
    playlists.append("playlists/"+generatePlaylists(list))

    play(ignore,playlists)

console()
