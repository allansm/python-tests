import os
tmp = os.getcwd()

os.chdir(os.path.dirname(__file__))

import sys
sys.path.append("../functions")

from fileHandle import *

os.chdir(tmp)

size = 0

files = getAllFilesPath(".")

for f in files:
    size += os.path.getsize(f)

print(str(size/1000000)+" mb")
