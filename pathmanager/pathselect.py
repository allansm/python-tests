import sys

sys.path.append("../functions")

from fileHandle import *

from os import chdir
from os import system

def run():
    paths = getLines(".config")
    i=0
    for path in paths:
        print(str(i)+" : "+path)
        i = i+1

    index = input("index :")

    chdir(paths[int(index)])
    
    command = input("command:")
    if(command == "select"):
        i = 0
        paths2 = ls(".","*")
        for path in paths2:
            print(str(i)+" : "+path)
            i = i+1

        index = input("index :")

        chdir(paths2[int(index)])
        
        command = input("command:")
    
    system(command)

run()
