import sys
sys.path.append("../functions")

from fileHandle import *
from re import search
from os import system
from youtube import *
from os import chdir
from os import mkdir
from os import getcwd

def console():
    info = getInfo(input("playlist link:"))

    links = getLinks(info)
    
    chdir(getTemp())

    try:
        mkdir("ytdownloads")
    except:
        dummy = ""

    chdir("ytdownloads")
    
    print("your files will be downloaded in :"+getcwd())

    for link in links:
        print("downloading : "+link+"...")
        downloadMp3(link)        

console()

