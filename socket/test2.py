import sys
sys.path.append("../../python-lib")

from allansm.socketHandle import *
from allansm.file import *
import allansm.zip as zip
from allansm.fileHandle import getTemp,mkdir
from os import getcwd,chdir

def run(s):
    global bytes

    data = receive(s)

    send(s,http("","*"))
    send(s,bytes)

    print("ok")

chdir(getTemp())
mkdir("stest")
chdir("stest")

print(getcwd())

mkdir("test")
hello = File("test/hello.txt")
hello.write("helloworld")

zip.dir("tmp","test")
tmp = File("tmp.zip")

bytes = tmp.bytes()
tmp.remove()

while(True):
    server(54321,run,1,"127.0.0.1")

