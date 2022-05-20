from os import system, environ, getenv, getcwd
from os.path import realpath

from allansm.argsHandle import *

command = getArgs(["command"]).command

msys2 = getenv("msys2")

if(msys2 == "" or msys2 == None):
    raise Exception("please add msys2 environment variable")

environ["MSYSTEM"] = "MINGW64"

cd = "/"+realpath(getcwd()).replace(":", "").replace("\\", "/")

base = msys2+"\\usr\\bin\\bash --login -i -c "
bash = lambda x: system(base+'"cd '+cd+' ; '+x+'"')

bash(command)
