import sys

sys.path.append("../functions")

from fileHandle import *

from os import chdir
from os import system
from os import getcwd

def run():
    flag = False

    paths = getLines(".config")
    i=0
    for path in paths:
        print(str(i)+" : "+path)
        i = i+1

    index = input("index :")

    chdir(paths[int(index)])
    
    while(True):
        command = input(getcwd().replace(":\\",".").replace("\\",".").replace(" ","")+".")
        if("cd " in command):
            chdir(command.replace("cd ",""))
        elif(command == "select"):
            i=0
            for path in paths:
                print(str(i)+" : "+path)
                i = i+1

            index = input("index :")

            chdir(paths[int(index)])
        
        else:
            system(command) 
run()
