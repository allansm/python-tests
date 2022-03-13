from allansm.socketHandle import *
from allansm.fileHandle import remove,ls
from allansm.downloader import *
from allansm.zip import unzip
from allansm.argsHandle import *

port = getArgs(["--port"]).port
if(port == None):
    port = "54321"

download("http://"+input("ip:")+":"+port,"tmp.zip")

unzip("tmp.zip","tmp")

remove("tmp.zip")

for n in ls("tmp"):
    print(n)

input("")

remove("tmp")
