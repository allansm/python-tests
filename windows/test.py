import sys
sys.path.append("../functions")

from subprocess import check_output
from time import sleep
from util import *
from argsHandle import *

def inspect(limit):
    output = check_output("tasklist",shell=True)

    list = str(output).split("\\r\\n")

    for item in list:
        if(item != "" and " K" in item):
            array = item.split(" ")

            array = removeEmpty(array) #[i for i in array if i]
            
            if("exe" in array[0]):
                exe = array[0]
                pid = array[1]
                memory = array[4].replace(".","")
                

                if(int(memory) > limit):
                    print(exe)

def console():
    limit = getArgs(["limit"],"").limit
    
    if(limit == None):
        limit = 50000
    else:
        limit = int(limit)

    inspect(limit)
    sleep(5)
    clear()

while(True):
    console()
