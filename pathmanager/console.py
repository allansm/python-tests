import sys
from os import chdir
from os.path import realpath
from os.path import dirname
chdir(dirname(realpath(__file__)))

sys.path.append("../functions")

from fileHandle import *

from os import system
from os import getcwd

def select(paths):
    i=0
    for path in paths:
        print(str(i)+" : "+path)
        i = i+1

    index = input("index :")

    chdir(paths[int(index)])


def run():
    flag = False

    paths = getLines(".config")
    select(paths)

    while(True):
        package = getcwd().split(":\\")[1].replace("\\",".").replace(" ","")
        command = input(package+".")
        if("cd " in command):
            chdir(command.replace("cd ",""))
        elif(command == "select"):
            select(paths)
        else:
            system(command) 
run()
