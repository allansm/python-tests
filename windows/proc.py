import dependency

from subprocess import check_output
from subprocess import call
from os import system
from time import sleep
from util import *
from argsHandle import *


def getOutput():
    return check_output("tasklist",shell=True)

def getProcess(output):
    list = str(output).split("\\r\\n")
    
    procs = []

    for item in list:
        if(item != "" and " K" in item):
            array = item.split(" ")

            array = removeEmpty(array) 

            if("exe" in array[0]):
                procs.append(array[0])
    
    return procs

def getPid(output):
    list = str(output).split("\\r\\n")
    
    pids = []

    for item in list:
        if(item != "" and " K" in item):
            array = item.split(" ")

            array = removeEmpty(array) 

            if("exe" in array[0]):
                pids.append(array[1])
    
    return pids

def getMemory(output):
    list = str(output).split("\\r\\n")
        
    mem = []

    for item in list:
        if(item != "" and " K" in item):
            array = item.split(" ")

            array = removeEmpty(array) 

            if("exe" in array[0]):
                mem.append(array[4].replace(".",""))
    
    return mem

def kill(pid):
    call("taskkill /f /pid "+pid+" 2>NUL",shell=True,stdout=open(os.devnull, 'w'))

