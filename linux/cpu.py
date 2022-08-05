from subprocess import check_output
from time import sleep
from os import system
import os
import argparse

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--loop",action="store_true", dest="loop")

    return parser.parse_args()

def getCpu():
    command = "ps -e -o %c, -o %cpu"

    out = check_output(command, shell=True).decode()
    cpus = check_output("lscpu | egrep 'CPU\(s\)'", shell=True).decode().split("\n")[0].split(" ")[-1]
    cpus = int(cpus)

    data = []

    for n in out.split("\n"):
        tmp = n.split(",")
        if(len(tmp) > 1):
            program = tmp[0].strip()
            cpu = tmp[1].strip()
            if(program != "COMMAND"):
                data.append({"program":program, "cpu":cpu})

    cpu = {}

    cpu["total in use"] = 0.0

    for n in data:
        cpu[n["program"]] = 0.0

    for n in data:
        try:
            cpu[n["program"]]+=float(n["cpu"])/cpus
            cpu["total in use"]+=float(n["cpu"])/cpus
        except Exception as e:
            pass
    
    return cpu

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
