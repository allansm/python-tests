import sys
sys.path.append("../functions")

#from subprocess import check_output
#from subprocess import call
#from os import system
from time import sleep
from util import *
from argsHandle import *
from proc import *

'''
def inspect(limit,op,pattern):
    pk = False
    tokill = []
    if(pattern != None):
        pk = True
        tokill = pattern.split(";")
        

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
                        call("taskkill /f /pid "+pid+" 2>NUL",shell=True,stdout=open(os.devnull, 'w'))

                    if(pk):
                        for p in tokill:
                            if(p in exe):
                                call("taskkill /f /pid "+pid+" 2>NUL",shell=True,stdout=open(os.devnull, 'w'))

                    totaldet = totaldet + 1
                    totaldetmem = totaldetmem + int(memory)

                totalmem = totalmem + int(memory)
                totalexe = totalexe + 1
    
    print("")
    print("memory in use:"+str(totalmem/1000))
    print("memory by detection:"+str(totaldetmem/1000))
    print("n:"+str(totalexe))
    print("total detections:"+str(totaldet))
'''

def test(limit,op,pattern):
    pk = False
    tokill = []
    if(pattern != None):
        pk = True
        tokill = pattern.split(";")
        

    totalmem = 0
    totalexe = 0
    totaldet = 0
    totaldetmem = 0
    
    if(limit == None):
        limit = 50000
    else:
        limit = int(limit)


    i = 0
    out = getOutput()

    nproc = getProcess(out)
    npid = getPid(out)
    nmem = getMemory(out)

    for proc in nproc:
        exe = proc
        pid = npid[i]
        memory = nmem[i]

        i = i + 1
        if(int(memory) > limit):
            print(exe)
            
            if(op == "kill"):
                kill(pid)
            if(pk):
                for p in tokill:
                    if(p.lower() in exe.lower()):
                        kill(pid)
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
    clear()
    args = getArgs(["limit","op","interval","pattern"],"")
    
    limit = args.limit
    op = args.op
    interval = args.interval
    pattern = args.pattern

    if(interval == None):
        interval = 5
    else:
        interval = int(interval)

    #inspect(limit,op,pattern)
    test(limit,op,pattern)

    sleep(interval)
    
while(True):
    console()

