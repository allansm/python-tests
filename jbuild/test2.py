import os
pdir = os.path.dirname(os.path.realpath(__file__))
wdir = os.getcwd()

os.chdir(pdir)

import sys
sys.path.append("../functions")

from fileHandle import *

os.chdir(wdir)

src = getAllFiles("src")
javac = []

for f in src:
    if ".java" in f:
        javac.append(os.path.dirname(f)+"\\"+"*.java")

javac = list(dict.fromkeys(javac))

for line in javac:
    os.system("javac -cp lib\* -d bin "+line)
