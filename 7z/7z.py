from dependency import *
include("../../python-lib")

from fileHandle import *
from os import chdir
from zip import *
from argsHandle import *
from os import system
from elapse import *
from util import exec,echo

args = getArgs(["zip","action"])

path = realpath(args.zip)

if(exists(path)):
    chdir(getTemp())
    remove("7z")
    mkdir("7z")
    chdir("7z")

    e = Elapse()
    exec('7z x "'+path+'"')
    echo("elapsed:")
    e.show(0.001)

    system(args.action)

    chdir(getTemp())

    remove("7z")

