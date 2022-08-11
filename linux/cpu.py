from subprocess import check_output
from proc import *
from time import sleep
from os import system
import os
import argparse

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--loop",action="store_true", dest="loop")

    return parser.parse_args()

def show(n, percent):
    print(n, end=" ")
    print(" "*(20-len(n)), end="")
    print("█"*round(percent/5), end="")
    print("░"*round((100-percent)/5),end="")
    print(" "+("{:.3}".format(cpu[n]))+"%\n")

cpu = getCpu()
for n in cpu:
    show(n, cpu[n])

while(getArgs().loop):
    cpu = getCpu()
    system("cls" if os.name=="nt" else 'printf "\033c"')
    total = 0.0
    for n in cpu:
        if(cpu[n] < 1):
            if(n != "total in use"):
                total+=cpu[n]
    
    cpu["a lot of programs"] = total
    
    for n in cpu:
        if(cpu[n] >= 1):
            show(n, cpu[n])

    sleep(1)    
