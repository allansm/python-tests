from os import system
from os import chdir

import sys
sys.path.append("../functions")

from fileHandle import *

def test1():
    try:
        consumeLine("test.txt",0)

    except:
        print("pass")

def test2():
    chdir("e:\\")

    system("dir")

test2()
