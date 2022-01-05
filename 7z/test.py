from dependency import *
include("../../python-lib")

from fileHandle import *
from os import chdir
from zip import *
from argsHandle import *
from os import system
from elapse import *


import py7zr
args = getArgs("z")

archive = py7zr.SevenZipFile(args.z, mode='r')
print(archive.getnames())
archive.close()
