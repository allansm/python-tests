from allansm.imageHandle import *
from allansm.fileHandle import getTemp, mkdir, remove, getFileName, ls
from allansm.argsHandle import *
from os import chdir,getcwd
from time import sleep

args = getArgs(["--interval", "?resume"])

interval = args.interval

if(interval == None):
    interval = 1
else:
    interval = float(interval)

chdir(getTemp())

if(not args.resume):
    remove("capture-loop")

mkdir("capture-loop")
chdir("capture-loop")

print(getcwd())

i=0

if(args.resume):
    for n in ls():
        h = int(getFileName(n).split(".")[0])

        if(h > i):
            i=h

while(True):
    print(i)
    screenshot().save(str(i)+".png")
    i+=1
    sleep(interval)
