import sys
sys.path.append("../functions")

from fileHandle import *

from os import mkdir
from os import system
from os import chdir

import argparse

def getArgs():
    parser = argparse.ArgumentParser(description='Optional app description')

    parser.add_argument("mainfile",type=str)
    parser.add_argument("projectfold",type=str)
    parser.add_argument("redirectto",type=str)
    
    return parser.parse_args()

def makeBat(mainclass):
    txt = "@echo off\njava "+mainclass
    remove(mainclass+".bat")
    writeFile(mainclass+".bat",txt)

def javac(mainfile,projectfold,redirectto):
    chdir(redirectto)

    try:
        mkdir("BIN")
    except:
        print("bin exist")

    try:
        mkdir("BIN\\"+projectfold)
    except:
        print("project folder exist")

    chdir(projectfold)

    system("javac -d \"..\\bin\\"+projectfold+"\" "+mainfile)

    chdir("..\\bin\\"+projectfold)

    mainclass = mainfile.split(".")[0]
    mainclass = mainclass.capitalize()
    
    makeBat(mainclass)

    system("java "+mainclass)


def console():
    args = getArgs()

    javac(args.mainfile,args.projectfold,args.redirectto)

console()
