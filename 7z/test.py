from dependency import *
include("../../python-lib")

from fileHandle import *
from os import chdir
from shutil import rmtree as remove
from zip import *
from argsHandle import *
from os import system

args = getArgs(["zip","action"])

path = realpath(args.zip)

try:
    remove("tmp")
except:
    dummy=""

mkdir("tmp")
chdir("tmp")

extract(path)

system(args.action)

chdir("..")

remove("tmp")

