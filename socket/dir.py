from allansm.socketHandle import *
from allansm.file import *
from allansm.fileHandle import getTemp,mkdir,realpath
from allansm.argsHandle import *
import allansm.zip as zip

from os import getcwd,chdir

def run(s):
    global bytes

    data = receive(s)

    send(s,http("","*"))
    send(s,bytes)

    print("ok")

args = getArgs(["path","--port"])

path = realpath(args.path)

port = args.port
if(port == None):
    port=54321
else:
    port=int(port)

chdir(getTemp())
mkdir("stest")
chdir("stest")

print(getcwd())

zip.dir("tmp",path)
tmp = File("tmp.zip")

bytes = tmp.bytes()
tmp.remove()

print("ready")

while(True):
    server(port,run)

