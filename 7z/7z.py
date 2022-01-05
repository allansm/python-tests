from dependency import *
include("../../python-lib")

from fileHandle import *
from os import chdir
from zip import *
from argsHandle import *
from os import system
from elapse import *

args = getArgs(["zip","action"])

path = realpath(args.zip)

chdir(getTemp())
remove("7z")
mkdir("7z")
chdir("7z")

e = Elapse()
extract(path)
e.show(0.001)

system(args.action)

chdir("..")

remove("7z")

