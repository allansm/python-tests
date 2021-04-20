import sys
sys.path.append("../functions")

from fileHandle import *
from timeHandle import *

def showRegister(fname): 
    lines = getLines(fname)
    for line in lines:
        print(line)

def register(fname): 
    register = input("thing to remember:")
    register = register+"\n"
    if fname == "data/important":
        writeFile(fname,getDate()+" - "+getTime()+" : "+register)
    else:    
        writeFile(fname,getTime()+":"+register)

def console():
    while True:
        print("current time:"+getTime())
        op = input("1: register 2: get today register 3: register important things 4: get important registers:")
        if int(op) == 1:
            register("data/"+getDate())
        elif int(op) == 2:
            showRegister("data/"+getDate())
        elif int(op) == 3:
            register("data/important")
        elif int(op) == 4:
            showRegister("data/important")

console()
