import sys
sys.path.append("../functions")

from fileHandle import *
import os
from shutil import rmtree

def removeMei():
    arr = ls(getTemp(),"*")

    for a in arr:
        if("MEI" in a and "_" in a):
            rmtree(a, ignore_errors=True)
