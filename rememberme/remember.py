import sys
sys.path.append("../functions")

from fileHandle import *
import datetime
import datetime

def showRegister():
    now = datetime.datetime.now()
    now = str(now)
    date = now.split(" ")[0]
    fname = "data/"+date
    lines = getLines(fname)
    for line in lines:
        print(line)

def register():
    now = datetime.datetime.now()
    now = str(now)
    date = now.split(" ")[0]
    fname = "data/"+date
    time = now.split(" ")[1].split(".")[0]

    register = input("thing to remember:")
    register = register+"\n"

    writeFile(fname,time+":"+register)

def console():
    while True:
        op = input("1: register 2: get today register:")
        if int(op) == 1:
            register()
        else:
            showRegister()

console()
