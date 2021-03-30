import sys
sys.path.append("../functions")

from fileHandle import *
from timeHandle import *

def showRegister(): 
    fname = "data/"+getDate()
    lines = getLines(fname)
    for line in lines:
        print(line)

def register(): 
    fname = "data/"+getDate()

    register = input("thing to remember:")
    register = register+"\n"

    writeFile(fname,getTime()+":"+register)

def console():
    while True:
        print("current time:"+getTime())
        op = input("1: register 2: get today register:")
        if int(op) == 1:
            register()
        else:
            showRegister()

console()
