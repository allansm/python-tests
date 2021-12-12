import sys
sys.path.append("../../python-lib")

from imageHandle import *
from fileHandle import getTemp,mkdir
from os import chdir,getcwd
from time import sleep
from argsHandle import *

interval = getArgs(["--interval"]).interval

if(interval == None):
    interval = 1
else:
    interval = int(interval)

chdir(getTemp())
mkdir("test")
chdir("test")

print(getcwd())

i=0
while(True):
    print(i)
    screenshot().save(str(i)+".png")
    i+=1
    sleep(interval)
