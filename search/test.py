import sys

sys.path.append("../functions")

from fileHandle import *
from os.path import realpath
from os import chdir
from os import mkdir

chdir(getTemp())

try:
    mkdir("search")
except:
    dummy = ""

chdir("search")

path = input("path:")
fn = input("filename:")

print("getting files..")
files = getAllFiles(path)
print("files stored")
print("matching..")

for f in files:
    f = realpath(f)
    writeFile(".test",f+"\n")

