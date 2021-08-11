import sys
sys.path.append("../functions")

from fileHandle import *
import os

arr = ls(getTemp(),"*")

for a in arr:
    if("MEI" in a and "_" in a):
        print(a)
