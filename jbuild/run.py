import os
from subprocess import call
pdir = os.path.dirname(os.path.realpath(__file__))
wdir = os.getcwd()
os.chdir(pdir)

import sys
sys.path.append("../functions")

from fileHandle import *

os.chdir(wdir)

bin = getAllFiles("bin")

i = 0

package = []

for b in bin:
    p = b.split(".")[0]
    p2 = p.split("\\")
    tmp = "."
    tmp = tmp.join(p2)
    package.append(tmp.replace("bin.",""))
    print(str(i)+" : "+package[i])
    i = i + 1

index = int(input("index:"))

cn = package[index].split(".")[-1]

try:
    os.mkdir("bat")
except:
    dummy = ""

call("echo @echo off > bat/"+cn+".bat",shell=True)
call("echo cd .. >> bat/"+cn+".bat",shell=True)
call("echo java -classpath bin "+package[index]+" >> bat/"+cn+".bat",shell=True)

call("java -classpath bin "+package[index],shell=True)

