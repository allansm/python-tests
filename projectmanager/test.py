import sys

sys.path.append("../functions")

from fileHandle import *

from os import chdir
from os import system

paths = getLines(".config")

command = input("command:")

for path in paths:
    chdir(path)
    system(command)
