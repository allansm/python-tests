import sys
sys.path.append("../functions")

from subprocess import check_output
from os import system
from time import sleep
from util import *
from argsHandle import *

def inspect(limit,op):
    totalmem = 0
    totalexe = 0
    totaldet = 0
    totaldetmem = 0
    
    if(limit == None):
        limit = 50000
    else:
        limit = int(limit)


    output = check_output("tasklist",shell=True)

    list = str(output).split("\\r\\n")

    for item in list:
        if(item != "" and " K" in item):
            array = item.split(" ")

            array = removeEmpty(array) 

            if("exe" in array[0]):
                exe = array[0]
                pid = array[1]
                memory = array[4].replace(".","")
                

                if(int(memory) > limit):
                    print(exe)
                    
                    if(op == "kill"):
                        system("taskkill /f /pid "+pid)

                    totaldet = totaldet + 1
                    totaldetmem = totaldetmem + int(memory)

                totalmem = totalmem + int(memory)
                totalexe = totalexe + 1
    
    print("")
    print("memory in use:"+str(totalmem/1000))
    print("memory by detection:"+str(totaldetmem/1000))
    print("n:"+str(totalexe))
    print("total detections:"+str(totaldet))

def console():
    args = getArgs(["limit","op"],"")
    
    limit = args.limit
    op = args.op

    inspect(limit,op)
    sleep(5)
    clear()

while(True):
    console()
