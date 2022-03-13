from allansm.imageHandle import *
from allansm.fileHandle import getTemp,mkdir,remove
from os import chdir,getcwd
from time import sleep
from allansm.argsHandle import *

interval = getArgs(["--interval"]).interval

if(interval == None):
    interval = 1
else:
    interval = float(interval)

chdir(getTemp())
remove("capture-loop")
mkdir("capture-loop")
chdir("capture-loop")

print(getcwd())

i=0
while(True):
    print(i)
    screenshot().save(str(i)+".png")
    i+=1
    sleep(interval)
