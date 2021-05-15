import os
pdir = os.path.dirname(os.path.realpath(__file__))
wdir = os.getcwd()

os.chdir(pdir)

import sys
sys.path.append("../functions")

from fileHandle import *

os.chdir(wdir)

bin = getAllFiles("bin")

i = 0

package = []

for b in bin:
    p = b.split(".")[0]
    p2 = b.split("\\")
    pa = "."
    pa = pa.join(p2)
    print(pa)
    #b.replace(".class","")
    package.append(pa)
    print(str(i)+" : "+b)
    i = i + 1
for p in package:
    print(p)
