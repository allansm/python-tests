from dependency import *
include("../../python-lib")

from fileHandle import *
from os import chdir
from zip import *
from argsHandle import *
from os import system

args = getArgs(["zip","action"])

path = realpath(args.zip)

chdir(getTemp())
remove("7z")
mkdir("7z")
chdir("7z")

extract(path)

system(args.action)

chdir("..")

remove("7z")

