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

    system(command)

run()
