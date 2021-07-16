import sys
sys.path.append("../functions")

from fileHandle import *
from re import search

from subprocess import call
from os import getcwd
from os import chdir
from os import mkdir
import os

from youtube import *
import youtube

from urllib import request


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

def download(url,fname):    
    request.urlretrieve(url, fname)


def downloadMp3(link,folder):
    cdir = getcwd()
    
    chdir(folder)
    
    try:
        youtube.downloadMp3(link)
    except:
        print("erro downloading...")

    chdir(cdir)


def generatePlaylists(list):
    if(os.path.isdir(list)):
        tmpname = os.path.basename(list)
        if(not exists("playlists/"+tmpname)):
            lines = getAllFiles(list)
            for line in lines:
                writeFile("playlists/"+tmpname,line+"\n")
        
        return tmpname

    elif(not "list=" in list):
        tmpname = list.split("v=")[-1]
        if(not exists("playlists/"+tmpname)):
            writeFile("playlists/"+tmpname,list)

        return tmpname

    else:
        tmpname = list.split("list=")[-1]
        if(not exists("playlists/"+tmpname)):
            info = getInfo(list)
            print(getTitle(info)+" ok")
            lines = getLinks(info)
            
            for line in lines:
                line = line+"\n"
                writeFile("playlists/"+tmpname,line)
        
        return tmpname

