from dependency import *

include("../../python-lib")

from allansm.file import *
from os import system,chdir
from allansm.util import exec

config = File(".config")

if(not config.exists()):
    config.write(input("virtualbox path:"))

try:
    chdir(config.read()) 
except:
    config.remove()

machine = input("machine name:")

status = ""
for n in exec("vboxmanage startvm "+machine):
    status+=n

print(status)
if("success" in status):
    while(True):
        op = input(machine+">")

        if(op == "quit"):
            system("vboxmanage controlvm "+machine+" savestate")
            exit()

        elif(op == "net"):
            net = input("on/off:")
            system("VBoxManage controlvm "+machine+" setlinkstate1 "+net)
else:
    print(":(")
