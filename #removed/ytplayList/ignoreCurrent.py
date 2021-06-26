import sys
sys.path.append("../functions")

from fileHandle import *

from os import chdir

chdir(getTemp())

chdir("ytplaylist")

link = readFile("current.txt")

ignore = readFile("ignore.txt")

if(ignore != "" and ignore != None):
    writeFile(ignore,link+"\n")
    print("ignored:"+link)
    print("path:"+ignore)
