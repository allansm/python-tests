def extract(f):
    import py7zr

    archive = py7zr.SevenZipFile(f, mode='r')
    archive.extractall(path="")
    archive.close()

from dependency import *
include("../../python-lib")

from fileHandle import *
from os import chdir
from shutil import rmtree as remove

path = realpath("test.7z")

remove("test")
mkdir("test")
chdir("test")

extract(path)

print(readFile("a.txt"))
print(readFile("b.txt"))

chdir("..")

remove("test")

