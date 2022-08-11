from proc import *
from os import system
import os
from time import sleep

def getRam():
    out = check_output("free | grep Mem | awk '{print $3/$2 * 100.0}'", shell=True).decode()
    out = float(out.replace("\n", "").replace(",", "."))
    return out

def show(n, percent):
    print(n, end=" ")
    print("", end = " ")
    print("█"*round(percent/5), end="")
    print("░"*round((100-percent)/5),end="")
    print(" "+("{:.3}".format(percent))+"%\n")

while(True):
    ram = getRam()
    cpu = getCpu()
    
    system("cls" if os.name=="nt" else 'printf "\033c"')
    
    show("cpu", cpu["total in use"])
    show("ram", ram)
    
    sleep(0.1)
