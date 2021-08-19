from random import shuffle
import platform
from subprocess import call
import os
from os import system

from urllib import request

import json
from urllib.request import urlopen

from os import getcwd
from os import chdir


def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

def fakeshuffle(arr):
    h1,h2 = split_list(arr)

    a,b = split_list(h1)
    c,d = split_list(h2)

    shuffle(a)
    shuffle(a)
    shuffle(a)
    shuffle(a)

    shuffle(b)
    shuffle(b)
    shuffle(b)

    shuffle(c)
    shuffle(c)
    shuffle(c)

    shuffle(d)
    shuffle(d)
    shuffle(d)
    shuffle(d)

    arr = a+b+c+d

    return arr

def isWindows():
    if(platform.system() == "Windows"):
        return True
    
    return false

#require notifu on windows blank on linux
def toast(message,title,exe=""):
    SUPRESS = open(os.devnull, 'w')

    if(isWindows()):
        call("@echo off",shell=True)
        call("taskkill /f /im notifu.exe 2>NUL",shell=True,stdout=SUPRESS)
        call("start \"\" \""+exe+"\" /m \"\\n"+message+"\" /p \""+title+"\" /t none /i %SYSTEMROOT%\\system32\\imageres.dll,10 /q",shell=True)
    else:
        call("notify-send \""+title+"\" \""+message+"\"")

clear = lambda: system("cls" if os.name=="nt" else "clear")
removeEmpty = lambda array: [i for i in array if i]

removeRedundant = lambda array: list(dict.fromkeys(array))

def download(url,fname):    
    request.urlretrieve(url, fname)

def getJson(url):
    response = urlopen(url)
    data = json.loads(response.read().decode())

    return data

def do(that,inside):
    tmp = getcwd()

    chdir(inside)
    val = that()
    chdir(tmp)
    
    return val

def showOptions(arr):
    i = 0
    for a in arr:
        print(str(i)+" : "+a)
        i = i + 1


