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

notifu = selfLocation(__file__)+"\\bin\\notifu"

def ignore(fname,link):
    if(fname != ""):
        lines = getLines(fname)
        for line in lines:
            if(line == link):
                return True

    return False

def generatePlaylists(list):
    if(not "list=" in list):
        tmpname = list.split("v=")[-1]
        if(not exists("playlists/"+tmpname)):
            writeFile("playlists/"+tmpname,list)

        return tmpname

    else:
        tmpname = list.split("list=")[-1]
        if(not exists("playlists/"+tmpname)):
            call("youtube-dl --get-id "+list+" > persistence.txt",shell=True)

            lines = getLines("persistence.txt")
            del lines[-1]

            for line in lines:
                line = "https://www.youtube.com/watch?v="+line+"\n"
                writeFile("playlists/"+tmpname,line)
        
        return tmpname

def play(ig,playlists):
    SUPRESS = open(os.devnull, 'w')

    #playlists = getAllFiles("playlists")
    lines = []
    for pl in playlists:
        print("getting lines..")
        try:
            lines = lines + getLines(pl)
        except:
            print("erro on:"+pl)
    
    print(lines)

    for x in range(randrange(5,11)):
        print("shuffle:"+str(x))
        shuffle(lines)

    for x in range(randrange(5,11)):
        print("fake:"+str(x))
        lines = fakeshuffle(lines)

    for line in lines:
        print("checking...")
        if(not ignore(ig,line) and not line == ""):
            writeFile(".log",line+"\n")
            
            #specify all path for linux
            call("youtube-dl -x --audio-format mp3 -o \""+getTemp()+"ytplaylist/%(title)s-%(id)s.%(ext)s\" "+line,shell=True,stdout=SUPRESS)
            
            try:
                mp3 = ls(".","*.mp3")[0]
                mp3msg = mp3.replace(".\\","")
                mp3msg = mp3msg.replace(".mp3","")

                print("\nlistening:"+line+"\nmp3:"+mp3msg)
                if(isWindows()):
                    call("@echo off",shell=True)
                    call("taskkill /f /im notifu.exe 2>NUL",shell=True,stdout=SUPRESS)
                    call("start \"\" \""+notifu+"\" /m \"\\n"+mp3msg+"\" /p \"Listening\" /t none /i %SYSTEMROOT%\\system32\\imageres.dll,10 /q",shell=True)

                call("ffplay -nodisp -autoexit -loglevel 0 \""+mp3+"\"",shell=True)

            except:
                writeFile(".log","file not found.\n")
                print("file not found.")
                    
            remove(mp3)
        else:
            print("ignored:"+line)

def useFile(fname,ignore):
    try:
        mkdir("playlists")
    except:
        dummy = ""

    playlists = []

    if(not fname.startswith("http")):
        if(exists(fname)):
            print("file exists : ok")
            lines = getLines(fname)
            
            #remove this
            #shuffle(lines)
            
            for line in lines:
                if(not line.startswith("#")):
                    if(not line.startswith("https://www.youtube.com/playlist?list=")):
                        print(line)
                        list = getListLink(line)
                    else:
                        list = line

                    print("getting links from list...")
                    
                    #this is a test
                    #getLinksFromList(list)
                    '''                    
                    if(not "list=" in list):
                        tmpname = list.split("v=")[-1]
                        if(not exists("playlists/"+tmpname)):
                            writeFile("playlists/"+tmpname,line)

                        playlists.append("playlists/"+tmpname)
                    else:
                        tmpname = list.split("list=")[-1]
                        if(not exists("playlists/"+tmpname)):
                            call("youtube-dl --get-id "+list+" > persistence.txt",shell=True)
            
                            lines = getLines("persistence.txt")
                            del lines[-1]

                            for line in lines:
                                line = "https://www.youtube.com/watch?v="+line+"\n"
                                writeFile("playlists/"+tmpname,line)
                        
                        playlists.append("playlists/"+tmpname)
                    '''
                    playlists.append("playlists/"+generatePlaylists(list))
                    print(playlists)
                    #end test

                    
            try:
                play(ignore,playlists)

            except:
                print("erro on play!!!")

            exit()

def deleteMp3():
    files = ls(".","*.mp3")

    for f in files:
        remove(f)

def deleteWebm():
    files = ls(".","*.webm")

    for f in files:
        remove(f)

def console():
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
    
    #remove this
    '''if(exists("play.txt")):
        if(input("use backuped list ? (y/n):") == "y"):
            if(exists("ignore.txt")):
                ignore = getLines("ignore.txt")[0]
                print("ignore:"+ignore)
            else:
                ignore = input("ignore link?\npath to txt(blank=none):")
                remove("ignore.txt")
                writeFile("ignore.txt",ignore)

            play(ignore)
            
            exit()
    '''
    remove("persistence.txt")
    #remove("play.txt")
    remove("ignore.txt")

    link = input("playlist link or txt path:")
    ignore = input("ignore link?\npath to txt(blank=none):")
    writeFile("ignore.txt",ignore)

    useFile(link,ignore)

    if(not link.startswith("https://www.youtube.com/playlist?list=")):
        list = getListLink(link)
    else:
        list = link

    #getLinksFromList(list)
    playlists = []
    playlists.append("playlists/"+generatePlaylists(link))

    play(ignore,playlists)

console()
