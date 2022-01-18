from dependency import *

include("../../python-lib")

from allansm.file import *
from allansm.util import exec
from allansm.argsHandle import *
from os import system,chdir

def boot(start=True):
    machine = None

    while(True):
        if(machine == None):            
            machines = ""
            for n in exec("vboxmanage list vms"):
                machines+=n

            machines = machines.replace("\"","\n\n").split("\n\n")
            
            print("\nmachines{")
            for n in machines:
                if(not "{" in n and n != ""):
                    print("     "+n.replace("\n",""))
            
            print("}\n") 
             
            machine = input("machine name:")
        

        status = ""
        if(start):
            for n in exec("vboxmanage startvm "+machine):
                status+=n

        print(status)
        if("success" in status or not start):
            while(True):
                op = input(machine+">")

                if(op == "quit"):
                    system("vboxmanage controlvm "+machine+" savestate")
                    exit()

                elif(op == "net"):
                    net = input("on/off:")
                    system("VBoxManage controlvm "+machine+" setlinkstate1 "+net)
                
                elif(op == "save"):
                    system("vboxmanage controlvm "+machine+" savestate")

                elif(op == "boot"):
                    start = True
                    break
                
                elif(op == "help"):
                    print("\ncommands{")
                    for n in ["boot","save","net","quit"]:
                        print("     "+n)

                    print("}\n")

config = File(".config")

if(not config.exists()):
    config.write(input("virtualbox path:"))

try:
    chdir(config.read()) 
except:
    config.remove()

boot(getArgs(["?boot"]).boot)

